import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from utils import extract_features  # Import feature extraction function

# Load the dataset
file_path = "PhiUSIIL_Phishing_URL_Dataset.csv"
data = pd.read_csv(file_path, encoding="utf-8", low_memory=False)

# Identify the column containing URLs and labels
urls = data["URL"]  # Replace with the actual column name
labels = data["label"]  # Replace with the actual column name

# Extract features
data["features"] = urls.apply(extract_features)
X = list(data["features"])
y = labels

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate and save the model
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
joblib.dump(model, "model.pkl")
print("Model saved as 'model.pkl'")
