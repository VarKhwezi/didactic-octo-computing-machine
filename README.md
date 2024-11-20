# didactic-octo-computing-machine

QR Code Generator and Reader

This repository contains two Python scripts: qr-writer.py and qr-reader.py. These scripts allow you to generate and read QR codes, respectively.

QR-Writer

qr-writer.py is a script that generates a QR code from a given HTTPS link. The script uses the qrcode library to create the QR code and saves it as a PNG image.

Usage

To use qr-writer.py, simply run the script and follow the prompts:

bash
Copy Insert in Terminal
python qr-writer.py
You will be asked to enter the HTTPS link you want to encode in the QR code. The script will then generate the QR code and save it as a PNG image.

QR-Reader

qr-reader.py is a script that reads a QR code from a given image file. The script uses the pyzbar library to decode the QR code and extract the embedded HTTPS link.

Usage

To use qr-reader.py, simply run the script and pass the path to the QR code image file as an argument:

bash
Copy Insert in Terminal
python qr-reader.py path/to/image.png
The script will then read the QR code and print the embedded HTTPS link.

Dependencies

Both scripts require the following dependencies to be installed:

qrcode: a library for generating QR codes
pyzbar: a library for reading QR codes
opencv-python: a library for image processing
pillow: a library for image processing
You can install these dependencies using pip:

bash
CopyInsert in Terminal
pip install qrcode pyzbar opencv-python pillow
Troubleshooting

If you encounter any issues while running the scripts, please make sure that you have the latest versions of the dependencies installed. You can also try running the scripts in a virtual environment to isolate any issues.

License

This repository is licensed under the MIT License. Feel free to use and modify the scripts as you see fit.

Acknowledgments

This repository uses the following third-party libraries:

qrcode: https://github.com/lincolnloop/python-qrcode
pyzbar: https://github.com/NaturalHistoryMuseum/pyzbar
opencv-python: https://github.com/opencv/opencv-python
pillow: https://github.com/python-pillow/Pillow
