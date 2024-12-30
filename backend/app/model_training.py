import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
import os

# Check if cleaned CSV exists
cleaned_file = "../cleaned_candidates.csv"
if not os.path.exists(cleaned_file):
    print(f"Warning: {cleaned_file} not found. Skipping model training.")
    exit(0)

# Load cleaned candidate data
df = pd.read_csv(cleaned_file)

# Fill missing values (just in case)
df["Total_Experience_Years"] = df["Total_Experience_Years"].fillna(0.0)
df["Skills"] = df["Skills"].fillna("")

# Extract features and labels
X_numerical = df[["Total_Experience_Years"]]
y = df["Disqualified"].apply(lambda x: 0 if x == "No" else 1)  # Use "Disqualified" as the target for training

# Use TF-IDF for skills
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(df["Skills"])

# Combine numerical and text features
X_combined = hstack([X_tfidf, X_numerical])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_combined, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")
print("Model and vectorizer saved as 'model.joblib' and 'vectorizer.joblib'.")
