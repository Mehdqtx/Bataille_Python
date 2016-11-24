from bateau import *

class Ensbateaux :


	def __init__(self): #creer_Ensbateau : int  -> Ensbateau
						#renvoie un ensemble de bateaux vide avec comme taille l'entier passé en parametre
		

	def taille(self) : # taille : Ensbateaux -> int
					   #Renvoi la taille de l'ensemble de bateaux passé en paramètre

	def bateaux(self): # bateau : Ensbateau -> [Bateau]
					   # Renvoie l'ensemble de bateaux contenue dans le tye Ensbateaux passé en paramètre

	def ajouterBateau(self,bateau): # ajouterBateau : Ensbateaux * Bateau ->
									# Ajoute le bateau passé en parametre à la liste des bateau et renvoi l'ensbateaux modifié

	def safe_bateaux(self,bateau): # safe_bateaux : Ensbateaux * Bateau -> bool 
					  			   # Renvoi TRUE si le bateau présent dans l'ensemble de bateaux n'est pas détruit, FALSE si le bateau n'est pas détruit ou n'appartient pas a l'ensemble

	def est_present_pos(self,position): # est_present_pos : Ensbateaux * Position -> bool
										# Renvoi TRUE si la position passee en paramètre appartient a un bateau de l'ensemble de bateaux. FALSE sinon. Sera utile pour le tir

	def est_present_bat(self,bateau): # est_present_bat : Ensbateaux * Bateau -> bool
									  # Renvoi TRUE si le bateau passé en paramètre appartient l'ensemble de bateaux. FALSE sinon. Sera utile pour le plaçage des bateaux, pour éviter qu'ils se supperpose

	def nb_bat_safe(self): # nb_bat_safe : Ensbateaux -> int
						   # Renvoi le nombre de bateaux de l'ensemble de bateaux qui sont détruit.
	#Propriétés



				
