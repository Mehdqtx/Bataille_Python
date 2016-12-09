#-*- coding: utf-8 -*-
class Position:
	def __init__(self,coordonneeX,coordonneeY): # creer_position : int * int -> Positiion
												# Constructeur du type position. Un bateau est composé d'une ou plusieurs positions
		return

	def absice(self): 	# absice : Position -> Int
		return			# permet de recuperer l'absice d'une position
						# absice(creer_position(a,b))=a
						

	def ordonnee(self):	# ordonnee : Position -> Int
		return			# permet de recuperer l'ordonnée d'une position

	def toucher(self):	# toucher : Position -> bool
		return			# permet de recuperer l'etat d'une position à savoir si il est touché ou pas
						# toucher(creer_position(a,b)) = false

	def modif_toucher(self): # modif_toucher : Position -> Position
		return				 # Permet de modifier l'état de la position. Si la position est à touché elle ne doit plus etre modifiée sinon on passe son etat a touché

	def est_valide_position(self): # verifie si la position créée est a l'intérieur des limites imposées par le sujet : 20 case en absices, 20 cases en ordonnee
		return					   # est_valide_position(p : position) = true ==> 0 < absice(p) <= 20 et 0 <ordonnee(p) <= 20




#Test unitaire

p = Position(1,2); 
pos = Position(3,25);
pos1 = Position(25,3);
print p.absice()==1; # Doit renvoyer true
print p.ordonnee()==2; # Doit renvoyer true
print pos.est_valide_position(); # Doit renvoyer false
print pos1.est_valide_position(); # Doit renvoyer false
print p.toucher(); # Doit renvoyer false
p.modif_toucher()
print p.toucher() # Doit renvoyer true
p.modif_toucher()
print p.toucher() # Doit renvoyer true