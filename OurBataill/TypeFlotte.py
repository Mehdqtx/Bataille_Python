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
		coule = False
		for ligne in range(0,len(grille.grille)-1) : 
			for colonne in range(0,len(grille.grille[ligne])-1):
				if grille.ValeurCoord(colonne,ligne) == numbateau : 
					coule = False
				else : 
					coule = True
	
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