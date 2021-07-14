import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOTS_TOKEN")
USER = os.getenv("SQL_USER")
PASSWORD = os.getenv("SQL_PASSWORD")
DB = os.getenv("SQL_DB")
HOST = os.getenv("SQL_HOST")
PORT = os.getenv("SQL_PORT")
ADMIN = os.getenv("ADMIN_ID")
