
class Position:
	def __init__(self,coordonneeX,coordonneeY): # creer_position : int * int -> Positiion
												# Constructeur du type position. Un bateau est composé d'une ou plusieurs positions


	def absice(self): 	# absice : int * int -> Position 
						# permet de recuperer l'absice d'une position
						# absice(creer_position(a,b))=a
						# ordonnee(creer_position(a,b))= b
						# toucher(creer_position(a,b)) = false

	def ordonnee(self):	# ordonnee : Position -> int
						# permet de recuperer l'ordonnée d'une position

	def toucher(self):	# toucher : Position -> bool
						# permet de recuperer l'etat d'une position à savoir si il est touché ou pas

	def modif_toucher(self):# modif_toucher : Position -> bool
							# Permet de modifier l'état de la position. Si la position est à touché elle ne doit plus etre modifiée sinon on la passe à TRUE

	def est_valide_position(self): # verifie si la position crée est a l'intérieur des limites imposées par le sujet : 20 case en absices, 20 cases en ordonnee
									# est_valide_position(p : position) == true ==> 0<absice(p)<=20 et 0<ordonnee(p)<=20



	#Test unitaire
	p = position(1,2);
	pos = position(3,25);
	pos1 = position(25,3);
	p.absice();
	p.ordonnee();
	pos.est_valide_position();
	pos1.est_valide_position();
	p.toucher();