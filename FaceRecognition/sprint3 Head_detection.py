import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

def head_detector(filename):
    """
    filename : a raw string with the path to the file (e.g. r'C:/Users/loicd/PycharmProjects/facerecognition/Data/tetris_blocks.png' )
    /!\ It works only with .png
    return : None, displays a print of the image with rectangles around the face and the eyes
    exit by pressing any key
    """
    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv.imshow('Head Detection',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

head_detector('Data/Lassale_003.png')
