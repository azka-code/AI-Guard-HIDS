from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)


OUTPUT_FILE = "Rule_Documentation.pdf"


# ---------------------------------------
# PDF DOCUMENT
# ---------------------------------------

document = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=45,
    bottomMargin=45
)


# ---------------------------------------
# STYLES
# ---------------------------------------

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    fontSize=22,
    leading=28,
    alignment=TA_CENTER,
    spaceAfter=15
)

subtitle_style = ParagraphStyle(
    "SubtitleStyle",
    parent=styles["Normal"],
    fontSize=12,
    leading=18,
    alignment=TA_CENTER,
    spaceAfter=25
)

heading_style = ParagraphStyle(
    "HeadingStyle",
    parent=styles["Heading2"],
    fontSize=15,
    leading=20,
    spaceBefore=15,
    spaceAfter=8
)

body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontSize=10,
    leading=15,
    spaceAfter=8
)

bullet_style = ParagraphStyle(
    "BulletStyle",
    parent=body_style,
    leftIndent=15,
    firstLineIndent=-8
)


# ---------------------------------------
# CONTENT
# ---------------------------------------

story = []


# COVER
story.append(Spacer(1, 100))

story.append(
    Paragraph(
        "AI Guard",
        title_style
    )
)

story.append(
    Paragraph(
        "Host-Based Intrusion Detection System",
        subtitle_style
    )
)

story.append(
    Paragraph(
        "Detection Rule Documentation",
        heading_style
    )
)

story.append(
    Paragraph(
        "Python-based defensive cybersecurity internship project",
        subtitle_style
    )
)

story.append(Spacer(1, 100))

story.append(
    Paragraph(
        "This document describes the custom detection rules, "
        "alert severity classification, storage mechanism, "
        "AI-assisted analysis and testing methodology used "
        "in the AI Guard HIDS prototype.",
        body_style
    )
)

story.append(PageBreak())


# ---------------------------------------
# 1. PROJECT OVERVIEW
# ---------------------------------------

story.append(
    Paragraph(
        "1. Project Overview",
        heading_style
    )
)

story.append(
    Paragraph(
        "AI Guard is a Python-based Host-Based Intrusion Detection "
        "System designed to monitor Linux security logs in real time. "
        "The prototype uses custom detection rules to identify "
        "suspicious authentication and privilege-related activity.",
        body_style
    )
)

story.append(
    Paragraph(
        "Detected events are stored in an SQLite database and "
        "displayed through a Streamlit dashboard. The prototype "
        "also integrates the Groq API to provide AI-assisted "
        "security event explanations and remediation guidance.",
        body_style
    )
)


# ---------------------------------------
# 2. DETECTION ARCHITECTURE
# ---------------------------------------

story.append(
    Paragraph(
        "2. Detection Architecture",
        heading_style
    )
)

story.append(
    Paragraph(
        "The monitoring workflow consists of the following stages:",
        body_style
    )
)

architecture_items = [
    "Linux security log or simulated security log generates an event.",
    "Watchdog monitors the log file for newly appended entries.",
    "The detector analyzes each new log line using custom rules.",
    "Detected events are stored in SQLite.",
    "The Streamlit dashboard displays current and historical alerts.",
    "Groq AI can analyze selected events and provide remediation guidance."
]

for item in architecture_items:
    story.append(
        Paragraph(
            "• " + item,
            bullet_style
        )
    )


# ---------------------------------------
# 3. FAILED LOGIN
# ---------------------------------------

story.append(
    Paragraph(
        "3. Failed Login Detection",
        heading_style
    )
)

story.append(
    Paragraph(
        "Objective: Detect unsuccessful SSH authentication attempts "
        "recorded in the monitored Linux authentication log.",
        body_style
    )
)

story.append(
    Paragraph(
        "Detection pattern: The rule searches for failed password "
        "messages containing a source IP address.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Example:</b> Failed password for invalid user admin "
        "from 192.168.56.101",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Severity:</b> LOW",
        body_style
    )
)

story.append(
    Paragraph(
        "Response: The detected event is stored in SQLite with "
        "timestamp, source IP, severity and the original log message.",
        body_style
    )
)


# ---------------------------------------
# 4. BRUTE FORCE
# ---------------------------------------

story.append(
    Paragraph(
        "4. Brute Force Detection",
        heading_style
    )
)

story.append(
    Paragraph(
        "Objective: Detect repeated failed authentication attempts "
        "from the same source IP address.",
        body_style
    )
)

story.append(
    Paragraph(
        "Detection logic: Five or more failed login attempts from "
        "the same IP address within a 60-second window are classified "
        "as a brute-force attempt.",
        body_style
    )
)

brute_table = Table(
    [
        ["Parameter", "Value"],
        ["Threshold", "5 failed attempts"],
        ["Time Window", "60 seconds"],
        ["Severity", "HIGH"]
    ],
    colWidths=[150, 250]
)

brute_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 6),
    ])
)

story.append(brute_table)
story.append(Spacer(1, 10))

story.append(
    Paragraph(
        "Response: The event is stored in SQLite and can be "
        "analyzed through the Groq-powered AI security assistant.",
        body_style
    )
)


# ---------------------------------------
# 5. PRIVILEGE ESCALATION
# ---------------------------------------

story.append(
    Paragraph(
        "5. Privilege Escalation Detection",
        heading_style
    )
)

story.append(
    Paragraph(
        "Objective: Identify suspicious sudo events involving "
        "root-level privileges.",
        body_style
    )
)

story.append(
    Paragraph(
        "Detection pattern: The rule searches for sudo log entries "
        "containing USER=root.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Example:</b> sudo: kali : user NOT in sudoers ; "
        "USER=root ; COMMAND=/bin/bash",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Severity:</b> HIGH",
        body_style
    )
)

story.append(
    Paragraph(
        "Response: The event is stored as a privilege escalation "
        "alert and displayed on the dashboard.",
        body_style
    )
)


# ---------------------------------------
# 6. PORT SCAN
# ---------------------------------------

story.append(
    Paragraph(
        "6. Port Scan Detection",
        heading_style
    )
)

story.append(
    Paragraph(
        "Objective: Identify port-scanning activity represented "
        "in the monitored security log.",
        body_style
    )
)

story.append(
    Paragraph(
        "Detection pattern: The system detects controlled log "
        "entries containing PORT_SCAN followed by a source IP address.",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Example:</b> PORT_SCAN detected from 127.0.0.1",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Severity:</b> MEDIUM",
        body_style
    )
)

story.append(
    Paragraph(
        "Validation: Port scanning functionality is validated "
        "in an authorized local laboratory using Nmap. A controlled "
        "port-scan event is also used to test the HIDS detection rule.",
        body_style
    )
)


# ---------------------------------------
# 7. SEVERITY CLASSIFICATION
# ---------------------------------------

story.append(
    Paragraph(
        "7. Alert Severity Classification",
        heading_style
    )
)

severity_table = Table(
    [
        ["Severity", "Meaning"],
        [
            "LOW",
            "Individual suspicious event requiring review"
        ],
        [
            "MEDIUM",
            "Suspicious network activity requiring investigation"
        ],
        [
            "HIGH",
            "Activity that may indicate an active attack "
            "or privilege-related threat"
        ]
    ],
    colWidths=[100, 300]
)

severity_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 6),
    ])
)

story.append(severity_table)


# ---------------------------------------
# 8. DATABASE STORAGE
# ---------------------------------------

story.append(
    Paragraph(
        "8. Alert Storage",
        heading_style
    )
)

story.append(
    Paragraph(
        "Detected security events are stored in an SQLite database.",
        body_style
    )
)

storage_items = [
    "Alert ID",
    "Timestamp",
    "Event Type",
    "Source",
    "Severity",
    "Original Log Message",
    "Status"
]

for item in storage_items:
    story.append(
        Paragraph(
            "• " + item,
            bullet_style
        )
    )


# ---------------------------------------
# 9. AI ANALYSIS
# ---------------------------------------

story.append(
    Paragraph(
        "9. AI-Assisted Security Analysis",
        heading_style
    )
)

story.append(
    Paragraph(
        "The prototype integrates the Groq API to provide "
        "AI-assisted analysis of detected security events.",
        body_style
    )
)

ai_items = [
    "Explanation of what happened",
    "Why the event may be a security concern",
    "Recommended remediation steps",
    "Suggested administrator checks"
]

for item in ai_items:
    story.append(
        Paragraph(
            "• " + item,
            bullet_style
        )
    )

story.append(
    Paragraph(
        "The AI assistant is intended to support security analysis "
        "and does not replace human investigation or professional "
        "security operations.",
        body_style
    )
)


# ---------------------------------------
# 10. TESTING
# ---------------------------------------

story.append(
    Paragraph(
        "10. Testing Methodology",
        heading_style
    )
)

testing_items = [
    "Failed login events were generated in the controlled log file.",
    "Five failed login attempts from the same source were used "
    "to validate brute-force detection.",
    "A controlled sudo USER=root event was used to validate "
    "privilege escalation detection.",
    "Nmap was used against an authorized local laboratory target "
    "for port-scanning validation.",
    "The Streamlit dashboard was used to verify stored alerts.",
    "Groq AI analysis was tested using detected security events."
]

for item in testing_items:
    story.append(
        Paragraph(
            "• " + item,
            bullet_style
        )
    )


# ---------------------------------------
# 11. LIMITATIONS
# ---------------------------------------

story.append(
    Paragraph(
        "11. Limitations",
        heading_style
    )
)

story.append(
    Paragraph(
        "This internship prototype uses simulated Linux log data "
        "for demonstration and controlled testing. It is not intended "
        "to represent complete enterprise-grade intrusion detection "
        "coverage.",
        body_style
    )
)

story.append(
    Paragraph(
        "The current prototype focuses on selected authentication, "
        "privilege and port-scan detection rules. Additional detection "
        "rules, endpoint telemetry and machine-learning capabilities "
        "can be added in future development phases.",
        body_style
    )
)


# ---------------------------------------
# BUILD PDF
# ---------------------------------------

document.build(story)

print("=" * 50)
print("Rule Documentation PDF created successfully!")
print("File:", OUTPUT_FILE)
print("=" * 50)
