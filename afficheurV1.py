from tkinter import *
from Partie import Partie
from PIL import Image,ImageTk

fenetre=Tk()
fenetre.title("Flood it !")
HAUTEUR=600
LARGEUR=600
N=14
COTE=min(HAUTEUR,LARGEUR)//N
centreH=(HAUTEUR-N*COTE)//2
centreL=(LARGEUR-N*COTE)//2
dessin=Canvas(fenetre,width=LARGEUR,height=HAUTEUR,background="white")
mona=Image.open("Morgana.png")
mona=ImageTk.PhotoImage(mona.convert("RGBA"))
aie=Image.open("Dommage.png")
aie=ImageTk.PhotoImage(aie.convert("RGBA"))

texte=StringVar() 
texte.set("0 coup / 22")
coup=Label(fenetre,width=30,textvariable=texte)

couleurs=["#900","#090","#009","#990","#909","#099"]

partie=Partie(6,N)
plateau=partie.plateau()

for i in range(N):
    for j in range(N):
        dessin.create_rectangle(centreL+j*COTE,centreH+i*COTE,centreL+(j+1)*COTE,centreH+(i+1)*COTE,fill=couleurs[plateau[i][j]],outline='')

def clic(event):
    global fait, partie
    if not fait :
        y,x=event.x-centreL, event.y-centreH
        #print(x//COTE,y//COTE)
        if 0<=x//COTE<N and 0<=y//COTE<N:
            dessin.delete("all")
            partie.repandre(x//COTE,y//COTE)
            texte.set(f"{partie.total()} coup / 22" if partie.total()<=1 else f"{partie.total()} coups / 22" )
            plateau=partie.plateau()
            for i in range(N):
                for j in range(N):
                    dessin.create_rectangle(centreL+j*COTE,centreH+i*COTE,centreL+(j+1)*COTE,centreH+(i+1)*COTE,fill=couleurs[plateau[i][j]],outline='')
            if partie.victoire():
                fait = not fait
                #texte=Label(fenetre,width=20,text="VICTIORE !") Ne marche pas
                dessin.create_text(LARGEUR//2,HAUTEUR*0.9,anchor="n",text="VICTIORE !",fill="black")
                #mona=PhotoImage("~/Projet Python/Projet_Flood_it/Morgana.png") : Ne marche pas
                #photo=Label(fenetre,image=mona) : Ne marche pas
                dessin.create_image(LARGEUR//2,HAUTEUR//2,image=mona,anchor="c")
            elif partie.defaite():
                fait = not fait
                dessin.create_text(LARGEUR//2,HAUTEUR*0.9,anchor="n",text="Dommage...",fill="black")
                dessin.create_image(LARGEUR//2,HAUTEUR//2,image=aie,anchor="c")
    else :
        partie=Partie(6,N)
        plateau=partie.plateau()

        for i in range(N):
            for j in range(N):
                dessin.create_rectangle(centreL+j*COTE,centreH+i*COTE,centreL+(j+1)*COTE,centreH+(i+1)*COTE,fill=couleurs[plateau[i][j]],outline='')
        fait=not fait
        texte.set("0 coup / 22")



fait = False

dessin.bind("<Button-1>",clic)

dessin.grid(column=0,row=0)
coup.grid(column=0,row=1)
fenetre.mainloop()
