import qrcode
from PIL import Image

# Ask the user for the HTTPS link to encode
print("Welcome to the QR Code Generator!")
print("-----------------------------------")
link = input("Please enter the HTTPS link you'd like to encode: ")

# Validate the user input
while not link.startswith("https://"):
    print("Oops, it looks like you didn't enter a valid HTTPS link.")
    print("Please try again!")
    link = input("Enter the HTTPS link: ")

# Create a QR code from the HTTPS link
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

# Generate the QR code image with a higher quality
img = qr.make_image(fill_color='black', back_color='white', image_factory=None)

# Ask the user for a filename
filename = input("What would you like to name your QR code image? (e.g. 'my_qr_code.png'): ")

# Validate the filename
while not filename.endswith(".png"):
    print("Oops, it looks like you didn't enter a valid filename.")
    print("Please try again!")
    filename = input("Enter a filename (e.g. 'my_qr_code.png'): ")

# Save the QR code as an image file with the user-specified filename
img.save(filename)

print(f"QR code generated and saved as {filename}!")