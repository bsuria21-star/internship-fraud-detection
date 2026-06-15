import pandas as pd
import joblib

model = joblib.load('fraud_model.joblib')
# Test data: 0.2 speed, 1 IP, 1 score
new_app = pd.DataFrame([[0.2, 1, 1]], columns=['submission_speed', 'ip_count', 'email_type_score'])
prediction = model.predict(new_app)

if prediction[0] == -1:
    print("Result: 🚨 FRAUD detected!")
else:
    print("Result: ✅ NORMAL application.")