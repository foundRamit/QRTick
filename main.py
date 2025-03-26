import os
import sys
from dotenv import load_dotenv
from pymongo import MongoClient
from QRTick.utils.generateQr import QrCodeGenerator  

# Ensure correct import paths
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), "QRTick"))

# Load environment variables
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("⚠️ MONGODB_URI is missing from the .env file.")

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client["QRTickDB"]
collection = db["qr_codes"]

# Initialize QR Code Generator
QrCode = QrCodeGenerator()

def generate_qr_entry():
    reg_no = input("Enter your registration number: ").strip()
    user_name = input("Enter your name: ").strip()

    if not reg_no or not user_name:
        print("⚠️ Registration number and name cannot be empty!")
        return
    
    # Generate the QR Code
    qr_code_path = QrCode.generate_qr_code(reg_no, user_name)

    # Store in MongoDB
    qr_document = {
        "user_name": user_name,
        "reg_no": reg_no,
        "qr_code_path": qr_code_path
    }

    collection.insert_one(qr_document)
    print(f"✅ QR Code generated and saved to database: {qr_code_path}")

if __name__ == "__main__":
    generate_qr_entry()
