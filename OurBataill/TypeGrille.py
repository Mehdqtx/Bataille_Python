#-*- coding: utf-8 -*-

#Type Grille

import TypeBateau

class Grille:
	def __init__(self,hauteur,largeur):
	#Creer une grille avec un nombre de ligne et de colonne donnes
	#pre : hauteur et largeur > 0
	# -> Grille

		self.hauteur = hauteur
		self.largeur = largeur
		self.grille = [[0] * largeur for _ in range(hauteur)]

	def ValeurCoord(self,colonne,ligne):
	#Renvoie la valeur de la coordonnee
	#pre : colonne et ligne >0
	#Grille x Int x Int -> Int
		val = self.grille[ligne][colonne]
		return val

	def Touche(self,colonne,ligne):
	#Renvoie True si position donnee est occupee par un bateau et modifie la valeur de la position à 0
	#pre : colonne et ligne >0
	#Grille x Int x Int -> Bool
		pos = self.grille[ligne][colonne]

		if pos != 0:
			self.grille[ligne][colonne] = 0
			return True
		else :
			return False

	def EnVue(self,colonne,ligne):
	#Renvoie True si un bateau est en vue
	#pre : colonne et ligne >0
	#Grille x Int x Int -> Bool
		envue = False
		for i in range(0,21) :
			if self.grille[i][colonne] != 0 or self.grille[ligne][i] !=0 :
				envue= True

		return envue

	def ModifVal(self,val,colonne,ligne):
	#Modifie la valeur aux coordonnees donne par la valeur donnee
	#pre : colonne et ligne >0
	#Grille x Int x Int x Int -> Grille 

		self.grille[ligne][colonne] = val
		return self

	def Verification(self, bateau):
	#Renvoie True si le bateau peut etre positionne
	#Grille x Bateau -> Bool

		posX = bateau.ligne
		posY = bateau.colonne
		direction = bateau.direction
		tailleB = bateau.taille
		i=0
	 	verif = False
		if direction == 0 :
			while i< tailleB :
				if self.grille[posX][posY+ i] != 0:
					verif= False
				else:
					verif = True	
				i+=1

		elif direction == 1 :
				while i< tailleB :
					if self.grille[posX+ i][posY] != 0:
						verif= False
					else :
						verif = True
					i+=1
		return verif

	def PositionnerBateau(self, bateau):
	#Place un bateau donne dans une grille donnee
	#Grille x Bateau -> Grille

		posX = bateau.ligne
		posY = bateau.colonne
		tailleB = bateau.taille
		numBateau = bateau.num
	 	i=0

	 	if self.Verification(bateau) :
	 		while i< tailleB :
	 			self.ModifVal(numBateau,posY,posX)
	 			i+=1  

	 	return self

	"""Propriétés:
	(1) : Positionnerbateau(b,g)  => Vérification(b,g) == True 
    (2) Touche(g,1,2) == True => ModifVal(g,0,1,2) """