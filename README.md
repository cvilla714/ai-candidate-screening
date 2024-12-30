# AI-Powered Candidate Screening and Scoring System

This project is an AI-powered application for screening and scoring candidates based on their resumes and job descriptions. The system uses Natural Language Processing (NLP) techniques to analyze and rank candidates according to their relevance for a specific job role.

## Features

- Upload and parse job descriptions (PDFs).
- Score and rank candidates based on experience, skills, and job description relevance.
- Display the top 30 candidates with their scores.
- Backend built with FastAPI and frontend built with React.
- Machine Learning model for candidate scoring.

## Technologies Used

- **Backend**: FastAPI, Python
- **Frontend**: React
- **Database**: PostgreSQL
- **Machine Learning**: Scikit-learn
- **Deployment**: Docker

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your local machine.
- PostgreSQL database.

### Clone the Repository

```bash
git clone git@github.com:cvilla714/ai-candidate-screening.git
cd python_challenge
```

### Environment Variables

Create a `.env` file in the `conf` directory part of `backend` folder with the following content:

```env
DB_HOST=db
DB_NAME=candidates_db
DB_USER=user
DB_PASS=password
DB_PORT=5432
```

### Build and Run the Application

1. Build and start the Docker containers:

   ```bash
   docker compose up -d --build
   ```

2. Access the frontend at [http://localhost:3000](http://localhost:3000).
3. Access the FastAPI Swagger documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

### Database Setup

1. Run Alembic migrations to create the database schema:

   ```bash
   docker exec -it python_challenge-backend-1 alembic upgrade head
   ```

2. Seed the database with initial data:

   ```bash
   docker exec -it python_challenge-backend-1 python seed_database.py
   ```

### Test the Application

1. Use Postman or any API testing tool to interact with the API endpoints:

   - `/api/upload-description/`: Upload a job description PDF.
   - `/api/score-candidates/`: Get the top candidates for a given job description.

2. Alternatively, use the web interface to upload a job description and view results.

## Project Structure

```plaintext
python_challenge/
├── backend/
│   ├── alembic/               # Database migrations
│   ├── app/
│   │   ├── models.py          # Database models
│   │   ├── routes/            # API routes
│   │   ├── utils/             # Utility scripts
│   │   ├── main.py            # FastAPI application
│   │   └── config.py          # Configuration settings
│   ├── conf/                  # Configuration folder
|   |   └── .env               # Environment variables
│   ├── Dockerfile             # Dockerfile for backend
│   ├── requirements.txt       # Python dependencies
│   └── seed_database.py       # Script to seed database
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js             # React application
│   │   └── index.js           # React entry point
│   ├── Dockerfile             # Dockerfile for frontend
│   └── package.json           # Node.js dependencies
├── docker-compose.yml         # Docker Compose configuration
└── README.md                  # Project documentation
```

## Challenges Faced

1. **Docker Configuration**:

   - Created separate Dockerfiles for backend and frontend.
   - Configured `docker-compose.yml` for multi-container setup.

2. **Database Integration**:

   - Integrated PostgreSQL and used Alembic for database migrations.
   - Addressed issues with environment variables and connection strings.

3. **Data Cleaning and Preprocessing**:

   - Developed a script to clean and preprocess candidate data.
   - Converted Excel data to CSV format and calculated total experience.

4. **Machine Learning Model**:

   - Trained a Random Forest model for candidate scoring.
   - Saved the model and vectorizer as `.joblib` files.

5. **Frontend-Backend Integration**:

   - Implemented CORS middleware to enable frontend-backend communication.
   - Added React components for uploading job descriptions and displaying results.

6. **API Testing**:
   - Used Postman to test endpoints during development.
   - Verified the end-to-end functionality through the UI.

## Future Enhancements

- Add user authentication and role-based access control.
- Deploy the application to a cloud platform.
- Improve the machine learning model's accuracy with additional features and fine-tuning.
- Enhance the frontend with better styling and responsiveness.
