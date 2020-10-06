import cv2
import os
import numpy as np
import face_recognition


path = 'image_dir'
images = []
class_names = []
encode_list = []
my_list = os.listdir(path)


def findEncodings(images):
    for img in images:
        print(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)


def init():
    for cl in my_list:
        cur_img = cv2.imread(f'{path}/{cl}')
        images.append(cur_img)
        class_names.append(os.path.splitext(cl)[0])


def main():
    init()    
    findEncodings(images)
    
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

        face_frame = face_recognition.face_locations(imgs)
        encode_frame = face_recognition.face_encodings(imgs, face_frame)

        for encode_face, face_loc in zip(encode_frame, face_frame):
            matches = face_recognition.compare_faces(encode_list, encode_face)
            face_dis = face_recognition.face_distance(encode_list, encode_face)
            print(face_dis)


if __name__ == "__main__":
    main()