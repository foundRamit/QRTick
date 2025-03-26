import qrcode
import os

class QrCodeGenerator:

    @staticmethod
    def generate_qr_code(reg_no, user_name):
        # Ensure QR storage directory exists
        os.makedirs("qr_codes", exist_ok=True)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"Reg No: {reg_no}, Name: {user_name}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="green", back_color="black")

        qr_code_path = f"qr_codes/{user_name}_{reg_no}.png"
        img.save(qr_code_path)
        return qr_code_path
