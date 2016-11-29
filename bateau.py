#-*- coding: utf-8 -*-
from enspositions import *

class Bateau:

	#fonction de creation 
	def __init__(self,Enspositions): # creer_bateau : int x Enspositions -> Bateau 
											# Creation d'un bateau qui prend en paramètre la taille du bateau et l'ensemble de ses positions sur la grille.
		return								# la taille du bateau est comprise entre 1 et 4 
											# nb_Pos_toucher(creer_bateau(n : int, b: Bateau)) = 0
											# est-detruit(creer_bateau(n:int,b:Bateau)) = FALSE
											# taillebat(creer_bateau(ep)) = ep.tailleEP()
		
	def positions(self): 	# position: Bateau -> Ensposition
		return				# Renvoie la liste des positions du bateau passé en paramètre si le bateau existe, ERREUR sinon.
							# La taille de la liste des positions renvoyées est égal a la taille du bateau

	def taillebat(self): 	#taillebat : Bateau -> int
		return				# Renvoie la taille du bateau entré en paramètre. ERREUR si le bateau n'existe pas.
					 		# 0 < taille(b:bateau) <= 4
					 		# taille(b : Bateau) <= 4 et taille(b : Bateau) >0
		
	def est_detruit(self):	# est_detruit: Bateau -> bool
		return				# Renvoie TRUE si le bateau passé en paramètre est coulé ce qui implique que toutes ses positions ont été touchées ( utiliser fonction positions) ,renvoie FALSE sinon. 
							
		
	def nB_Pos_toucher(self): 	# nB_Pos_toucher: Bateau -> int
		return					# Renvoie le nombre de positions qui ont été touchées du bateau passé en paramètre. Lorsque le nombre de position touchées est égale a la taille du bateau. la fonction est_Detruit passe a TRUE.
								

	def position_appartient(self,Position): # position_appartient: Bateau x Position -> bool
		return								# Renvoie TRUE si la position est dans l'Ensemble de positions du bateau. FALSE sinon. ERREUR si le bateau n'existe pas.
											# Peut servir a savoir si une position est déja occupée au sein du meme bateau
		

	def est_toucher(self, coordonneeX,coordonneeY): # est_toucher: Bateau x Int x Int ->bool	
		return						 				# Renvoie TRUE si la position entré en paramètre correspond à une des positions présente dans l'ensemble des positions du bateau. FALSE sinon, ERREUR si la position est non valide.
									 				# est_touche(b: Bateau, p : Position) => est_detruit(b : Bateau) == FALSE

	def est_envue(self, coordonneeX,coordonneeY):  # est_envue: Bateau x Int x Int -> bool
		return				   					   # Renvoie TRUE si dans la position entré en paramètre, l'une des deux coordonnées correspond a une coordonnées presente dans l'ensemble des positions du bateau. False sinon. ERREUR si le bateau n'existe pas
						   						   # est_envue(b: Bateau, a : Int, b: Int)==TRUE => est_detruit(b : Bateau) == FALSE

	def bat_bien_former(self): 		# bat_bien_former: Bateau -> bool
		return						# Explication : Les coordonnées des bateaux sont entrées par l'utilisateur une par une. Donc pour eviter qu'il y ai dislocation de bateau (qu'un joueur place une position en (1,1) et ensuite en (6,6)) on appel cette fonction
									# Un bateau est bien formé si il y'a un ecart de 1 très exactement entre 2 coordonnées selon la direction que l'utilisateur voudras donner a son bateau 
									# Par exemple si on a un bateau de taille 2, si la 1ere position du bateau est (1,1) la 2e sera soit (1,2) soit (2,1)
	

		


# >> TEST UNITAIRE <<

ensp = Enspositions(1)
	
p = Position(1,2)
tir = Position(5,6)
tir2 = Position(1,4)
tir3 = Position(1,2)
ensp.ajouterPosition(p)
bat = Bateau(ensp)
print bat.taillebat()==1 # Doit renvoyer True 
print bat.est_detruit() # Doit renvoyer False
print bat.nB_Pos_toucher()==0 # Doit renvoyer True 
print bat.position_appartient(p) # Doit renvoyer True
print bat.est_toucher(tir) # Doit renvoyer False
print bat.est_envue(tir2) # Doit renvoyer True 
print bat.est_toucher(tir3) # Doit renvoyer True
