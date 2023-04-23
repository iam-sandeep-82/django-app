import pytesseract as tess
from PIL import Image
import cv2
import time
tess.pytesseract.tesseract_cmd=r'C:\tesseract\tesseract.exe'
image = cv2.imread('E:\\Pics for OCR\\fines.png') 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
print(tess.image_to_string(gray_image))
