from random import randint
from time import sleep

class Partie():
    def __init__(self,nbClrs: int, taille : int):
        """Crée une Partie Flood it. Elle est matérialisé par 
        Une matrice carrée de taille *taille* composé de nombres
        allant de 0 à *nbClrs-1* (Qui pourra être utilisé pour une
        version daltonienne du jeu) """
        assert nbClrs > 2 and taille > 5
        self.matrice = [[randint(0,nbClrs-1) for i in range(taille)] for j in range(taille)]
        self.taille = taille
        self.nbClrs = nbClrs
        self.expansion = self.expandre( 0, 0,[(0,0)])

    def victoire(self):
        return self.matrice.count(self.matrice[0])==self.taille and self.matrice[0].count(self.matrice[0][0])

    def expandre(self, i : int, j : int, expansion_partielle : list):
        if i>0:
            u,v=self.case_a_gauche(i,j)
            #print("(",u,",",v,")")
            if (u,v) not in expansion_partielle and self.matrice[i][j]==self.matrice[u][v]:
                expansion_partielle.append((u,v))
                self.expandre(u,v,expansion_partielle)
        if i<self.taille-1:
            u,v=self.case_a_droite(i,j)
            #print("(",u,",",v,")")
            if (u,v) not in expansion_partielle and self.matrice[i][j]==self.matrice[u][v]:
                expansion_partielle.append((u,v))
                self.expandre(u,v,expansion_partielle)
        if j>0:
            u,v=self.case_en_haut(i,j)
            #print("(",u,",",v,")")
            if (u,v) not in expansion_partielle and self.matrice[i][j]==self.matrice[u][v]:
                expansion_partielle.append((u,v))
                self.expandre(u,v,expansion_partielle)
        if j<self.taille-1:
            u,v=self.case_en_bas(i,j)
            #print("(",u,",",v,")")
            if (u,v) not in expansion_partielle and self.matrice[i][j]==self.matrice[u][v]:
                expansion_partielle.append((u,v))
                self.expandre(u,v,expansion_partielle)
        #print(expansion_partielle)
        return expansion_partielle
        


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
        self.expansion=self.expandre(0,0,[(0,0)])
        print(self.expansion)
    
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