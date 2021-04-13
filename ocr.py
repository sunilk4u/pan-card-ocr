# Required Libraries and Imports
# Using Tesseract OCR and Open CV

import pytesseract
import cv2
import re

images = ["1.jpg", "2.jpg", "3.jpg"]

pytesseract.pytesseract.tesseract_cmd = r"./Tesseract/tesseract.exe"    #tesseract OCR path

for image in images:                         #loops through list of images
    img = cv2.imread("" + image + "")                                   
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)      #changing image to gray scale or binary color
    img = cv2.resize(img, None, fx=2, fy=2)          #zoom into the images for better scanning                    
    ret, img = cv2.threshold(img, 95, 255, cv2.THRESH_BINARY)       #applying threshold to images

    data = pytesseract.image_to_string(img)

    print("------   PAN CARD " + str(images.index(image)+1) + "   ------")

    date_of_birth = re.findall("([0-9]+/[0-9]+/[0-9]+)", data)
    pan_no = re.findall("([A-Z]+[0-9]+[A-Z])", data)

    print("Pan Card Number :", pan_no[0])
    print("Date of Birth   :", date_of_birth[0])
    print("\n")