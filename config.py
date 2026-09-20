import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DATABASE_PATH = "data/alerts.db"

LOG_FILE = "logs/sample_auth.log"

BRUTE_FORCE_THRESHOLD = 5

BRUTE_FORCE_WINDOW = 60