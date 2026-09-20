# AI Guard — Host-Based Intrusion Detection System

AI Guard is a Python-based Host-Based Intrusion Detection System designed to monitor Linux security logs, detect suspicious activities and provide AI-assisted security analysis.

## Features

- Real-time log monitoring
- Failed login detection
- Brute-force detection
- Privilege escalation detection
- Port scan detection
- SQLite alert storage
- Streamlit security dashboard
- Groq-powered AI security analysis
- Natural-language security chatbot
- Historical event monitoring

## Technology Stack

- Python 3
- Watchdog
- Regex
- SQLite
- Streamlit
- Pandas
- Groq API
- python-dotenv
- ReportLab

## Detection Rules

### Failed Login
Detects failed SSH authentication attempts.

### Brute Force
Detects five or more failed login attempts from the same IP within 60 seconds.

### Privilege Escalation
Detects suspicious sudo events containing USER=root.

### Port Scan
Detects controlled port-scan events represented in the monitored log.

## Project Structure

```text
ProStackHub_HIDS/
│
├── app.py
├── watcher.py
├── detector.py
├── database.py
├── ai_engine.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── alerts.db
│
├── logs/
│   └── sample_auth.log
│
├── rules/
│   └── detection_rules.md
│
└── screenshots/