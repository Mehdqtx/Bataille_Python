#Type Joueur

import TypeGrille

import TypeFlotte

class Joueur:
	def __init__(self,flotte,grille):
	#Creer une joueur avec une grille et une flotte associee
	# -> Flotte

	self.flotte = flotte
	self.grille = grille

	def Flottejoueur(self):
	#Renvoie la flotte du joueur donne
	#Joueur -> Flotte
	return self.flotte

	def Grillejoueur(self):
	#Renvoie la grille du joueur donne
	#Joueur -> Grille
	return self.grille