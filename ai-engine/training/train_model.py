import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load metrics dataset
data = pd.read_csv("metrics.csv")

X = data.drop("failure", axis=1)
y = data["failure"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "../models/random_forest.pkl")
print("✅ Failure prediction model trained & saved")

