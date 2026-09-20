import re
from datetime import datetime, timedelta
from database import save_alert

failed_attempts = {}

BRUTE_FORCE_THRESHOLD = 5
BRUTE_FORCE_WINDOW = 60

FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password .* from (?P<ip>\d+\.\d+\.\d+\.\d+\b)"
)

PRIVILEGE_PATTERN = re.compile(
    r"sudo:.*USER=root"
)

PORT_SCAN_PATTERN = re.compile(
    r"PORT_SCAN detected from (?P<ip>\d+\.\d+\.\d+\.\d+\b)"
)


def detect_brute_force(source_ip):
    now = datetime.now()

    if source_ip not in failed_attempts:
        failed_attempts[source_ip] = []

    failed_attempts[source_ip].append(now)

    cutoff_time = now - timedelta(seconds=BRUTE_FORCE_WINDOW)

    failed_attempts[source_ip] = [
        timestamp
        for timestamp in failed_attempts[source_ip]
        if timestamp >= cutoff_time
    ]

    if len(failed_attempts[source_ip]) >= BRUTE_FORCE_THRESHOLD:
        return True

    return False


def analyze_log_line(line):

    # Failed Login / Brute Force
    failed_login = FAILED_LOGIN_PATTERN.search(line)

    if failed_login:
        source_ip = failed_login.group("ip")

        if detect_brute_force(source_ip):
            save_alert(
                event_type="Brute Force Attempt",
                source=source_ip,
                severity="HIGH",
                log_message=line.strip()
            )

            return "Brute Force Attempt detected"

        save_alert(
            event_type="Failed Login",
            source=source_ip,
            severity="LOW",
            log_message=line.strip()
        )

        return "Failed Login detected"

    # Privilege Escalation
    privilege_event = PRIVILEGE_PATTERN.search(line)

    if privilege_event:
        save_alert(
            event_type="Privilege Escalation Attempt",
            source="Local System",
            severity="HIGH",
            log_message=line.strip()
        )

        return "Privilege Escalation Attempt detected"

    # Port Scan
    port_scan = PORT_SCAN_PATTERN.search(line)

    if port_scan:
        source_ip = port_scan.group("ip")

        save_alert(
            event_type="Port Scan",
            source=source_ip,
            severity="MEDIUM",
            log_message=line.strip()
        )

        return "Port Scan detected"

    return None
