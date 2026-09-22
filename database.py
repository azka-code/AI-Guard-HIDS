import sqlite3
import os
from datetime import datetime

DATABASE = "data/alerts.db"

os.makedirs("data", exist_ok=True)


def init_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            event_type TEXT NOT NULL,
            source TEXT,
            severity TEXT NOT NULL,
            log_message TEXT NOT NULL,
            status TEXT DEFAULT 'NEW'
        )
    """)

    connection.commit()
    connection.close()


def save_alert(event_type, source, severity, log_message):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO alerts
        (timestamp, event_type, source, severity, log_message)
        VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        event_type,
        source,
        severity,
        log_message
    ))

    connection.commit()
    connection.close()


def get_alerts():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, timestamp, event_type, source,
               severity, log_message, status
        FROM alerts
        ORDER BY id DESC
    """)

    alerts = cursor.fetchall()
    connection.close()

    return alerts
