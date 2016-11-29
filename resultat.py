#-*- coding: utf-8 -*-
from joueur import *

class Resultat : 
	def __init__(self,joueur,x,y): 	# creer_resultat : Joueur x Int * Int -> Resultat
									# Creation d'un type resultat qui prend en paramètre le joueur adverse ainsi que les coordonnées du tir du joueur actif.
		return
		

	def joueur(self): # joueur : Resultat -> Joueur
					  # Renvoie le joueur a qui appartient le resultat.
		return

					  #Propiétés du type 
					  #L1 : Le joueur est forcement inactif au moment de l'appel de resultat. 

	


	def resultat_tir(self, tir): # resultat_tir : Resultat -> string 
		
		return						# Renvoie une chaine de caractère pouvant correspondre a (la chaine sera ensuite affiché dans le main, l'affichage ne se fait pas ici !) :
								 	# - Si le tir correspond extactement a l'une des positions d'un des bateaux du joueur adverse (verifier pour chaque bateau dans leur ensemble de position -> fonction dans la classe bateau) ALORS	
								 			#Si la position n'a pas deja été touché
								 				#	>>> RENVOIE "Touché"" <<<
								 				# Si apres toute les positions du bateaux on été touché ALORS
								 					# >>> RENVOIE "coulé "<<<

								 			# - Sinon 
								 				# >>> RENVOIE "a l'eau "<<<


								 	# - Sinon Si le tir a touché l'une des deux coordonnées d'une position d'un bateau du joueur adverse ALORS
								 			# >>> RENVOIE "En Vue" <<<
								 	# - Sinon 
							 			# >>> RENVOIE "a l'eau" <<<

								 	


#Test unitaire

ensp= Enspositions(1)
p=Position(1,2)
p2=Position(5,6)
ensp.ajouterPosition(p)
ensp.ajouterPosition(p2)
bat = Bateau(2,ensp)
eb = Ensbateaux(2)
eb.ajouterBateau(bat)
j = Joueur(eb,False)
print j.etat() # Doit renvoyer False
j.modif_etat()
print j.etat() # Doit renvoyer True

		



				
