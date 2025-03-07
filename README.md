Steganography

This project implements image steganography using OpenCV and Python. It allows users to hide a secret message inside an image by modifying pixel values and later retrieve the hidden message using a passcode.

 Features
- Hide a secret message inside an image.
- Protects message access with a password.
- Uses image pixels for message storage.
- Supports encryption & decryption.
- Works with .jpg and .png images.

Technologies Used
- Python
- OpenCV
- NumPy

Install required libraries

- pip install opencv-python numpy

Encryption Process

Run the encryption script:
- python encrypt.py
- Enter your secret message and a passcode.

Decryption Process

Run the decryption script:
- python decrypt.py
- Enter the correct passcode to reveal the hidden message.
