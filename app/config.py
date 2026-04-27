import os
from dotenv import load_dotenv

# Load .env once
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")