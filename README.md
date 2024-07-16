# Image Steganography with Python

This project implements image steganography using LSB method to hide a text messsage inside an image.
The LSB of image pixels are manipulated to store the message bit by bit. 
The image difference is not noticable to naked eyes.

## Requirements

- Python 3.x
- OpenCV
- PIL (Pillow)
- NumPy
- Matplotlib

## Installation

You can install the required packages using pip:
```bash
pip install opencv-python pillow numpy matplotlib
```
Then clone the repo to your local machine and navigate to the folder
```bash
git clone https://github.com/chaitraDev/Image_Steganography.git
cd Image_Steganography
```
Make sure to rename your image file as 'image_steganography.png' and then run the script 
```bash
python image_steganography.py
```

## Future Scope
- As of now, the message is storing from 1st pixel, we could randomize the starting index
- Using any encryption algorithm like RSA, the starting index can be encrypted
- Using socket programming, an interface could be made where people could share the steg images and hide the messages.
