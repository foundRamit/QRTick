import os

def create_folders():
    folders = [
        "QRTick/artifacts/qr",
        "QRTick/artifacts/tickets",
        "QRTick/utils",
        "qr_codes"
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Create __init__.py to make utils a package
    with open("QRTick/utils/__init__.py", "w") as f:
        f.write("# Init file to make utils a package")

    print("✅ Folder structure set up successfully!")

if __name__ == "__main__":
    create_folders()
