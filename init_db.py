import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Get MongoDB URI from .env
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("⚠️ MONGODB_URI is missing from the .env file.")

# Connect to MongoDB
client = MongoClient(MONGODB_URI)

# Create database & collection
db = client["QRTickDB"]
collection = db["qr_codes"]

print("✅ Database and collection initialized successfully!")

# Close connection
client.close()
