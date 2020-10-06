import cv2
import os
import numpy as np
import face_recognition
from datetime import datetime

path = 'image_dir'
images = []
class_names = []
encode_list = []
my_list = os.listdir(path)


def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
        data_list = f.readlines()
        name_list = []
        for line in data_list:
            entry = line.split(',')
            name_list.append(entry[0])
        if name not in name_list:
            now = datetime.now()
            date_str = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{date_str}')


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
           #  print(face_dis)

        match_index = np.argmin(face_dis)
        
        if matches[match_index]:
            name = class_names[match_index].upper()
            print(name)
            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            markAttendance(name)

        cv2.imshow('Webcam', img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()