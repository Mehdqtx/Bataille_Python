#-*- coding: utf-8 -*-
from resultat import * 


def changerEtat(j): # changerEtat : Joueur -> Joueur
					# Fonction permettant de faire passer le joueur dans l'etat actif s'il etait inactif, inactif s'il etait actif.
	j.modif_etat()

	return j


def entrer_position(j): # entrer_position : Joueur -> Joueur
						# Fonction qui va permettre de placer les bateaux de chaque joueur.
						# Tour à tour ils vont avoir le choix de placer leur bateaux dans la grille 21*21
						# Chaque joueur possède sa propre grille fictive. Il est donc possible que les deux joueur place un bateau sur la meme position.
						# Chaque joueur possède un ensemble de bateaux, 5 bateaux : un de taille 1, un de taille 2, 1 de taille 3, 2 de taille 4.
						# Le positionnement des bateaux de taille > 1 se realise en entrant toute ses positions. (exemple : un bateau de taille 2 a deux positions à placer)
						 # >> Le positionnement de tel bateaux implique de placer chaque positions a la suite les unes des autres pour ne pas creer un bateau disloquer ou un porte avion.
	i = 0

	# Compare le nombre de bateaux présent dans l'ensemble a la taille de l'ensemble de bateaux qui a été donné par l'utilisateur lors de la creation de l'ensemble
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
		res = resultat(j2,x,y)
		print res.resultat_tir(x,y)
		

	if j2.etat :
		print("Entrer coordonnees à frapper ")
		print "X = "
		x = int(input())
		print "Y = "
		y = int(input())
		res = resultat(j1,x,y)
		print res.resultat_tir(x,y)
	
	j1 = changerEtat(j1)
	j2 = changerEtat(j2)	

if j1.perdu :
	print "Le joueur 1 a perdu, force au joueur 2"

if j2.perdu : 
	print "Le joueur 2 a perdu, force au joueur 1"



