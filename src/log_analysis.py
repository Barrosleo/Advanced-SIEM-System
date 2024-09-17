import json

def analyze_logs(logs):
    alerts = []
    for log in logs:
        if "ERROR" in log or "WARNING" in log:
            alerts.append(log)
    return alerts

if __name__ == "__main__":
    with open("../data/collected_logs.json", 'r') as log_file:
        logs = json.load(log_file)
    alerts = analyze_logs(logs)
    with open("../data/alerts.json", 'w') as alert_file:
        json.dump(alerts, alert_file)
    print(f"Generated {len(alerts)} alerts.")
