# Importer et ouvrir une image en gris

import cv2

def display_images(filename):
    img = cv2.imread(filename,0)
    cv2.imshow('Image',img)
    k = cv2.waitKey(0) & 0xFF  #because we're in x64
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite(filename[0:len(filename)-4]+" gray.png",img)
        cv2.destroyAllWindows()

display_images('Data/tetris_blocks.png')
