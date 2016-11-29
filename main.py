#-*- coding: utf-8 -*-
from resultat import * 


def changerEtat(j):
	if j.etat() : 
		j.modif_etat(False)

	else :
		j.modif_etat(True)

	return j

def entrer_position(j):
	i = 0
	while j.ensbateaux().nb_bat_safe() < j.ensbateaux().tailleEB():
		ep = Enspositions(taille[i])
		b = Bateau(ep,taille[i])
		print "Entrez les coordonnees du bateau de taille ",taille[i]
		p = Positon(-1,-1)
		while ep.nb_position_pres() < ep.tailleEP() and not(j.ensbateaux().est_present_pos(p)):
			while not(p.est_valide_position()) : 
				print "Le X entré ou le Y entré n'est pas valide. Rerentrez vos coordonnées "
				print "X = "
				x = int(input())
				print "Y = "
				y = int(input())
				p = Position(x,y)

			if not(j.ensbateaux().est_present_pos(p)):
				ep.ajouterPosition(p)
			else :
				print "Cette position est déja utilisée. Bateau impossible a creer. Veuillez entrer d'autres positions pour votre bateau "


		b.setEnspositions(ep)
		if bat_bien_former(b) and (b.positions().tailleEP() == b.taillebat()):
			j.modif_Ensbateaux(b)
			i+=1

		else :
			print "Votre bateau est mal formé. Rerentrez toutes ses coordonnees"

	
	return j


taille=[1]#,2,3,4,4]
eb1 = Ensbateaux(len(taille))	
eb2 = Ensbateaux(len(taille))	
j1 = Joueur(eb1,True)
j2 = Joueur(eb2,False)
j1 = entrer_position(j1)
j2 = entrer_position(j2)

while not(j1.perdu() or j2.perdu()) :
	if j1.etat :
		print("Entrer coordonnees à frapper ")
		print "X = "
		x = int(input())
		print "Y = "
		y = int(input())
		tir = tir(x,y)
		res = resultat(joueur2,tir)
		print res.resultat_tir(tir)
		

	if j2.etat :
		print("Entrer coordonnees à frapper ")
		print "X = "
		x = int(input())
		print "Y = "
		y = int(input())
		res = resultat(j1,x,y)
		res.resultat_tir(tir)
	
	j1 = changerEtat(j1)
	j2 = changerEtat(j2)	

if j1.perdu :
	print "Le joueur 1 a perdu, force au joueur 2"

if j2.perdu : 
	print "Le joueur 2 a perdu, force au joueur 1"



