from tkinter import *
from Partie import Partie
from PIL import Image,ImageTk

fenetre=Tk()
fenetre.title("Flood it !")
HAUTEUR=600
LARGEUR=600
N=15
COTE=min(HAUTEUR,LARGEUR)//N
centreH=(HAUTEUR-N*COTE)//2
centreL=(LARGEUR-N*COTE)//2
dessin=Canvas(fenetre,width=LARGEUR,height=HAUTEUR,background="white")
mona=Image.open("Morgana.png")
mona=ImageTk.PhotoImage(mona.convert("RGBA"))

couleurs=["#900","#090","#009","#990","#909","#099"]

partie=Partie(6,N)
plateau=partie.plateau()

for i in range(N):
    for j in range(N):
        dessin.create_rectangle(centreL+j*COTE,centreH+i*COTE,centreL+(j+1)*COTE,centreH+(i+1)*COTE,fill=couleurs[plateau[i][j]])

def clic(event):
    global fait
    if not fait :
        dessin.delete("all")
        y,x=event.x, event.y
        #print(x//COTE,y//COTE)
        partie.repandre(x//COTE,y//COTE)
        plateau=partie.plateau()
        for i in range(N):
            for j in range(N):
                dessin.create_rectangle(centreL+j*COTE,centreH+i*COTE,centreL+(j+1)*COTE,centreH+(i+1)*COTE,fill=couleurs[plateau[i][j]])
        if partie.victoire():
            fait = not fait
            dessin.delete("all")
            dessin.create_rectangle(centreL,centreH,centreL+LARGEUR,centreH+HAUTEUR,fill=couleurs[plateau[0][0]])
            #texte=Label(fenetre,width=20,text="VICTIORE !") Ne marche pas
            dessin.create_text(LARGEUR//2,HAUTEUR*0.9,anchor="n",text="VICTIORE !",fill="black")
            #mona=PhotoImage("~/Projet Python/Projet_Flood_it/Morgana.png") : Ne marche pas
            #photo=Label(fenetre,image=mona) : Ne marche pas
            dessin.create_image(300,300,image=mona,anchor="c")

fait = False

dessin.bind("<Button-1>",clic)

dessin.grid(column=0,row=0)
fenetre.mainloop()