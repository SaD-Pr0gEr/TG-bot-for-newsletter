import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOTS_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
DATABASE_URL = os.getenv("DATABASE_URL")
