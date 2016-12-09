#-*- coding: utf-8 -*-

#Type Flotte

import TypeBateau

class Flotte:
	def __init__(self,bateau1,bateau2,bateau3,bateau4,bateau5):
		self.bateau1= bateau1
		self.bateau2= bateau2
		self.bateau3= bateau3
		self.bateau4= bateau4
		self.bateau5= bateau5
		self.bateaux_restants = 5

	#Creer une flotte de 5 bateaux
	# -> Flotte


	def Coule(self,numbateau,grille):
		coule= True
		ligne = 0
		while ligne < 21 and coule == True : 
			colonne = 0
			while colonne < 21 and coule == True : 
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




	def Bateau_Flotte(self,numbateau):

		if self.bateau1.NumeroBateau() == numbateau :
			return bateau1

		if self.bateau2.NumeroBateau() == numbateau :
			return bateau2

		if self.bateau3.NumeroBateau() == numbateau :
			return bateau3

		if self.bateau4.NumeroBateau() == numbateau :
			return bateau4

		if self.bateau5.NumeroBateau() == numbateau :
			return bateau5
	#Renvoie le bateau dont le numéro est donné en paramètre, Retourne une erreur si le bateau n'existe pas
	#Flotte x Int -> Bateau

	"""Proprietes:
	(1) Coule (f,1) == True => BateauxRestants(f) = BateauxRestants(f) - 1"""