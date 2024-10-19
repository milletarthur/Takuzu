# P.value = true ssi la case de coordonnées (i,j) vaut 1
class P():
    def __init__(self, value, i, j):
        self.value = value
        self.i = i
        self.j = j

def lignes_diff_principal(n):
    Liste_ij = []
    for i1 in range(0, n-1):
        for i2 in range(i1+1,n):
            Liste_ij += lignes_diff(i1,i2,n)
    return Liste_ij

def lignes_diff(i1,i2,n):
    if n < 2:
        print("Erreur : longueur de ligne trop courte")
        return[]
    Liste_ij = [[P(True,i1,0), P(True,i2,0)],[P(False,i1,0), P(False,i2,0)]]
    if n == 2:
        return Liste_ij
    return lignes_diff_rec(Liste_ij,i1,i2,2,n)
    
def lignes_diff_rec(Liste_ij,i1,i2,j,n):
    Liste1 = []
    Liste2 = []
    for k in range(0, len(Liste_ij)):
        Liste1.append(Liste_ij[k] + [P(True,i1,j), P(True,i2,j)])
        Liste2.append(Liste_ij[k] + [P(False,i1,j), P(False,i2,j)])
    Liste_ij = Liste1 + Liste2
    if j == n-1:
        return Liste_ij
    return lignes_diff_rec(Liste_ij,i1,i2,j+1,n)
    



def colonnes_diff_principal(n):
    Liste_ij = []
    for j1 in range(0, n-1):
        for j2 in range(j1+1,n):
            Liste_ij += lignes_diff(j1,j2,n)
    return Liste_ij

def colonnes_diff(j1,j2,n):
    if n < 2:
        print("Erreur : longueur de ligne trop courte")
        return[]
    Liste_ij = [[P(True,0,j1), P(True,0,j2)],[P(False,0,j1), P(False,0,j2)]]
    if n == 2:
        return Liste_ij
    return lignes_diff_rec(Liste_ij,j1,j2,2,n)
    
def colonnes_diff_rec(Liste_ij,j1,j2,i,n):
    Liste1 = []
    Liste2 = []
    for k in range(0, len(Liste_ij)):
        Liste1.append(Liste_ij[k] + [P(True,i,j1), P(True,i,j2)])
        Liste2.append(Liste_ij[k] + [P(False,i,j1), P(False,i,j2)])
    Liste_ij = Liste1 + Liste2
    if i == n-1:
        return Liste_ij
    return lignes_diff_rec(Liste_ij,j1,j2,i+1,n)
    
n=6
L = colonnes_diff_principal(n)
print("nb clause = ", len(L))
print("taille clause = ",len(L[1]))
