#Type Bateau

class Bateau:
	def __init__(self,colonne,ligne,taille,num,direction): 
	#Creer un bateau de taille donnee, avec un numero donne, une direction donnee, aux coordonnees donnees
	#pre : 21 > colonne >= 0
	#pre : 21 > ligne  >= 0
	#pre : 0 < taille < 5
	#pre : dir = 0 si le bateau est horizontal, 1 sinon
	# -> Bateau

	self.colonne = colonne
	self.ligne = ligne
	self.taille = int(taille)
	self.num = int(num)
	self.direction  = direction

	def NumeroBateau(self):
	#Renvoie le numero du bateau
	#Bateau -> Int
	return self.num

	def TailleBateau(self):
	#Renvoie la taille du bateau
	#Bateau -> Int
	return self.taille

	def DirectionBateau(self):
	#Renvoie 0 si le bateau est horizontal, 1 sinon
	#Bateau -> Int
	return self.direction


	def LigneBateau(self):
	#Renvoie la ligne du bateau
	#Bateau -> Int
	return self.ligne
	
	
	def ColonneBateau(self):
	#Renvoie la colonne du bateau
	#Bateau -> Int
	return self.colonne
