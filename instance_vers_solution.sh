
if [ $# -lt 1 ]
then
	echo "Utilisation : ./instance_vers_solution.sh <fichier_entree> (<fichier_sortie>)"
else
	python3 grille_vers_dimacs.py $1
	minisat -solve dimacs_out.txt solved.txt
	if [ $# -eq 1 ]
	then
		python3 solution_dimacs_vers_grille.py solved.txt
	else
		python3 solution_dimacs_vers_grille.py solved.txt $2
	fi	
fi
