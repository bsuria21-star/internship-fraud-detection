Fraud Detection System
This project implements a machine learning-based Fraud Detection System using the Isolation Forest algorithm.It is designed to identify anomalous patterns in transaction data, distinguishing between legitimate and potentially fraudulent activities.

Key Features:
Anomaly Detection: Utilizes the Isolation Forest algorithm to efficiently isolate outliers in datasets.

Model Persistence: Uses joblib to save and load the trained model for future predictions.

Data Driven: Analyzes features such as submission_speed, ip_count, and email_type_score to determine the risk level of an application.

How it works:
The system trains on historical data to learn the "normal" behavior. When a new application is submitted, the model analyzes the input and classifies it as either Normal or Fraudulent.

How to Run:
Clone this repository to your local machine.

Install the required libraries:

Bash
pip install pandas scikit-learn joblib
Run the training script:

Bash
python train_model.py
Run the prediction script:

Bash
python predict.py
