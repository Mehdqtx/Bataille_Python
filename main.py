def changerJoueur(j1,j2):
	j1.modif_etat(True)
	j2.modif_etat(False)

def entrer_position(j):
	taille=[1]#,2,3,4,4]
	eb = Ensbateaux(len(taille))
	while eb.nb_bat_safe() < eb.tailleEB():
		ep = Enspositions(taille[i])
		b = bateau(ep,taille[i])
		print "Entrez les coordonnees du bateau de taille ",taille[i]
		while ep.nb_position_pres() < ep.tailleEP():
			print "X = "
			x = input()
			print "Y = "
			y = input()
			p = position(x,y)
			if not(eb.est_present_pos(p))
				ep.ajouterPosition(p)
			else 
				print "Cette position est déja utilisée. Veuillez entrer une autre position ou relancer le programme si votre bateau ne peut être complété"


		if bat_bien_former(b):
			b.setEnspositions(ep)
			eb.ajouterBateau(b)
			eb.modif_nb_bat_safe() = eb.nb_bat_safe() + 1
			i++

		else 
			print "Votre bateau est mal formé. Rerentrez ses coordonnees"

	for b in eb :
		j.ensbateaux().ajouterBateau(b);
	return j

eb1 = Ensbateaux()	
eb2 = Ensbateaux()	
joueur1 = joueur(eb1,True)
joueur2 = joueur(eb2,False)
joueur1 = entrezposition(joueur1)
joueur2 = entrezposition(joueur2)

while not(j1.perdu() or j2.perdu()) :
	if j1.etat :
		print("Entrer coordonnees à frapper ")
		print "X = "
		x = input()
		print "Y = "
		y = input()
		tir = tir(x,y)
		res = resultat(joueur2,tir)
		print res.resultat_tir(tir)

	if j2.etat :
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



