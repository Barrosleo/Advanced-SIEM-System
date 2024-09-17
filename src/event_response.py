import json
import joblib

def respond_to_events(alerts, model_path):
    model = joblib.load(model_path)
    for alert in alerts:
        prediction = model.predict([alert])
        if prediction == -1:
            print(f"Anomaly detected: {alert}")
            # Add your response logic here

if __name__ == "__main__":
    with open("../data/alerts.json", 'r') as alert_file:
        alerts = json.load(alert_file)
    respond_to_events(alerts, '../models/anomaly_detector.pkl')
