import pygame
import mm2

#En cas de partie gagnée
def win(fenetre, tentative):
    # Attribution d'un format(police et taille) à une variable
    font = pygame.font.SysFont("monospace", 25) 
    #Préparation à l'affichage en y indiquant la variable du format, le texte, la couleur, en utilisant la fonction render() de pygame attribué à la variable txt
    txt = font.render(f"Bravo tu as gagné en {tentative} tentative(s) ! Félicitations",1, mm2.Rouge) 
    #affichage du contenu de la variable txt sur la fenetre avec la fonction blit(text,[x,y])
    fenetre.blit(txt,[20,700])
    #Actualisation de la fenetre pygame pour afficher les changements effectués
    pygame.display.update()
    #on retourne False pour mettre fin au jeu
    return False

#En cas de partie perdu
def lose(fenetre):
    #Attribution à une variable font, le format et la taille
    font = pygame.font.SysFont("monospace", 25)
    #Attribution à une variable text le contenu de la fonction render qui pour parametre le text et la couleur
    txt = font.render(f"Perdu !", 1, mm2.Rouge)
    #Affichage sur la fenetre du contenue de la variable txt sur la fenetre à l'emplacement x,y
    fenetre.blit(txt, [400,700])
    #Actualisation de la fenetre pygame pour afficher les changements effectuées
    pygame.display.update()
    #Retourne False pour mettre fin à la partie
    return False

#Fonction de calcul du résultat
def calcul_res(secret, proposition):
    #initialisation de variable local blanc et noir à 0
    blanc = 0
    noir = 0
    #copy de la liste proposition pour une liste p2
    p2 = proposition.copy()
    #boucle pour à répéter 5 fois
    for i in range(5):
        #on regarde si un élément de secret à l'index i est égal à un élément de proposition au meme index i
        if secret[i] == proposition[i]:
            #si oui on ajout un pion blanc
            blanc = blanc+1
            #Nous retirons l'élement de la liste p2 pour ne plus le prendre en compte les pions mal placés
            p2.remove(proposition[i])
        #nous regardons si un element de secret à l'index i est contenu dans la liste p2
        elif secret[i] in p2:
            #si oui alors on ajoute un pion noir
            noir = noir + 1
            #retrait de cette elements de la liste p2 pour éviter de le comptabiliser plusieurs fois
            p2.remove(secret[i])
    #création d'une list res avec le nombre de pions blancs et de pions noirs
    res = [blanc,noir]
    #on renvoie le résultat
    return res




def start():
    #initialisation de pygame
    pygame.init()
    #création de la fenetre et de son format
    fenetre = pygame.display.set_mode([800,800])
    #couleur du fond de la fenètre
    fenetre.fill(mm2.Blanc)

    #affichage d'un texte
    myfont = pygame.font.SysFont("monospace", 25)
    lab = myfont.render("MasterMind - Pierre Lilou Chérine",1, mm2.Noir)
    fenetre.blit(lab,[100,750])
    pygame.display.update()

    #importation de fonctons contenu dans le fichier mm pour afficher le plateau et le choix des couleurs
    mm2.afficherPlateau(fenetre)
    mm2.afficherChoixCouleur(fenetre)
    #création de la combinaison secrète
    secret = mm2.CreationSecret()
    #initialisation de la variable manche à True
    manche = True
    #Tant que manche est vrai
    while manche:
        #initialisation de la variable count à 0
        count = 0
        #initialisation de la variable inc à 2 (qui veut dire que les pions seront placés à partir de la ligne 2)
        inc = 2
        #initialisation de la variable partie à True
        partie = True
        #Tant que la variable inc n'est pas égal à 17 (soit un maximum de 2 à 17 lignes) et que partie est vraie
        while inc != 17 and partie:
            #incrémentation du compteur
            count = count + 1
            #récupération de la combinaison créée par le joueur
            reponse = mm2.construireProposition(fenetre, inc)
            #Récupération du résultat de la proposition (pion blanc, pion noir)
            total =calcul_res(secret, reponse)
            #Affichage du résultat sous la forme de pion sur l'écran
            mm2.afficherResultat(fenetre,total,inc)
            #si la réponse est égal au secret alors
            if reponse == secret:
                # partie est assigné à la fonction win qui retourne False
                partie = win(fenetre, count)
                # la manche est arrété et passe donc a false
                manche = False
            #le compteur de ligne est incrémenté de un pour aller à la ligne suivante
            inc = inc + 1
        # on affiche le résultat
        mm2.afficherSecret(fenetre,secret)
        # Si la partie est encore en vrai (donc que toute les chances ont été utilisé) alors la partie est perdu
        if partie is True:
            # on assigne la variable manche à la fonction lose qui retourne False et qui mets fin au jeu
            manche = lose(fenetre)
        
        
    enterpressed = False
    while not enterpressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
              
 
if __name__ == "__main__":
    start()


