import tkinter as tk
import picamera

import euro_detect
import calcul_somme

camera = picamera.PiCamera()

camera.resolution = (1640,1232)

# On affiche l'image prise par la camera en direct
camera.start_preview(fullscreen=False,window=(100,100,500,800))

def photo():
    # On enregistre la photo
    camera.capture('/home/pi/Documents/picture.jpg')

    # On appelle les différentes fonctions et on affiche les résultats
    liste = euro_detect.main()
    text.delete('1.0', tk.END)
    text.insert(tk.INSERT, "Vous avez {} € \n".format(calcul_somme.calcul_somme(liste)))
    catalogue = calcul_somme.catalogue(liste)
    text.insert(tk.END, "Voici les pièces dont vous disposez : \n")
    for (key,value) in catalogue.items():
        text.insert(tk.END, "{} pièce(s) de {} \n".format(value, key))
    text.pack()

def quitter():
    camera.stop_preview()
    camera.close()
    root.destroy()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

#Bouton pour quitter le programme
button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quitter)
button.pack(side=tk.LEFT)

# Bouton pour prendre une photo
slogan = tk.Button(frame,
                   text="Photo",
                   command=photo)
slogan.pack(side=tk.LEFT)

text = tk.Text(root)
text.insert(tk.END, "Prenez une photo")
text.pack()

root.mainloop()
