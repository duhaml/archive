import cv2
import numpy as np
from matplotlib import pyplot as plt

def img_display(filename,color=0):
    """
    filename : a raw string with the path to the file (e.g. 'C:/Users/loicd/PycharmProjects/facerecognition/Data/tetris_blocks.png' )
    color : int, 1 for colored image, 0 for gray, -1 for normal
    return : None, displays a print of the image
    exit by pressing ESC, save and exit with 's' key
    """
    img = cv2.imread(filename,color)    #loading image
    cv2.imshow('image',img)             #displaying the image
    #closing the image
    k = cv2.waitKey(0) & 0xFF
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        #finding the right name : we only want what is after the last slash in filename
        name = filename.partition('/')[-1]
        while name.partition('/')[-1] != '':
            name = name.partition('/')[-1]
        cv2.imwrite(name,img)
        cv2.destroyAllWindows()


def process_image_plus_de_bordures(filename):
    """
    filename : a raw string with the path to the file (e.g. 'C:/Users/loicd/PycharmProjects/facerecognition/Data/tetris_blocks.png' )
    return : None, displays a print of the processed image
    """
    img = cv2.imread(filename,0)     #loading image
    edges = cv2.Canny(img,100,200)   #processing (canny edge detection)
    #displaying the image :
    cv2.imshow('image',edges)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        #finding the right name : we only want what is after the last slash in filename
        name = filename.partition('/')[-1]
        while name.partition('/')[-1] != '':
            name = name.partition('/')[-1]
        name = name.partition('.')[0]   #the .png at the end of the doc name is deleted
        namedge = name + '_edged.png'
        cv2.imwrite(namedge,edges)
        cv2.destroyAllWindows()

def process_image_flou(filename):
    """
    filename : a raw string with the path to the file (e.g. 'C:/Users/loicd/PycharmProjects/facerecognition/Data/tetris_blocks.png' )
    return : None, displays a print of the processed image
    """
    img = cv2.imread(filename)
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

process_image_flou('Data\tetris_blocks.png')
