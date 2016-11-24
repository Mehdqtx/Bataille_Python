

class Bateau:

	#fonction de creation 
	def __init__(self,taille,Enspositions): #Creation d'un bateau qui prend en paramètre la taille du bateau et et la l'ensemble de ses positions sur la grille.
											#la taille du bateau est comprise entre 1 et 4
		
	def positions(self): 	# position: Bateau -> Ensposition
							# Renvoie la liste des positions du bateau passé en paramètre si le bateau existe, ERREUR sinon.
		return				# La taille de la liste des positions renvoyées est égal a la taille du bateau

	def taille(self): 		#taille : Bateau -> int
							# Renvoie la taille du bateau entré en paramètre. ERREUR si le bateau n'existe pas.
		return			 	# 0 < taille(b:bateau) <= 4
		
	def est_detruit(self):	#est_detruit: Bateau -> bool
							# Renvoie TRUE si le bateau passé en paramètre est coulé ce qui implique que toutes ses positions ont été touchées, renvoie FALSE sinon. 
		return				# ERREUR si le bateau n'existe pas
		
	def nB_Pos_toucher(self): 	# nB_Pos_toucher: Bateau -> int
								# Renvoie le nombre de positions qui ont été touchées du bateau passé en paramètre. Lorsque le nombre de position touchées est égale a la taille du bateau. la fonction est_Detruit passe a TRUE.
		return

	def position_appartient(self,Position): # position_appartient: Bateau x Position -> bool
											# Renvoie TRUE si la position est dans l'Ensemble de positions du bateau. FALSE sinon. ERREUR si le bateau n'existe pas.
		return

	def est_toucher(self, Position): # est_toucher: Bateau x Position ->bool	
		return							 # Renvoie TRUE si la position entré en paramètre correspond à une des positions présente dans l'ensemble des positions du bateau. FALSE sinon, ERREUR si la position est non valide.

	def est_envue(self, Position): #est_manquer: Bateau x Position -> bool
		return					   # Renvoie TRUE si dans la position entré en paramètre, l'une des deux coordonnées correspond a une coordonnées presente dans l'ensemble des positions du bateau. False sinon. ERREUR si le bateau n'existe pas


	#Propriété type Bateau
		#L1: taille(creer_bateau(n: int,b: Bateau))= n
		#L2: nb_Pos_toucher(creer_bateau(n : int, b: Bateau)) = 0
		#L3: est-detruit(creer_bateau(n:int,b:Bateau)) = FALSE
		#L4: taille(b : Bateau) <= 4 et taille(b : Bateau) >0
		#L5: recuperer_position( b: Bateau) => est_detruit(b : Bateau) == FALSE
		#L6: supprimer_position(b : Bateau) => est_detruit(b : Bateau) == FALSE
		#L7: est_touche(b: Bateau, p : Position) =>est_detruit(b : Bateau) == FALSE


	# >> TEST UNITAIRE <<

	ensp= Enspositions()
	bat = Bateau(2,ensp)
	p=Position(1,2)
	p2=Position(5,6)
	bat.taille()
	bat.est_detruit()
	bat.nB_Pos_toucher()
	print bat.position_appartient(p)
	print bat.est_toucher(p2)
	print bat.est_envue(p2)
