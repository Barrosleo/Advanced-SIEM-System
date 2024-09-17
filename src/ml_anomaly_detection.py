import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
import joblib

def train_model(features_path):
    data = pd.read_csv(features_path)
    X_train, X_test = train_test_split(data, test_size=0.2, random_state=42)
    model = IsolationForest(n_estimators=100, random_state=42)
    model.fit(X_train)
    predictions = model.predict(X_test)
    print(classification_report(X_test, predictions))
    return model

if __name__ == "__main__":
    model = train_model('../data/log_features.csv')
    joblib.dump(model, '../models/anomaly_detector.pkl')

