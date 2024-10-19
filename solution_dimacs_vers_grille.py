import fonctions_takuzu
import sys

if len(sys.argv) < 2:
    print("Utilisation : python", sys.argv[0], "<fichier_entree> (<fichier_sortie>)")

else:
    if (len(sys.argv) == 2):
        filename_out = "grille_resolue.txt"
    else:
        filename_out = sys.argv[2]

    filename_in = sys.argv[1]
    print("Ecriture du fichier", filename_out)
    fonctions_takuzu.solution_dimacs_vers_fichier(filename_in, filename_out)
