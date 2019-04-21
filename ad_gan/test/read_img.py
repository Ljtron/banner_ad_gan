import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
img = cv2.imread('img2.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
s = pytesseract.image_to_string(gray)
print(s)