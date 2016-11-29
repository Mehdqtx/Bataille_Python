from position import *

class Enspositions :
	def __init__(self,tailleEP): # creer_ensposition : int -> Ensposition
						# Constructeur du type Ensposition. Permet d'avoir l'ensemble de positions d'un bateau.
						# nb_position_pres(creer_Ensposition()) = 0
		
	def positions(self):# positions : Ensposition -> tableau de positions.
						# C'est l'ensembles des positions present dans le type posiiton. Il est vide lorsqu'on crée un Enspositon 
						# position(creer_Ensposition()) -> vide

	def tailleEP(self): # tailleEP : Ensposition -> int
						# C'est la taille de l'ensemble de positions. Donc le nombre de position max

	def ajouterPosition(self,Position):# ajouterPosition : Ensposition * Position -> Ensposition 
									   # Renvoie l'ensemble de position d'un bateau avec la positionn passée en parametre rajoutée a cet ensemble
									   # ajouterPosition(Ensp , position) ->  0 < nb_position_pres(Ensp) < tailleEP(Ensp)
		

	def est_present_posit(self,Position): # est_present_posit : Ensposition * Position -> bool
										  # permet de vérifier qu'une position appartient a l'ensemble de positions passé en parametre
										  # est_present_posit(creer_Ensposition(),Position) = False


	def nb_position_pres(self): # nb_position_pres : Ensposition -> int 
								# Renvoi le nombre de positions non touchées de l'ensemble de position
								# nb_position_pres(Ensp) = 0 --> toutes les position touchées ou aucune position dans l'ensemble de positions
								# ajouter

	def modif_nb_position_pres(self): # modif_nb_position_pres : Ensposition -> Ensposition
								 	  # Modifie le nombre de positions presente dans l'ensemble de positions passé en paramètre.




						
	

#test unitaire

Ens = Ensposition(2)
p = Position(1,2)
pos1 = Position(2,3)
Ens.ajouterPosition(p)
Ens.ajouterPosition(pos1)
print Ens.est_present_posit(p)
print Ens.est_present_posit(pos1)
print Ens.nb_position_pres()
print Ens.tailleEP()