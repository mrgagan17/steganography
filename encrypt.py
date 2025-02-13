import cv2
import os
import numpy as np

img = cv2.imread("mypic.jpg")
if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

with open("encryption_data.txt", "w") as f:
    f.write(password + "\n")
    f.write(str(len(msg)) + "\n")

ascii_values = [ord(char) for char in msg]

n, m = 0, 0

# Encrypt message into the image (using the blue channel)
for val in ascii_values:
    img[n, m, 0] = val 
    m += 1
    if m >= img.shape[1]:
        m = 0
        n += 1

# Save the encrypted image
cv2.imwrite("encryptedImage.png", img)  
os.system("start encryptedImage.png") 
print("Message encrypted successfully!")
