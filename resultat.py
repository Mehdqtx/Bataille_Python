#-*- coding: utf-8 -*-
from joueur import *

class Resultat : 
	def __init__(self,joueur,x,y): 	# creer_resultat : Joueur x Int * Int -> Resultat
									# Creation d'un resultat qui prend en paramètre le joueur adverse ainsi que les coordonnées du tir du joueur actif.
		return
		

	def joueur(self): # joueur : Resultat -> Joueur
					  # Renvoie le joueur adverse sur lequel on veut travailler.
		return

					  # Propiétés du type 
					  # Le joueur visé est forcement inactif au moment de l'appel de resultat. 
					  # joueur(creer_resultat(j,x,y)) = j 

	

	def absice_tir(self): # absice_tir : Resultat -> Int
		return			  # Renvoi l'absice x du tir.
						  # absice_tir(creer_resultat(j,x,y)) = x

	def ordonnee_tir(self): # ordonnee_tir : Resultat -> Int
		return				    # Renvoi l'ordonnee x du tir.
						    # ordonnee_tir(creer_resultat(j,x,y)) = y

	def resultat_tir(self): # resultat_tir : Resultat -> String 
		
		return					 # Renvoie une chaine de caractère pouvant correspondre a :
								 # - Si les coordonnees de tir sont a l'interieur de la grille
								 	# - Si le tir correspond extactement a l'une des positions d'un des bateaux du joueur adverse (verifier pour chaque bateau dans leur ensemble de position -> fonction dans la classe bateau) ALORS	
								 		# Si la position n'a pas deja été touché
								 			#	>>> RENVOIE "Touché"" <<<
								 			# Si apres toute les positions du bateaux on été touché ALORS
								 				# >>> RENVOIE "coulé "<<<

								 		# - Sinon 
								 			# >>> RENVOIE "a l'eau "<<<


									# - Sinon Si le tir a touché l'une des deux coordonnées d'une position d'un bateau du joueur adverse ALORS
								 			# >>> RENVOIE "En Vue" <<<
								 	# - Sinon 
							 				# >>> RENVOIE "a l'eau" <<<
							 	# - Sinon
							 			# >>> RENVOIE "a l'eau" <<<

								# PS: La chaine sera ensuite affiché dans le main, l'affichage ne se fait pas ici !


#Test unitaire

ensp = Enspositions(1)
p = Position(1,2)
p2 = Position(5,6)
ensp.ajouterPosition(p)
ensp.ajouterPosition(p2)
bat = Bateau(ensp)
eb = Ensbateaux(2)
eb.ajouterBateau(bat)
j = Joueur(eb,False)
res = Resultat(j,5,8)
res2 = Resultat(j,1,4)
res3 = Resultat(j,1,2)
#print res.joueur().etat() # Doit renvoyer False car on travaille sur le joueur inactif
print res.resultat_tir() # Doit renvoyer a l'eau
print res.resultat_tir() # Doit renvoyer En vue
print res.resultat_tir() # Doit renvoyer Touché coulé






		



				
