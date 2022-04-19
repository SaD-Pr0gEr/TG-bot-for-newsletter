import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

BOT_TOKEN = os.getenv("BOTS_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
BASE = declarative_base()
