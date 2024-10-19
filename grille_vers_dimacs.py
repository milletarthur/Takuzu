import sys
import fonctions_takuzu


if len(sys.argv) < 2:
    print("Format : python3 grille_vers_dimacs.py <fichier_entree> (<fichier_sortie>)")

else:
    if len(sys.argv) == 2:
        filename_out = "dimacs_out.txt"
    else:
        filename_out = sys.argv[2]
    
    filename_in = sys.argv[1]

    # On lit le fichier donné en argument et on le convertit en liste de clauses
    (Liste_P_ij, n) = fonctions_takuzu.convertir_fichier_en_clauses(filename_in)

    # On ajoute la traduction en fnc de toutes les règles pour une grille de taille n
    Liste_P_ij += fonctions_takuzu.regle_autant_0_1_ligne(n)
    Liste_P_ij += fonctions_takuzu.regle_autant_0_1_colonne(n)
    Liste_P_ij += fonctions_takuzu.pas_2_chiffres_identiques_ligne(n)
    Liste_P_ij += fonctions_takuzu.pas_2_chiffres_identiques_colonne(n)
    Liste_P_ij += fonctions_takuzu.lignes_diff_principal(n)
    Liste_P_ij += fonctions_takuzu.colonnes_diff_principal(n)

    # On écrit le fichier DIMACS correspondant
    t = len(Liste_P_ij)
    print("Ecriture du fichier", filename_out)
    fonctions_takuzu.ensemble_clauses_vers_DIMACS(Liste_P_ij, n, filename_out)
