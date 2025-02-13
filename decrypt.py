import cv2

img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Read stored password and message length
try:
    with open("encryption_data.txt", "r") as f:
        stored_password = f.readline().strip()  
        msg_length = int(f.readline().strip()) 
except FileNotFoundError:
    print("Error: Encryption data not found!")
    exit()

pas = input("Enter passcode for Decryption: ")

if stored_password == pas:
    message = ""
    n, m = 0, 0

    # Decrypt message from the image
    for _ in range(msg_length):
        message += chr(img[n, m, 0])  
        m += 1  
        if m >= img.shape[1]:  
            m = 0
            n += 1

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
