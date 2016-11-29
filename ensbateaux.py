#-*- coding: utf-8 -*-
from bateau import *

class Ensbateaux :


	def __init__(self,tailleEB): # creer_Ensbateaux : int  -> Ensbateau
		return					 # renvoie un ensemble de bateaux vide avec comme taille l'entier passé en parametre
								 # le nombre de bateaux present a la creation est de 0 et le nombre de bateaux vivant est egalement 0 
		

	def tailleEB(self) : # taille : Ensbateaux -> int
		return			 #Renvoi la taille de l'ensemble de bateaux passé en paramètre
					     # tailleEB(creer_Ensbateau(n)) = n

	def bateaux(self): # bateau : Ensbateaux -> [Bateau]
		return		   # Renvoie l'ensemble de bateaux contenue dans le tye Ensbateaux passé en paramètre


	def ajouterBateau(self,bateau): # ajouterBateau : Ensbateaux * Bateau ->
		return					    # Ajoute le bateau passé en parametre à la liste des bateau et renvoi l'ensbateaux modifié
									# ajouterBateau(bat) -> 0 < nb_bat_safe() < tailleEB

	def safe_bateau(self,bateau): # safe_bateaux : Ensbateaux * Bateau -> bool 
		return			  		  # Renvoi TRUE si le bateau présent dans l'ensemble de bateaux n'est pas détruit, FALSE si le bateau n'est pas détruit ou n'appartient pas a l'ensemble
					  			  # safe_bateau(bat) == TRUE --> nb_bat_safe() > 0 
					  			  # safe_bateau(bat) == FALSE --> On ne verifie plus ses position lors d'un tir

	def est_present_pos(self,position): # est_present_pos : Ensbateaux * Position -> bool
		return							# Renvoi TRUE si la position passee en paramètre appartient a un bateau de l'ensemble de bateaux. FALSE sinon. Sera utile pour le tir et pour verifier si une position n'est pas déja utilisée par un bateau
										# est_present_pos(pos) == TRUE -> pos n'appartient pas a un bateau detruit


	def nb_bat_safe(self): # nb_bat_safe : Ensbateaux -> int
		return			   # Renvoi le nombre de bateaux de l'ensemble de bateaux qui ne sont pas encore détruit. Utile pour savoir si un joueur n'as plus de bateaux valides. Sert egalement lors de l'ajout des bateaux a la flotte
						   # nb_bat_safe(creer_Ensbat()) = 0

	def modif_nb_bat_safe(self): # modif_nb_bat_safe : Ensbateaux -> Ensbateaux
		return				     # Modifie le nombre de bateaux vivant dans l'ensemble de bateaux passé en paramètre 

#Test unitaires


ensp= Enspositions(1)
p=Position(1,2)
p2=Position(5,6)
ensp.ajouterPosition(p)
ensp.ajouterPosition(p2)
bat = Bateau(2,ensp)
eb = Ensbateaux(2)
eb.ajouterBateau(bat)
print eb.tailleEB()==2 # Doit renvoyer True
print eb.safe_bateau(bat) # Doit renvoyer True
print eb.est_present_pos(p) # Doit renvoyer True
print eb.nb_bat_safe()  == 1 # Doit renvoyer True
	

	
	
	
	
	

				
