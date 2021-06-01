from random import randint
from time import sleep

class Partie():
    def __init__(self,nbClrs: int, taille : int):
        """Crée une Partie Flood it. Elle est matérialisé par 
        Une matrice carrée de taille *taille* composé de nombres
        allant de 0 à *nbClrs-1* (Qui pourra être utilisé pour une
        version daltonienne du jeu) """
        assert nbClrs > 2 and taille > 5
        self.quatrecoins=set()
        self.matrice = [[randint(0,nbClrs-1) for i in range(taille)] for j in range(taille)]
        self.taille = taille
        self.nbClrs = nbClrs
        self.expansion = self.expandre([(0,0)])
        self.nbCoups=0
        

    def victoire(self):
        """renvoie True si, et seulement si, toutes les cases sont de la même couleur"""
        return self.matrice.count(self.matrice[0])==self.taille and self.matrice[0].count(self.matrice[0][0])

    def defaite(self):
        """renvoie True si, et seulement si le nombre de coups est excédentaire"""
        return self.nbCoups>=22

    def expandre(self, expansion_partielle : list):
        liste = set([x for x in expansion_partielle])
        liste.difference_update(self.quatrecoins)
        liste=list(liste)
        while liste != [] :
            i,j=liste.pop()
            if i>0:
                u,v=self.case_a_gauche(i,j)
                #print("(",u,",",v,")")
                if (u,v) not in expansion_partielle and self.matrice[i][j]==self.matrice[u][v]:
                    expansion_partielle.append((u,v))
                    liste.append((u,v))
            if i<self.taille-1:
                u,v=self.case_a_droite(i,j)
                #print("(",u,",",v,")")
                if (u,v) not in expansion_partielle and self.matrice[i][j]==self.matrice[u][v]:
                    expansion_partielle.append((u,v))
                    liste.append((u,v))
            if j>0:
                u,v=self.case_en_haut(i,j)
                #print("(",u,",",v,")")
                if (u,v) not in expansion_partielle and self.matrice[i][j]==self.matrice[u][v]:
                    expansion_partielle.append((u,v))
                    liste.append((u,v))
            if j<self.taille-1:
                u,v=self.case_en_bas(i,j)
                #print("(",u,",",v,")")
                if (u,v) not in expansion_partielle and self.matrice[i][j]==self.matrice[u][v]:
                    expansion_partielle.append((u,v))
                    liste.append((u,v))
            #print(expansion_partielle)
        return expansion_partielle
        
    def bords(self):
        liste=[]
        bar=set(self.expansion)
        bar.difference_update(self.quatrecoins)
        for (i,j) in self.expansion :
            drapeau=True
            if i>0:
                u,v=self.case_a_gauche(i,j)
                #print("(",u,",",v,")")
                if (u,v) not in self.expansion :
                    liste.append((u,v))
                    drapeau=False

            if i<self.taille-1:
                u,v=self.case_a_droite(i,j)
                #print("(",u,",",v,")")
                if (u,v) not in self.expansion:
                    liste.append((u,v))
                    drapeau=False

            if j>0:
                u,v=self.case_en_haut(i,j)
                #print("(",u,",",v,")")
                if (u,v) not in self.expansion:
                    liste.append((u,v))
                    drapeau=False

            if j<self.taille-1:
                u,v=self.case_en_bas(i,j)
                #print("(",u,",",v,")")
                if (u,v) not in self.expansion:
                    liste.append((u,v))
                    drapeau=False
            
            if drapeau :
                self.quatrecoins.add((i,j))
        
        return liste

    def case_a_gauche(self, i : int, j : int):
        return i-1,j

    def case_a_droite(self, i : int, j : int):
        return i+1,j

    def case_en_bas(self, i : int, j : int):
        return i,j+1

    def case_en_haut(self, i : int, j : int):
        return i,j-1

    def repandre(self, i : int, j : int):
        n=self.matrice[i][j]
        for u,v in self.expansion :
            self.matrice[u][v]=n
        self.expansion[:]=self.expandre(self.expansion)
        self.nbCoups+=1
        #print(self.expansion)
    
    def plateau(self):
        return self.matrice

    def total(self):
        return self.nbCoups

    def __str__(self):
        return "\n".join(["\t".join([str(y) for y in x]) for x in self.matrice])


if __name__=='main':
    test=Partie(8,10)

    print(test)
    print("-"*50)

    while not test.victoire():
        i,j=randint(0,6),randint(0,6)
        while (i,j) in test.expansion:
            i,j=randint(0,6),randint(0,6)
        test.repandre(i,j)
        print("(",i,",",j,")")
        print(test)
        print("-"*50)
        sleep(1)
