from PIL import Image, ImageTk
import tkinter as tk
import argparse
import datetime
import cv2
import os

class Application:
    def __init__(self, output_path = "/Desktop/pi"):
        """ Initialise des fonctions qui montrent la vue webcam, et qui pilotent la prise de photo """
        self.videostream = cv2.VideoCapture(0) # capture le flux vidéo, 0 est la caméra vidéo par défaut de l'ordinateur
        self.output_path = output_path  # retient le chemin d'enregirstrement
        self.current_image = None  # current image from the camera

        self.fenetre = tk.Tk()  # initialise la fenêtre d'affichage
        self.fenetre.title("ReCoinition")  # ajoute un titre

        self.panel = tk.Label(self.fenetre)  # initialise le panel d'images
        self.panel.pack(padx=10, pady=10)

        # crée un bouton qui, fait un screenshot de la vidéo et ferme la fenêtre
        bouton = tk.Button(self.fenetre, text="Prendre une photo", command=self.take_snapshot)
        bouton.pack(fill="both", expand=True, padx=10, pady=10)

        # commence une boucle vidéo qui affiche la vidéo
        self.video_loop()

    def video_loop(self):
        """ Get frame from the video stream and show it in Tkinter """
        ok, frame = self.videostream.read()  # read frame from video stream
        if ok:  # frame captured without any errors
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convertit les couleurs from BGR to RGBA
            self.current_image = Image.fromarray(cv2image)  # convert image for PIL
            current_image = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter
            self.panel.current_image = current_image  # anchor imgtk so it does not be deleted by garbage-collector
            self.panel.config(image=current_image)  # affiche image
        self.fenetre.after(30, self.video_loop)  # reprend une photo toutes les 30 millisecondes

    def take_snapshot(self):
        """ prend un sceenshot et l'enregistre, puis ferme la fenêtre """
         # grab the current timestamp
        filename = ("{}.jpg".format("photo_pièce"))  # construit le nom du fichier
        p = os.path.join(self.output_path, filename)  # construit le chemin d'enregistrement
        cv2.imwrite(p, (self.videostream.read())[1].copy())  # enregistre l'image sous Jpeg
        print("[INFO] saved {}".format(filename))
        quit()



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", default="./",
    help="path to output directory to store snapshots (default: current folder")
args = vars(ap.parse_args())

# lance l'application
print("[INFO] starting...")
pba = Application(args["output"])
pba.fenetre.mainloop()
