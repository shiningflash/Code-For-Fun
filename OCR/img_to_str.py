import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'


img = cv2.imread('1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th = 255 - cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

th = cv2.GaussianBlur(th, (3,3), 0)
result = pytesseract.image_to_string(th, lang='eng', config='--psm 6')

print(result)

"""
cv2.imshow("image", img)
cv2.waitKey(0)
"""