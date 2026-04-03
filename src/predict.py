import pandas as pd
import joblib

# Load your full pipeline (feature + preprocess + model)
model = joblib.load("artifacts/model.pkl")

# -----------------------------
# Sample Test Input (RAW DATA)
# -----------------------------
test_data = pd.DataFrame([{
    "Pclass": 3,
    "Name": "Braund, Mr. Owen Harris",
    "Sex": "male",
    "Age": 22,
    "SibSp": 1,
    "Parch": 0,
    "Fare": 7.25,
    "Embarked": "S",
    "Cabin": None
}])

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict(test_data)[0]
probability = model.predict_proba(test_data)[0][1]

print("Prediction (0 = No, 1 = Yes):", prediction)
print("Survival Probability:", probability)