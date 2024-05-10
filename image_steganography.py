# ===== Setup and Preprocessing ===== #
import cv2
from google.colab.patches import cv2_imshow
import PIL
from PIL import Image
import numpy as np

img = cv2.imread("image_steganography.png")

cv2_imshow(img)

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2_imshow(grey)

print(grey.shape)

''' 
    1. Take the ascii values of characters in the text
    2. Take their binaries
    3. Pad those binaries to be of length 8
    4. Group all the binaries together to store in image
'''
secret = "Image Steganography is COOL"

def text2binary(sentence,max_len=9):
  binary = ""
  for word in sentence:
    for char in word:
      ascii = ord(char)
      binary += format(ascii,"08b")#number to 8 bits binary
  return binary

def hide(cover_img,msg):
  """ adds bits in msg to each pixel of image, one by one """
  """ returns the modified array of pixels"""
  index = 0
  msg_length = len(msg)
  rows,cols = len(cover_img),len(cover_img[0])

  for rowInd in range(rows):
    for colInd in range(cols):
      val = cover_img[rowInd][colInd]
      #find what is the last bit
      last_bit = val&1
      msg_bit = msg[index]
      #change only if needed
      if last_bit==0 and msg_bit=='1':#the number is eve
        val += 1
      elif last_bit==1 and msg_bit=='0':#the number is odd
        val -= 1

      cover_img[rowInd][colInd] = val

      index += 1
      if index == msg_length:
        return cover_img

binary = text2binary(secret)
print(binary)

stego_pixels = hide(grey,binary)

# ===== Steganography Result ===== #
stego_img = Image.fromarray(stego_pixels)
print(stego_img)

stego_img.save("stego_img.png")

import matplotlib.pyplot as plt

fig,ax = plt.subplots(1,2,figsize=(10,3))

fig.suptitle("Difference Between Original and Changed Image",y=-0.1)

ax[0].imshow(grey, cmap='gray', vmin=0, vmax=255)
ax[0].set_title("Cover Image")

ax[1].imshow(stego_img, cmap='gray', vmin=0, vmax=255)
ax[1].set_title("Stego Image")
plt.show()

# ===== Reveal ===== #
def reveal(stego_img,msg_length):
  binary_text = ""
  index = 0
  for row in stego_img:
    for val in row:
      last_bit = val&1
      binary_text += str(last_bit)
      index += 1
      if index == msg_length:
        return binary_text

def binary_to_text(binary):
  bin_length = len(binary)
  secret = ""
  for index in range(0,bin_length,8):
    first_char = binary[index:index+8]
    ascii = int(first_char,2)
    char = chr(ascii)
    secret += char
  return secret

steg_color = cv2.imread("stego_img.png")
steg_grey = cv2.cvtColor(steg_color,cv2.COLOR_BGR2GRAY)

secret_bin = reveal(steg_grey,len(secret)*8)
print(secret_bin)

text = binary_to_text(str(secret_bin))
print(text)