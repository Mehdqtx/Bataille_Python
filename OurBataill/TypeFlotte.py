#Type Flotte

import TypeBateau

class Flotte:
	def __init__(self,bateau1,bateau2,bateau3,bateau4,bateau5):
		self.listeBat = [bateau1,bateau2,bateau3,bateau4,bateau5]
		self.bateaux_restants = len(self.listeBat)

	#Creer une flotte de 5 bateaux
	# -> Flotte


	def Coule(self,numbateau,grille):
		coule = True
		for ligne in range(len(grille)) : 
			for colonne in range(len(grille[ligne])):
				if grille[ligne][colonne] == numbateau : 
					coule = False
				else : 
					coule = True
					self.bateaux_restants = self.BateauxRestants() - 1
		return coule


	#Renvoie True si le bateau de numero donne est coule et modifie le nombre de bateaux restants
	#Flotte x Bateau x Grille -> Bool

	def BateauxRestants(self):

		return self.bateaux_restants

	#Renvoie le nombre de bateaux restants
	#Flotte -> Int

	"""Proprietes:
	(1) Coule (f,1) == True => BateauxRestants(f) = BateauxRestants(f) - 1"""