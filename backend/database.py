from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

print(f"DEBUG: MONGO_URL = {MONGO_URL}")
print(f"DEBUG: DB_NAME = {DB_NAME}")

if not MONGO_URL or not DB_NAME:
    raise ValueError("MONGO_URL or DB_NAME environment variables not set!")

try:
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    print("MongoDB connection initialized")
except Exception as e:
    print(f"ERROR: Failed to connect to MongoDB: {e}")
    raise