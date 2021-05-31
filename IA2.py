from random import randint
from tkinter import *
from Partie import Partie
from PIL import Image,ImageTk
from copy import deepcopy
from os import fork
from time import time

#mona=Image.open("Morgana.png")
#mona=ImageTk.PhotoImage(mona.convert("RGBA"))

fenetre=Tk()
fenetre.title("Flood it !")
HAUTEUR=600
LARGEUR=600
N=50
k=6
COTE=min(HAUTEUR,LARGEUR)//N
centreH=(HAUTEUR-N*COTE)//2
centreL=(LARGEUR-N*COTE)//2
dessin1=Canvas(fenetre,width=LARGEUR,height=HAUTEUR,background="white")
dessin2=Canvas(fenetre,width=LARGEUR,height=HAUTEUR,background="white")

#Initialisation

couleurs=["#900","#090","#009","#990","#909","#099"]

partie1=Partie(k,N)
plateau1=partie1.plateau()
partie2=deepcopy(partie1)
plateau2=partie2.plateau()

for i in range(N):
    for j in range(N):
        dessin1.create_rectangle(centreL+j*COTE,centreH+i*COTE,centreL+(j+1)*COTE,centreH+(i+1)*COTE,fill=couleurs[plateau1[i][j]],outline='')

for i in range(N):
    for j in range(N):
        dessin2.create_rectangle(centreL+j*COTE,centreH+i*COTE,centreL+(j+1)*COTE,centreH+(i+1)*COTE,fill=couleurs[plateau2[i][j]],outline='')

text1=Label(text="Choix Gluton :\nMaximum coloré aux bords")
text2=Label(text="Choix Gluton :\nMaximum coloré aux bords\nCases entourées exclus")

dessin1.grid(row=1,column=0)
dessin2.grid(row=1,column=1)
text1.grid(row=0,column=0)
text2.grid(row=0,column=1)

def glouton1():
    tableau=[set() for i in range(k)]
    for (i,j) in partie1.bords():
        n=partie1.plateau()[i][j]
        if (i,j) not in tableau[n]:
            tableau[n].update(partie1.expandre([(i,j)]))
    return list(max(tableau,key=len))

def isole(i : int, j : int, partie : Partie):
    return ((i==0 or partie.case_a_gauche(i,j) in partie.expansion)
        and (i==len(partie.plateau()) or partie.case_a_droite(i,j) in partie.expansion)
        and (j==0 or partie.case_en_haut(i,j) in partie.expansion)
        and (j==len(partie.plateau()) or partie.case_en_bas(i,j) in partie.expansion))

def glouton2():
    #Exclu du compte les cases entourés de  ceux déjà remplis
    tableau=[set() for i in range(k)]
    for (i,j) in partie2.bords():
        n=partie2.plateau()[i][j]
        if not isole(i,j,partie2) and (i,j) not in tableau[n]:
            tableau[n].update(partie2.expandre([(i,j)]))
    try:
        return list(max(tableau,key=len))[0]
    except:
        return (i,j)




def pick():
    global dessin1,partie1,tps,plateau1,fin1,fin2
    if not partie1.victoire():
        i,j=glouton1()[0]
        partie1.repandre(i,j)
        plateau1=partie1.plateau()
        for i in range(N):
            for j in range(N):
                dessin1.create_rectangle(centreL+j*COTE,centreH+i*COTE,centreL+(j+1)*COTE,centreH+(i+1)*COTE,fill=couleurs[plateau1[i][j]],outline='')
        #t=int((time()-tps)*1000)
        if fin2 :
            fenetre.after(1,pick)
            #print(t)
        else :
            fenetre.after(1,pick2)
    else:
        fin1=True
        dessin1.create_text(LARGEUR//2,HAUTEUR*0.9,anchor="n",text=f"VICTIORE !\nTerminé en {partie1.total()} coups",fill="black",justify="center")
        #dessin1.create_image(LARGEUR//2,HAUTEUR//2,image=mona,anchor="c")
        fenetre.after(1,pick2)


def pick2():
    global dessin2,partie2,tps,fin1,fin2
    if not partie2.victoire():
        i,j=glouton2()
        partie2.repandre(i,j)
        plateau2=partie2.plateau()
        for i in range(N):
            for j in range(N):
                dessin2.create_rectangle(centreL+j*COTE,centreH+i*COTE,centreL+(j+1)*COTE,centreH+(i+1)*COTE,fill=couleurs[plateau2[i][j]],outline='')
        t=int((time()-tps)*1000)
        if fin1:
            fenetre.after(1,pick2)
            #print(t)
        else :
            fenetre.after(1,pick)
    else:
        fin2=True
        dessin2.create_text(LARGEUR//2,HAUTEUR*0.9,anchor="n",text=f"VICTIORE !\nTerminé en {partie2.total()} coups",fill="black",justify="center")
        #dessin1.create_image(LARGEUR//2,HAUTEUR//2,image=mona,anchor="c")
        fenetre.after(1,pick)

fin1,fin2=False, False
tps=time()
#fenetre.after(1000,pick)
fenetre.after(1000,pick2)
fenetre.mainloop()