
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load candidate data
df = pd.read_csv("candidates.csv")

# Preprocess data
# ...preprocessing code...

# Extract features and labels
X = df[["experience", "skills", "education", "certifications"]]
y = df["score"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model.joblib")