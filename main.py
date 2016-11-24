def changerJoueur(j1,j2):
	j1.setActif(True)
	j2.setActif(False)

def entrer_position(j):
	taille=[1]#,2,3,4,4]
	for i in range(len(taille))
		ep = Ensposition()
		eb = Ensbateau(len(taille))
		print "Entrez les coordonnees du bateau de taille ",taille[i]
		for k in range (taille[i]):
				print "X = "
				x = input()
				print "Y = "
				y = input()
				p = position(x,y)
				if p.est_valide_position(): 
					ep.ajouterPosition(p)
				else:
					print "Les coordonnées que vous avez entrés dépasse la grille, veuillez les rerentrer "
					k = k-1

		b = Bateau(taille[i],ep)
		eb.ajouterBateau(b)
	j.modifensbateau(eb)
	return j

eb1 = Ensbateaux()	
eb2 = Ensbateaux()	
joueur1 = joueur(eb1,True)
joueur2 = joueur(eb2,False)
joueur1 = entrezposition(joueur1)
joueur2 = entrezposition(joueur2)

while not(j1.perdu() or j2.perdu()) :
	if j1.getActif :
		print("Entrer coordonnees à frapper ")
		print "X = "
		x = input()
		print "Y = "
		y = input()
		tir = tir(x,y)
		res = resultat(joueur2,tir)
		print res.resultat_tir(tir)

	if j2.getActif :
		print("Entrer coordonnees à frapper ")
		print "X = "
		x = input()
		print "Y = "
		y = input()
		tir = tir(x,y)
		res = resultat(joueur1,tir)
		res.resultat_tir(tir)

if j1.perdu :
	print "Le joueur 1 a perdu, force au joueur 2"

if j2.perdu : 
	print "Le joueur 2 a perdu, force au joueur 1"



