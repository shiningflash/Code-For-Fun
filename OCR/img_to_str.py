# install tesseract-ocr ( $ sudo apt-get install tesseract-ocr )
# install pytesseract and pillow ( $ pip3 install pillow pytesseract )

from PIL import Image
import pytesseract as tess

img = Image.open("b.png")
str = tess.image_to_string(img, lang="eng")

print(str)