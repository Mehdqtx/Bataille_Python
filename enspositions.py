#-*- coding: utf-8 -*-
from position import *

class Enspositions :
	def __init__(self,tailleEP): # creer_ensposition : int -> Ensposition
		return					 # Constructeur du type Ensposition. Permet d'avoir l'ensemble de positions d'un bateau.
								 # nb_position_pres(creer_Ensposition()) = 0
		
	def positions(self):# positions : Ensposition -> tableau de positions.
		return			# C'est l'ensembles des positions present dans le type posiiton. Il est vide lorsqu'on crée un Enspositon 
						# position(creer_Ensposition()) -> vide

	def tailleEP(self): # tailleEP : Ensposition -> int
		return			# C'est la taille de l'ensemble de positions. Donc le nombre de position max

	def ajouterPosition(self,Position): # ajouterPosition : Ensposition * Position -> Ensposition 
		return							# Renvoie l'ensemble de position d'un bateau avec la positionn passée en parametre rajoutée a cet ensemble
									    # ajouterPosition(Ensp , position) ->  0 < nb_position_pres(Ensp) < tailleEP(Ensp)
		

	def est_present_posit(self,Position): # est_present_posit : Ensposition * Position -> bool
		return							  # permet de vérifier qu'une position appartient a l'ensemble de positions passé en parametre
										  # est_present_posit(creer_Ensposition(),Position) = False


	def nb_position_pres(self): # nb_position_pres : Ensposition -> int 
		return				    # Renvoi le nombre de positions non touchées de l'ensemble de position
								# nb_position_pres(Ensp) = 0 --> toutes les position touchées ou aucune position dans l'ensemble de positions
								# ajouter

	def modif_nb_position_pres(self): # modif_nb_position_pres : Ensposition -> Ensposition
		return						  # Modifie le nombre de positions presente dans l'ensemble de positions passé en paramètre.




						
	

#test unitaire

Ens = Enspositions(2)
p = Position(1,2)
pos1 = Position(2,3)
Ens.ajouterPosition(p)
Ens.ajouterPosition(pos1)
print Ens.est_present_posit(p) 
print Ens.est_present_posit(pos1)
print Ens.nb_position_pres() == 2
print Ens.tailleEP() == 2