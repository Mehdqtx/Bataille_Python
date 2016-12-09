#-*- coding: utf-8 -*-

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
		ligne = 0
		while ligne < len(grille.grille) and coule == True : 
			colonne = 0
			while colonne < len(grille.grille[ligne]) and coule == True :
				if grille.ValeurCoord(colonne,ligne) == numbateau : 
					coule = False
				colonne += 1 
			ligne += 1
	
		if coule == True : 
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