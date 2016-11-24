from position import *

class Enspositions :
	def __init__(self): # Constructeur du type Ensposition. Permet d'avoir l'ensemble de positions d'un bateau.
		
	def positions(self):# positions : Ensposition -> Tableau de position.
						# C'est l'ensembles des positions present dans le type posiiton. Il est vide lorsqu'on crée un Enspositon 
		
	def ajouterPosition(self,Position):# ajouterPosition : Ensposition * Position -> Ensposition 
									   # Renvoie l'ensemble de position d'un bateau avec la positionn passée en parametre rajoutée a cet ensemble
		
	def delPosition(self,Position):# delPosition : Ensposition * Position -> Ensposition 
								   # Renvoie l'ensemble de position d'un bateau avec la positionn passée en parametre supprimée de cet ensemble
		

	def est_present_posit(self,Position): # est_present_posit : Ensposition * Position -> bool
										  # permet de vérifier qu'une position appartient a l'ensemble de positions passé en parametre



	# Propriété
	# position(creer_Ensposition()) -> vide
	# est_present_posit(creer_Ensposition(),Position) = False


#test unitaire

Ens = Ensposition()
p = Position(1,2)
pos1 = Position(2,3)
print Ens.ajouterPosition(p)
Ens.ajouterPosition(pos1)
Ens.delPosition(pos1)
print Ens.est_present_posit(p)