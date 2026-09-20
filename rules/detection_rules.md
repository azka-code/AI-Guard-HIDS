# AI Guard HIDS — Detection Rule Documentation

## 1. Failed Login Detection

### Objective
Detect unsuccessful SSH authentication attempts.

### Detection Pattern
The system searches Linux authentication logs for failed password messages containing a source IP address.

### Example Event
Failed password for invalid user admin from 192.168.56.101

### Severity
LOW

### Response
The event is stored in SQLite with timestamp, source IP, severity and original log message.

---

## 2. Brute Force Detection

### Objective
Detect repeated failed authentication attempts from the same source.

### Detection Logic
Five or more failed login attempts from the same IP address within 60 seconds are classified as a brute-force attempt.

### Threshold
5 attempts

### Time Window
60 seconds

### Severity
HIGH

### Response
The event is stored in SQLite and can be analyzed by the Groq-powered AI security assistant.

---

## 3. Privilege Escalation Detection

### Objective
Identify suspicious attempts involving root privileges.

### Detection Pattern
The rule searches for sudo log entries containing USER=root.

### Example Event
sudo: kali : user NOT in sudoers ; USER=root ; COMMAND=/bin/bash

### Severity
HIGH

### Response
The event is stored as a privilege escalation alert and presented on the dashboard.

---

## 4. Port Scan Detection

### Objective
Identify port scanning activity represented in the monitored security log.

### Detection Pattern
The system detects log entries containing PORT_SCAN followed by a source IP address.

### Example Event
PORT_SCAN detected from 127.0.0.1

### Severity
MEDIUM

### Validation
Port scanning functionality is validated in an authorized local lab using Nmap. A controlled port-scan event is also inserted into the simulated log to test the HIDS detection rule.

---

## 5. Alert Severity Levels

| Severity | Meaning |
|---|---|
| LOW | Individual suspicious event requiring review |
| MEDIUM | Suspicious network activity requiring investigation |
| HIGH | Activity that may indicate an active attack or privilege-related threat |

---

## 6. Storage

Detected security events are stored in SQLite.

Stored fields include:

- Alert ID
- Timestamp
- Event Type
- Source
- Severity
- Original Log Message
- Status

---

## 7. AI Analysis

Detected events can be analyzed using the Groq API.

The AI assistant provides:

- Event explanation
- Security significance
- Recommended remediation
- Suggested administrator checks

The AI response is intended to assist security analysts and does not replace human investigation.

---

## 8. Limitations

This internship prototype uses simulated Linux log data for demonstration.

The current prototype is designed for controlled lab testing and does not claim to provide complete enterprise-grade intrusion detection coverage.
