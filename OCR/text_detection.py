""" 
    install opencv [$ sudo apt install python3-opencv]

    verify installation of opencv
    python3 -c "import cv2; print(cv2.__version__)"

    run this code [$ python3 ./text_detection.py]

"""

import cv2
import pytesseract as tess

""" show image """
def showImage(img):
    cv2.imshow('Result', img)
    cv2.waitKey(0)

""" detecting characters """
def detectChar(img):
    height, weight, _ = img.shape
    boxes = tess.image_to_boxes(img)
    for b in boxes.splitlines():
        # print(b)
        b = b.split(' ')
        print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, height-y), (w, height-h), (0, 0, 255), 1)
        cv2.putText(img, b[0], (x, height-y+18), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

""" detecting words """
def detectWord(img):
    height, weight, _ = img.shape
    boxes = tess.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
                cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

if __name__ == "__main__":
    """ load image """
    img = cv2.imread('1.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # showImage(img)

    """ print image to string """
    # print(tess.image_to_string(img))

    """ detecting characters """ 
    # detectChar(img)

    """ detecting words """
    # detectWord(img)

    str = tess.image_to_string(img)
    print(str)
    

showImage(img)


