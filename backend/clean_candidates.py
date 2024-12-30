import pandas as pd
from dateutil import parser
import re

# Load the candidate database
file_path = "candidate_database.xlsx"
df = pd.read_excel(file_path)

# Select only relevant columns for the database
required_columns = ["Name", "Experiences", "Skills", "Educations", "Disqualified"]
df = df[required_columns]

# Fill missing values with defaults
df["Experiences"] = df["Experiences"].fillna("None")
df["Skills"] = df["Skills"].fillna("None")
df["Educations"] = df["Educations"].fillna("None")
df["Disqualified"] = df["Disqualified"].fillna("No")

# Normalize Skills (convert to lists)
df["Skills"] = df["Skills"].apply(lambda x: x.lower().split("|") if isinstance(x, str) else [])

# Calculate Total Experience in Years
def calculate_total_experience(experiences):
    total_months = 0
    if isinstance(experiences, str):
        jobs = experiences.split("|")
        for job in jobs:
            match = re.search(r"\((.*?) to (.*?)\)", job)
            if match:
                start_date = match.group(1).strip()
                end_date = match.group(2).strip()
                if end_date == "N/A":
                    end_date = "Dec 2024"  # Assume the current date for ongoing jobs
                try:
                    start = parser.parse(start_date)
                    end = parser.parse(end_date)
                    total_months += (end.year - start.year) * 12 + (end.month - start.month)
                except Exception:
                    continue
    return round(total_months / 12, 2)  # Convert months to years

df["Total_Experience_Years"] = df["Experiences"].apply(calculate_total_experience)

# Optional: Exclude disqualified candidates (if needed)
# df = df[df["Disqualified"] != "Yes"]

# Save the cleaned data to a CSV file
cleaned_csv_path = "cleaned_candidates.csv"
df.to_csv(cleaned_csv_path, index=False)

print(f"Cleaned candidates saved as '{cleaned_csv_path}'.")
