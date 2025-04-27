import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

dbtype = bool(os.getenv("DBTYPE"))
DB_TYPE = "sqlite" if dbtype else "postgres"
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

ADMIN_ID = ADMINS = [int(admin_id) for admin_id in os.getenv("ADMINS_ID").split(",")]
