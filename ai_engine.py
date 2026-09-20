import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=GROQ_API_KEY)


def analyze_security_event(event_type, severity, log_message):
    prompt = f"""
You are a cybersecurity assistant inside a Host-Based Intrusion Detection System.

Analyze the following security event.

Event Type: {event_type}
Severity: {severity}
Log Message: {log_message}

Provide:
1. What happened
2. Why it may be a security concern
3. Recommended remediation steps
4. What the system administrator should check next

Keep the explanation practical and beginner-friendly.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a cybersecurity monitoring assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content