# AI Guard — Host-Based Intrusion Detection System

AI Guard is a Python-based Host-Based Intrusion Detection System designed to monitor Linux security logs, detect suspicious activities, and provide AI-assisted security analysis.

## Features

* Real-time log monitoring
* Failed login detection
* Brute-force detection
* Privilege escalation detection
* Port scan detection
* SQLite alert storage
* Streamlit security dashboard
* Groq-powered AI security analysis
* Natural-language security chatbot
* Historical event monitoring

## Technology Stack

* Python 3
* Watchdog
* Regex
* SQLite
* Streamlit
* Pandas
* Groq API
* python-dotenv
* ReportLab

## Detection Rules

### Failed Login

Detects failed SSH authentication attempts.

### Brute Force

Detects five or more failed login attempts from the same IP within 60 seconds.

### Privilege Escalation

Detects suspicious sudo events containing `USER=root`.

### Port Scan

Detects controlled port-scan events represented in the monitored log.

## Project Structure

```text
AI-Guard-HIDS/
│
├── app.py
├── watcher.py
├── detector.py
├── database.py
├── ai_engine.py
├── config.py
├── create_rule_pdf.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── logs/
│   └── sample_auth.log
│
├── rules/
│   └── detection_rules.md
│
└── screenshots/
```

## How It Works

1. The log watcher monitors the configured Linux security log.
2. New log entries are passed to the detection engine.
3. Custom regex-based rules identify suspicious events.
4. Detected events are stored in SQLite.
5. The Streamlit dashboard displays alerts and historical events.
6. The Groq-powered AI engine analyzes security events and provides explanations and remediation guidance.
7. The natural-language chatbot allows users to ask questions about security events.

## Alert Severity

| Event                | Severity |
| -------------------- | -------- |
| Failed Login         | LOW      |
| Brute Force          | HIGH     |
| Privilege Escalation | HIGH     |
| Port Scan            | MEDIUM   |

## Installation

Create a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

Do not upload the `.env` file or expose the API key publicly.

## Running the System

Start the log monitor:

```bash
python3 watcher.py
```

In another terminal, start the Streamlit dashboard:

```bash
streamlit run app.py
```

## Testing

The system can be tested using controlled sample log entries representing:

* Failed login attempts
* Brute-force activity
* Privilege escalation events
* Port-scan events

The project can also be validated in a controlled lab environment using security-testing tools.

## AI Security Analysis

The system uses the Groq API to provide AI-assisted analysis of detected security events.

The AI assistant can:

* Explain what happened
* Explain why the event may be a security concern
* Suggest remediation steps
* Recommend what the administrator should check next

The analysis is intended to assist security monitoring and does not replace professional security investigation.

## Dashboard

The Streamlit dashboard provides:

* Security event metrics
* Alert severity information
* Historical security events
* AI-assisted event analysis
* Natural-language security chatbot functionality

## Documentation

The repository includes detection-rule documentation covering the implemented detection rules, severity levels, SQLite storage, AI analysis, testing, and project limitations.

## Security Note

This project is an educational cybersecurity prototype developed for learning and internship evaluation. It is not intended to replace enterprise-grade security monitoring, endpoint detection and response systems, or professional Security Operations Center infrastructure.

## Limitations

* The current prototype focuses on Linux log monitoring.
* Detection rules are based on predefined patterns and thresholds.
* Port-scan detection is represented through controlled log events in the prototype.
* AI analysis depends on the availability of the Groq API.
* The system is an internship-level prototype and has not been designed as a production enterprise security solution.
