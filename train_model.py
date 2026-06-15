import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load data
df = pd.read_csv('data.csv')
# Train model
model = IsolationForest(n_estimators=100, contamination=0.3, random_state=42)
model.fit(df)

# Save model
joblib.dump(model, 'fraud_model.joblib')
print("Model trained successfully!")