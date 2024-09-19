import qrcode
from io import BytesIO
from base64 import b64encode

def generate_qr_code(medication_info):
    """
    Generate a QR code based on medication information (e.g., medication name, dosage).
    :param medication_info: Dictionary containing medication details.
    :return: QR code image in base64 format.
    """
    qr_data = f"{medication_info['medication_name']}|{medication_info['dosage']}|{medication_info['instructions']}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    
    # Converts the QR code image to base64 format to send it as JSON response
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = b64encode(buffered.getvalue()).decode('utf-8')
    
    return img_str


def decode_qr_code(qr_code_data):
    """
    Decode QR code data into medication details.
    :param qr_code_data: Base64 encoded QR code string.
    :return: Dictionary containing medication details.
    """
    # In this placeholder example, we simulate decoding by splitting the QR code string.
    medication_info = qr_code_data.split('|')
    return {
        "medication_name": medication_info[0],
        "dosage": medication_info[1],
        "instructions": medication_info[2]
    }
