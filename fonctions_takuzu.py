import math

# P.value = true ssi la case de coordonnées (i,j) vaut 1
class P():
    def __init__(self, value, i, j):
        self.value = value
        self.i = i
        self.j = j


# Concatène L1 à tous les éléments de L2 (il faut que L2 soit une liste de listes)
def map_concat_elem(L1, L2):
    n = len(L2)
    for i in range(n):
        L2[i].append(L1[0])
    return L2


# Renvoie la liste de toutes les listes de taille L contenant H fois 1 et L-H fois 0
def enum_h_parmi_l_bits(H, L):
    if L == 0:
        return [[]]
    else:
        if H == 0:
            L2 = map_concat_elem([0], enum_h_parmi_l_bits(H, L-1))

            return L2
        elif H == L:
            L1 = map_concat_elem([1], enum_h_parmi_l_bits(H-1, L-1))
            return L1
        else:
            L1 = map_concat_elem([1], enum_h_parmi_l_bits(H-1, L-1))
            L2 = map_concat_elem([0], enum_h_parmi_l_bits(H, L-1))
            return L1 + L2


# Renvoie la liste de P(i,j) correspondant à la règle "Autant de 0 que de 1 sur une même ligne" pour une grille de taille n
def regle_autant_0_1_ligne(n):
    # On créé la liste de toutes les configurations possibles de k bits valant 1 dans une liste de taille n,
    # excepté pour n/2 bits
    Liste_Binaire_Configs = []
    for k in range(n + 1):
        if (k != n/2):
            Liste_Binaire_Configs = Liste_Binaire_Configs + enum_h_parmi_l_bits(k, n)
    # On écrit la règle pour chaque ligne i
    # On fait donc la négation de chaque configuration précédente
    Liste_P_ij = []
    nb_clauses = 0
    for i in range(n):
        for L in Liste_Binaire_Configs:
            Liste_P_ij.append([])
            for j in range(n):
                if L[j] == 1:
                    Liste_P_ij[nb_clauses].append(P(False, i, j))
                else:
                    Liste_P_ij[nb_clauses].append(P(True, i, j))
            nb_clauses += 1

    return Liste_P_ij


# Renvoie la liste de P(i,j) correspondant à la règle "Autant de 0 que de 1 sur une même colonne" pour une grille de taille n
def regle_autant_0_1_colonne(n):
    # On créé la liste de toutes les configurations possibles de k bits valant 1 dans une liste de taille n,
    # excepté pour n/2 bits
    Liste_Binaire_Configs = []
    for k in range(n + 1):
        if (k != n/2):
            Liste_Binaire_Configs = Liste_Binaire_Configs + enum_h_parmi_l_bits(k, n)
    # On écrit la règle pour chaque colonne j
    # On fait donc la négation de chaque configuration précédente
    Liste_P_ij = []
    nb_clauses = 0
    for j in range(n):
        for L in Liste_Binaire_Configs:
            Liste_P_ij.append([])
            for i in range(n):
                if L[i] == 1:
                    Liste_P_ij[nb_clauses].append(P(False, i, j))
                else:
                    Liste_P_ij[nb_clauses].append(P(True, i, j))
            nb_clauses += 1

    return Liste_P_ij


# Traduit la règle "Pas plus de 2 chiffres identiques côte à côte sur une même colonne"
def pas_2_chiffres_identiques_colonne(n):
    Liste_P_ij = []
    for i in range(1, n-2, 1):
        for j in range(0, n, 1):
            clause_1 = [P(False, i-1, j), P(False, i, j), P(False, i+1, j)]
            clause_2 = [P(True, i-1, j), P(True, i, j), P(True, i+1, j)]
            clause_3 = [P(False, i, j), P(False, i+1, j), P(False, i+2, j)]
            clause_4 = [P(True, i, j), P(True, i+1, j), P(True, i+2, j)]
            Liste_P_ij.append(clause_1)
            Liste_P_ij.append(clause_2)
            Liste_P_ij.append(clause_3)
            Liste_P_ij.append(clause_4)
    return Liste_P_ij


# Traduit le règle "Pas plus de 2 chiffres identiques côte à côte sur une même ligne"
def pas_2_chiffres_identiques_ligne(n):
    Liste_P_ij = []
    for i in range(0, n, 1):
        for j in range(1, n-2, 1):
            clause_1 = [P(False, i, j-1), P(False, i, j), P(False, i, j+1)]
            clause_2 = [P(True, i, j-1), P(True, i, j), P(True, i, j+1)]
            clause_3 = [P(False, i, j), P(False, i, j+1), P(False, i, j+2)]
            clause_4 = [P(True, i, j), P(True, i, j+1), P(True, i, j+2)]
            Liste_P_ij.append(clause_1)
            Liste_P_ij.append(clause_2)
            Liste_P_ij.append(clause_3)
            Liste_P_ij.append(clause_4)
    return Liste_P_ij

# Fonction qui vérifie la règle "Toutes les colonnes sont différentes" pour une taille de colonne n
def colonnes_diff_principal(n):
    Liste_ij = []
    for j1 in range(0, n-1):
        for j2 in range(j1+1,n):
            Liste_ij += lignes_diff(j1,j2,n)
    return Liste_ij

# Fonction d'initialisation de la récursivité pour construire la règle
# Elle vérifie que la colonne n'est pas trop courte pour une comparaison :
#  - si oui elle renvoie une liste vide
#  - sinon elle initialise u(2) et fait appelle à la fonction récursive
def colonnes_diff(j1,j2,n):
    if n < 2:
        print("Erreur : longueur de ligne trop courte")
        return[]
    Liste_ij = [[P(True,0,j1), P(True,0,j2)],[P(False,0,j1), P(False,0,j2)]]
    if n == 2:
        return Liste_ij
    return lignes_diff_rec(Liste_ij,j1,j2,2,n)
    
# Fonction récursive
# Elle renvoie u(n+1) = (u(n) v -P(k,j1) v -P(k,j2)) ^ (u(n) v P(k,j1) v P(k,j2))
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

# Fonction qui vérifie la règle "Toutes les colonnes sont différentes" pour une taille de colonne n
def lignes_diff_principal(n):
    Liste_ij = []
    for i1 in range(0, n-1):
        for i2 in range(i1+1,n):
            Liste_ij += lignes_diff(i1,i2,n)
    return Liste_ij

# Fonction d'initialisation de la récursivité pour construire la règle
# Elle vérifie que la colonne n'est pas trop courte pour une comparaison :
#  - si oui elle renvoie une liste vide
#  - sinon elle initialise u(2) et fait appelle à la fonction récursive
def lignes_diff(i1,i2,n):
    if n < 2:
        print("Erreur : longueur de ligne trop courte")
        return[]
    Liste_ij = [[P(True,i1,0), P(True,i2,0)],[P(False,i1,0), P(False,i2,0)]]
    if n == 2:
        return Liste_ij
    return lignes_diff_rec(Liste_ij,i1,i2,2,n)
    
# Fonction récursive
# Elle renvoie u(n+1) = (u(n) v -P(i1,k) v -P(i2,k)) ^ (u(n) v P(i1,k) v P(i2,k))
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

# Convertit le fichier filename en liste de [P(i,j)] (/!\ Les P(i,j) sont tous dans une liste de taille 1)
# Exemple de format de fichier :
# 1..0
# 0.1.
# ....
# 11..
def convertir_fichier_en_clauses(filename):
    Liste_P_ij = []
    i = 0
    f = open(filename, "r")
    for ligne in f:
        j = 0
        # ligne.strip retire les espaces/tab et les '\n' de chaque ligne
        for c in ligne.strip():
            if c == '0':
                Liste_P_ij.append([P(False, i, j)])
            elif c == '1':
                Liste_P_ij.append([P(True, i, j)])
            j += 1
        i += 1
    if i != j:
        print("Erreur lors de la lecture du fichier ", filename, " : Nombre de lignes et de colonnes différent.")
    f.close
    return Liste_P_ij, i


# Convertit ListeClauses (ensemble d'ensembles de P_ij) vers le format DIMACS dans le fichier nommé filename
def ensemble_clauses_vers_DIMACS(ListeClauses, taille_grille, filename):
    f = open(filename, "w")
    nb_clauses = len(ListeClauses)
    # On écrit l'en-tête du fichier avec le nombre de variables et le nombre de clauses
    f.write("p cnf " + str(taille_grille**2) + " " + str(nb_clauses) + "\n")

    # On écrit ensuite chaque clause sous le format DIMACS
    # Une variable P(i,j) sera traduite par l'entier (taille_grille * i) + j
    for clause in ListeClauses:
        # On écrit une clause par ligne
        Ligne = ""
        for P in clause:
            # print(str(P.i) + " " + str(P.j))
            n = (taille_grille * P.i) + P.j + 1
            if P.value is False:
                n = -n
            Ligne = Ligne + str(n) + " "
        f.write(Ligne + "0\n")
    f.close()


# Convertit le fichier DIMACS résolu en grille sous le format d'entrée
def solution_dimacs_vers_fichier(input_file, output_file):
    f_in = open(input_file, "r")
    line = f_in.readline()
    if line.strip() != "SAT":
        print("Erreur : instance insatisfaisable")
        print(line.strip())
    else:
        # On récupère toutes les variables contenues dans le fichier d'affilée, en excluant les zéros (fin de ligne)
        Liste_termes = []
        for line in f_in:
            for terme in line.split():
                if (terme.strip().lstrip('-')).isnumeric():
                    x = int(terme.strip())
                    if (x != 0):
                        Liste_termes.append(x)

        k = 1
        f_out = open(output_file, "w")
        taille_grille = math.sqrt(len(Liste_termes))
        for x in Liste_termes:
            if x > 0:
                f_out.write("1")
            else:
                f_out.write("0")
            if k == taille_grille:
                f_out.write("\n")
                k = 0
            k += 1
        f_out.close()
    f_in.close()
