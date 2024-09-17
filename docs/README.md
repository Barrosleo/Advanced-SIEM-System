# Advanced SIEM System

## Description
This project is a Security Information and Event Management (SIEM) system that collects, analyzes, and responds to security events in real-time.

## Skills
- Python
- Log Analysis
- Networking
- Machine Learning

## Features
- Log collection from multiple sources
- Log analysis to detect warnings and errors
- Machine learning for anomaly detection
- Real-time event response

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Barrosleo/Advanced-SIEM-System.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Advanced-SIEM-System/src
    ```
3. Install required libraries:
    ```bash
    pip install pandas scikit-learn joblib
    ```
4. Collect logs:
    ```bash
    python log_collection.py
    ```
5. Analyze logs:
    ```bash
    python log_analysis.py
    ```
6. Train the machine learning model:
    ```bash
    python ml_anomaly_detection.py
    ```
7. Respond to events:
    ```bash
    python event_response.py
    ```

## Usage
- Place your log files in the `data/logs/` directory.
- Run the scripts to collect logs, analyze them, train the model, and respond to events.
