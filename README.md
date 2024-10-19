# Takuzu

Par GAULMIN    Rémi
    MILLET     Arthur
    TOUREILLE  Grégory

Ce programme a pour but de résoudre des grilles du jeu Takuzu (ou Sudoku binaire)

FORMAT DE FICHIER D'ENTREE :
Une grille carrée de taille paire, contenant que les caractères '.', '0' et '1'.
Les points représentent les cases vides, et les 0 et 1 sont les cases déjà remplies,
de valeur respectivement 0 et 1.
Exemple de grille :

  1.....

  ..0..1

  ....11

  11....

  ....0.

  .1..01


POUR GENERER UN FICHIER DIMACS :
python3 grille_vers_dimacs.py <fichier_entree> <fichier_sortie>
L'argument du fichier de sortie n'est pas obligatoire, par défaut la sortie se fera
dans le fichier "dimacs_out.txt".

POUR GENERER UNE GRILLE RESOLUE A PARTIR DU FICHIER RENVOYE PAR LE SAT SOLVEUR :
python3 solution_dimacs_vers_grille.py <fichier_entree> <fichier_sortie>
Le fichier de sortie est lui aussi optionnel et le résultat sera par défaut écrit
dans le fichier "grille_resolue.txt".

/!\ Ce programme est fait pour convertir un fichier produit par le SAT solveur
Minisat, il n'est pas garanti que le format de sortie d'un autre SAT solveur
fonctionne /!\

POUR GENERER UNE GRILLE RESOLUE A PARTIR D'UNE GRILLE INCOMPLETE :
./instance_vers_solution.sh <fichier_entree> <fichier_sortie>
L'argument fichier_sortie est optionnel et la sortie se fait par défaut dans le
fichier "grille_resolue.txt".

/!\ Ce programme ne fonctionne pas si Minisat n'est pas installé sur votre machine /!\
