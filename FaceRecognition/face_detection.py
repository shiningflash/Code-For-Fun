import cv2
import numpy as np
import face_recognition


def showResult(trainImg, testImage):
    encoded_train_img = face_recognition.face_encodings(trainImg)[0]
    encoded_test_img = face_recognition.face_encodings(testImage)[0]

    result = face_recognition.compare_faces([encoded_train_img], encoded_test_img)
    distance = face_recognition.face_distance([encoded_train_img], encoded_test_img)

    cv2.putText(testImage, f'{result} {round(distance[0], 2)}', (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    print(distance, result)


def resizeImg(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized


def detectFaceAndShow(img, msg):
    """ detect the face from image """
    face_loc_train = face_recognition.face_locations(img)[0]
    cv2.rectangle(img, (face_loc_train[3], face_loc_train[0]), (face_loc_train[1], face_loc_train[2]), (255, 0, 255), 2)

    """ show the detected face """
    cv2.imshow(msg, img)


def resizeImage(img):
    """ resize image if it's large
        otherwise, don't """
    x, y, z = img.shape
    if x * y * z > 500000:
        img = resizeImg(img, 40)
    return img


def loadImage(path):
    """ load train image of Elon Musk """
    img = face_recognition.load_image_file(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = resizeImage(img)
    return img


def trainTestImage():
    img_train = loadImage('images/Elon/ElonTrain.jpeg')
    img_test = loadImage('images/Elon/ElonTest.jpg')

    # img_train = loadImage('images/Faria/faria.jpeg')
    # img_test = loadImage('images/Faria/faizun_faria.jpeg')

    showResult(img_train, img_test)

    detectFaceAndShow(img_train, "Train Image")
    detectFaceAndShow(img_test, "Test Image")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    trainTestImage()


if __name__ == "__main__":
    main()