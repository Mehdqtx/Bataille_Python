

class Bateau:

	#fonction de creation 
	def __init__(self,taille, Enspositions): # creer_bateau : int x Enspositions -> Bateau 
											#Creation d'un bateau qui prend en paramètre la taille du bateau et l'ensemble de ses positions sur la grille.
											#la taille du bateau est comprise entre 1 et 4 
											#L2: nb_Pos_toucher(creer_bateau(n : int, b: Bateau)) = 0
											#L3: est-detruit(creer_bateau(n:int,b:Bateau)) = FALSE
		
	def positions(self): 	# position: Bateau -> Ensposition
							# Renvoie la liste des positions du bateau passé en paramètre si le bateau existe, ERREUR sinon.
							# La taille de la liste des positions renvoyées est égal a la taille du bateau

	def taille(self): 		#taille : Bateau -> int
							# Renvoie la taille du bateau entré en paramètre. ERREUR si le bateau n'existe pas.
					 		# 0 < taille(b:bateau) <= 4
					 		#L4: taille(b : Bateau) <= 4 et taille(b : Bateau) >0
		
	def est_detruit(self):	#est_detruit: Bateau -> bool
							# Renvoie TRUE si le bateau passé en paramètre est coulé ce qui implique que toutes ses positions ont été touchées ( utiliser fonction positions) ,renvoie FALSE sinon. 
							
		
	def nB_Pos_toucher(self): 	# nB_Pos_toucher: Bateau -> int
								# Renvoie le nombre de positions qui ont été touchées du bateau passé en paramètre. Lorsque le nombre de position touchées est égale a la taille du bateau. la fonction est_Detruit passe a TRUE.
								

	def position_appartient(self,Position): # position_appartient: Bateau x Position -> bool
											# Renvoie TRUE si la position est dans l'Ensemble de positions du bateau. FALSE sinon. ERREUR si le bateau n'existe pas.
		

	def est_toucher(self, Position): # est_toucher: Bateau x Position ->bool	
									 # Renvoie TRUE si la position entré en paramètre correspond à une des positions présente dans l'ensemble des positions du bateau. FALSE sinon, ERREUR si la position est non valide.
									 #L7: est_touche(b: Bateau, p : Position) => est_detruit(b : Bateau) == FALSE

	def est_envue(self, Position):  #est_manquer: Bateau x Position -> bool
						   			# Renvoie TRUE si dans la position entré en paramètre, l'une des deux coordonnées correspond a une coordonnées presente dans l'ensemble des positions du bateau. False sinon. ERREUR si le bateau n'existe pas
						   			#L7: est_envue(b: Bateau, p : Position) => est_detruit(b : Bateau) == FALSE

	
		


	# >> TEST UNITAIRE <<

	ensp= Enspositions()
	
	p=Position(1,2)
	p2=Position(5,6)
	ensp.ajouterPosition(p)
	ensp.ajouterPosition(p2)
	bat = Bateau(2,ensp)
	bat.taille()
	bat.est_detruit()
	bat.nB_Pos_toucher()
	print bat.position_appartient(p)
	print bat.est_toucher(p2)
	print bat.est_envue(p2)
