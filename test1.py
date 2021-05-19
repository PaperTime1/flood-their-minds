from tkinter import *

#Objectifs : Création de premier Widget et familiarisation avec la modification dynamique de texte

morceau="I do not want to pay I'll never do that again don't lean on the table you are not allowed to cry boomerang don't let me hurt the camels".split()
k=len(morceau)

def augmenter():
    global n
    n+=1
    texte.set(morceau[n%k])

def reduire():
    global n
    n-=1
    texte.set(morceau[n%k])

fenetre=Tk()
fenetre['bg']="blue"
bouton1=Button(fenetre,text="+1",command=augmenter)
bouton2=Button(fenetre,text="-1",command=reduire)
n=0
texte=StringVar() # Important pour mettre à jour les textes
texte.set(morceau[0])
nombre=Label(fenetre,width=25,textvariable=texte)
bouton1.grid(row=0,column=1)
bouton2.grid(row=2,column=1)
nombre.grid(row=1,column=0)





fenetre.mainloop()