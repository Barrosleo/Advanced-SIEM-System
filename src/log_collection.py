import os
import json

def collect_logs(log_directory):
    logs = []
    for filename in os.listdir(log_directory):
        if filename.endswith(".log"):
            with open(os.path.join(log_directory, filename), 'r') as file:
                logs.extend(file.readlines())
    return logs

if __name__ == "__main__":
    log_directory = "../data/logs"
    logs = collect_logs(log_directory)
    with open("../data/collected_logs.json", 'w') as log_file:
        json.dump(logs, log_file)
    print(f"Collected {len(logs)} log entries.")
