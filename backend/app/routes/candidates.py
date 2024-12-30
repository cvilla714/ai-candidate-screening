from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Candidate
from ..schemas import JobDescription
from app.utils.pdf_utils import extract_text_from_pdf  # Import utility function
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import hstack


router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Load the trained model
model = joblib.load("app/model.joblib")
vectorizer = joblib.load("app/vectorizer.joblib")


@router.post("/upload-description/")
async def upload_description(file: UploadFile = File(...)):
    """
    Endpoint to upload a job description PDF and extract its content.

    Args:
        file (UploadFile): The uploaded job description PDF.

    Returns:
        dict: Extracted text from the PDF.
    """
    try:
        # Save the uploaded file temporarily
        file_location = f"/tmp/{file.filename}"
        with open(file_location, "wb") as temp_file:
            temp_file.write(file.file.read())

        # Extract text from the PDF using t`he utility function
        description = extract_text_from_pdf(file_location)

        return {"message": "Job description uploaded successfully", "description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")


@router.post("/score-candidates/")
async def score_candidates(job_description: JobDescription, db: Session = Depends(get_db)):
    """
    Endpoint to score candidates based on a job description.

    Args:
        job_description (JobDescription): The job description input.
        db (Session): Database session.

    Returns:
        dict: Top 30 candidates with scores.
    """
    # Load candidates from the database
    candidates = db.query(Candidate).all()
    skills = [candidate.skills for candidate in candidates]
    experiences = [candidate.experience for candidate in candidates]

    # Compute similarity scores (if applicable)
    vectors = vectorizer.transform([job_description.description] + skills)
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    # Predict scores using the model
    X_combined = hstack([vectorizer.transform(skills), [[exp] for exp in experiences]])
    predicted_scores = model.predict(X_combined)
    
    # Combine predicted scores with similarity scores
    combined_scores = [
        {
            "name": candidates[i].name,
            "score": round((0.7 * predicted_scores[i] + 0.3 * similarities[i]) * 100, 2)  # Scale to 0-100
        }
        for i in range(len(candidates))
    ]

    # combined_scores = [
    #     {"name": candidates[i].name, "score": 0.7 * predicted_scores[i] + 0.3 * similarities[i]}
    #     for i in range(len(candidates))
    # ]

    # Sort and return top 30 candidates
    top_candidates = sorted(combined_scores, key=lambda x: x["score"], reverse=True)[:30]
    return {"top_candidates": top_candidates}


