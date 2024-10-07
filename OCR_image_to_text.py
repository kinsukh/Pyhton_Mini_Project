## link "github.com/UB-Mannheim/tesseract/wiki" and download the .exe file for your system

## pip install tesseract

import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' ## path to the tesseract.exe file

def convert():
    img = Image.open('image.png')
    text = pytesseract.image_to_string(img)    
    return text

print(convert())