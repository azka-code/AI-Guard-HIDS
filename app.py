import streamlit as st
import sqlite3
import pandas as pd

from ai_engine import analyze_security_event

DATABASE = "data/alerts.db"


st.set_page_config(
    page_title="AI Guard HIDS",
    page_icon="🛡️",
    layout="wide"
)


def get_alerts():
    connection = sqlite3.connect(DATABASE)

    query = """
        SELECT
            id,
            timestamp,
            event_type,
            source,
            severity,
            log_message,
            status
        FROM alerts
        ORDER BY id DESC
    """

    dataframe = pd.read_sql_query(query, connection)

    connection.close()

    return dataframe


# --------------------------------
# HEADER
# --------------------------------

st.title("🛡️ AI Guard - Host-Based Intrusion Detection System")

st.caption(
    "Real-time Linux security monitoring, threat detection and AI-assisted analysis"
)

st.divider()


# --------------------------------
# LOAD ALERTS
# --------------------------------

df = get_alerts()


# --------------------------------
# STATISTICS
# --------------------------------

if not df.empty:

    total_alerts = len(df)

    high_alerts = len(
        df[df["severity"] == "HIGH"]
    )

    medium_alerts = len(
        df[df["severity"] == "MEDIUM"]
    )

    low_alerts = len(
        df[df["severity"] == "LOW"]
    )

else:

    total_alerts = 0
    high_alerts = 0
    medium_alerts = 0
    low_alerts = 0


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Alerts", total_alerts)

with col2:
    st.metric("High Severity", high_alerts)

with col3:
    st.metric("Medium Severity", medium_alerts)

with col4:
    st.metric("Low Severity", low_alerts)


st.divider()


# --------------------------------
# ALERT DISTRIBUTION
# --------------------------------

st.subheader("Alert Distribution")

if not df.empty:

    severity_counts = (
        df["severity"]
        .value_counts()
        .rename_axis("Severity")
        .reset_index(name="Count")
    )

    st.bar_chart(
        severity_counts.set_index("Severity")
    )

else:

    st.info("No security alerts detected yet.")


# --------------------------------
# HISTORICAL EVENTS
# --------------------------------

st.subheader("Historical Security Events")

if not df.empty:

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No historical events available.")


# --------------------------------
# AI SECURITY ANALYSIS
# --------------------------------

st.divider()

st.subheader("🤖 AI Security Analyst")

if not df.empty:

    selected_id = st.selectbox(
        "Select a security event",
        df["id"].tolist()
    )

    selected_event = df[
        df["id"] == selected_id
    ].iloc[0]

    st.write("### Selected Event")

    st.write(
        f"**Event Type:** {selected_event['event_type']}"
    )

    st.write(
        f"**Severity:** {selected_event['severity']}"
    )

    st.write(
        f"**Source:** {selected_event['source']}"
    )

    st.code(
        selected_event["log_message"]
    )

    if st.button("🔍 Analyze with AI"):

        with st.spinner("AI is analyzing the security event..."):

            try:

                analysis = analyze_security_event(
                    selected_event["event_type"],
                    selected_event["severity"],
                    selected_event["log_message"]
                )

                st.success("AI Analysis Complete")

                st.markdown(analysis)

            except Exception as error:

                st.error(
                    f"AI analysis failed: {error}"
                )

else:

    st.info(
        "No security events available for AI analysis."
    )

# --------------------------------
# SECURITY CHATBOT
# --------------------------------

st.divider()

st.subheader("💬 AI Security Chatbot")

user_question = st.text_input(
    "Ask a question about detected security events",
    placeholder="What happened in the last hour?"
)


if st.button("Ask AI"):

    if user_question.strip():

        recent_events = df.head(20)

        if recent_events.empty:

            st.info("No security events are currently stored.")

        else:

            event_context = recent_events.to_string(
                index=False
            )

            chatbot_prompt = f"""
You are the AI security analyst for AI Guard HIDS.

Answer the user's question using only the security events
provided below.

Security Events:
{event_context}

User Question:
{user_question}

Provide a clear cybersecurity-focused answer.
Mention relevant event types, severity and source where useful.
If the available logs do not contain enough information,
clearly say that the information is not available.
"""

            try:

                from groq import Groq
                import os
                from dotenv import load_dotenv

                load_dotenv()

                client = Groq(
                    api_key=os.getenv("GROQ_API_KEY")
                )

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a defensive cybersecurity analyst."
                        },
                        {
                            "role": "user",
                            "content": chatbot_prompt
                        }
                    ],
                    temperature=0.2
                )

                answer = response.choices[0].message.content

                st.markdown("### AI Response")

                st.markdown(answer)

            except Exception as error:

                st.error(
                    f"Chatbot error: {error}"
                )

    else:

        st.warning("Please enter a question.")
# --------------------------------
# REFRESH
# --------------------------------

st.divider()

if st.button("🔄 Refresh Dashboard"):

    st.rerun()