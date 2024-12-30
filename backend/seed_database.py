import csv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import Candidate  # Your SQLAlchemy model for the candidates table
from app.config import settings  # Assuming your config module is at the same level

# Determine if running in test mode (optional)
is_test_mode = False  # Set to True if you want to seed a test database

# Database connection using settings.get_database_uri
engine = create_engine(settings.get_database_uri(is_test=is_test_mode))
Session = sessionmaker(bind=engine)
session = Session()

# Read the cleaned CSV and seed the database
with open("cleaned_candidates.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    headers = next(reader)  # Get the first row as headers
    print(headers)
    for row in reader:
        candidate = Candidate(
            name=row["Name"],
            experience=float(row["Total_Experience_Years"]),
            skills=row["Skills"],
            education=row["Educations"],
        )
        session.add(candidate)

session.commit()
print("Database seeded successfully.")
