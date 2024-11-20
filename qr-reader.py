import cv2
import json
from pyzbar.pyzbar import decode

# Function to decode QR code
def decode_qr_code(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    
    # Decode the QR code using pyzbar
    qr_codes = decode(img)
    
    if not qr_codes:
        print("No QR code found in the image.")
        return None
    
    for qr_code in qr_codes:
        # Convert byte data to https link
        qr_link = qr_code.data.decode("utf-8")

        # Print the decoded https link
        print(f"Decoded QR code: {qr_link}")

        return qr_link

# Path to the QR code image
qr_code_image_path = "portfolio_qr_code.png"

# Call the function to decode the QR code
decoded_data = decode_qr_code(qr_code_image_path)

if decoded_data:
    print(f"Decoded data: {decoded_data}")
else:
    print("No QR code found in the image.")