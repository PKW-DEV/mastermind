import pygame
import mm

# En cas de partie gagnée
def win(fenetre, tentative):
    # Attribution d'un format (police et taille) à une variable
    font = pygame.font.SysFont("monospace", 25) 
    # Préparation à l'affichage en y indiquant la variable du format, le texte, la couleur, en utilisant la fonction render() de pygame attribué à la variable txt
    txt = font.render(f"Bravo tu as gagné en {tentative} tentative(s) ! Félicitations",1, mm.Rouge) 
    # Affichage du contenu de la variable txt sur la fenetre avec la fonction blit(text,[x,y])
    fenetre.blit(txt,[20,700])
    # Actualisation de la fenêtre pygame pour afficher les changements effectués
    pygame.display.update()
    # On retourne False pour mettre fin au jeu
    return False

# En cas de partie perdue
def lose(fenetre):
    # Attribution à une variable font, le format et la taille
    font = pygame.font.SysFont("monospace", 25)
    # Attribution à une variable text le contenu de la fonction render qui pour paramètre le texte et la couleur
    txt = font.render(f"Perdu !", 1, mm.Rouge)
    # Affichage sur la fenêtre du contenu de la variable txt sur la fenêtre à l'emplacement x,y
    fenetre.blit(txt, [400,700])
    # Actualisation de la fenêtre pygame pour afficher les changements effectués
    pygame.display.update()
    # Retourne False pour mettre fin à la partie
    return False

# Fonction de calcul du résultat
def calcul_res(secret, proposition):
    # Initialisation de variable locale blanc et noir à 0
    blanc = 0
    noir = 0
    # Copie de la liste proposition pour une liste p2
    p2 = proposition.copy()
    # Boucle pour à répéter 5 fois
    for i in range(5):
        # On regarde si un élément de secret à l'index i est égal à un élément de proposition au même index i
        if secret[i] == proposition[i]:
            # Si oui on ajout un pion blanc
            blanc = blanc+1
            # Nous retirons l'élement de la liste p2 pour ne plus le prendre en compte les pions mal placés
            p2.remove(proposition[i])
        # Nous regardons si un élement de secret à l'index i est contenu dans la liste p2
        elif secret[i] in p2:
            # Si oui alors on ajoute un pion noir
            noir = noir + 1
            # Retrait de cet élement de la liste p2 pour éviter de le comptabiliser plusieurs fois
            p2.remove(secret[i])
    # Création d'une liste res avec le nombre de pions blancs et de pions noirs
    res = [blanc,noir]
    # On renvoie le résultat
    return res


def start():
    # Initialisation de pygame
    pygame.init()
    # Création de la fenêtre et de son format
    fenetre = pygame.display.set_mode([800,800])
    # Couleur du fond de la fenêtre
    fenetre.fill(mm.Blanc)

    # Affichage d'un texte
    myfont = pygame.font.SysFont("monospace", 25)
    lab = myfont.render("MasterMind - Pierre Lilou Chérine",1, mm.Noir)
    fenetre.blit(lab,[100,750])
    pygame.display.update()

    # Importation de fonctions contenues dans le fichier mm pour afficher le plateau et le choix des couleurs
    mm.afficherPlateau(fenetre)
    mm.afficherChoixCouleur(fenetre)
    # Création de la combinaison secrète
    secret = mm.CreationSecret()
    # Initialisation de la variable manche à True
    manche = True
    # Tant que manche est Vrai
    while manche:
        # Initialisation de la variable count à 0
        count = 0
        # Initialisation de la variable inc à 2 (qui veut dire que les pions seront placés à partir de la ligne 2)
        inc = 2
        # Initialisation de la variable partie à True
        partie = True
        # Tant que la variable inc n'est pas égale à 17 (soit un maximum de 2 à 17 lignes) et que partie est vraie
        while inc != 17 and partie:
            # Incrémentation du compteur
            count = count + 1
            # Récupération de la combinaison créée par le joueur
            reponse = mm.construireProposition(fenetre, inc)
            # Récupération du résultat de la proposition (pion blanc, pion noir)
            total =calcul_res(secret, reponse)
            # Affichage du résultat sous la forme de pion sur l'écran
            mm.afficherResultat(fenetre,total,inc)
            # Si la réponse est égale au secret alors
            if reponse == secret:
                # Partie est assignée à la fonction win qui retourne False
                partie = win(fenetre, count)
                # La manche est arrétée et passe donc à False
                manche = False
            # Le compteur de ligne est incrémenté de un pour aller à la ligne suivante
            inc = inc + 1
        # On affiche le résultat
        mm.afficherSecret(fenetre,secret)
        # Si la partie est encore en Vrai (donc que toutes les chances ont été utilisé) alors la partie est perdue
        if partie is True:
            # On assigne la variable manche à la fonction lose qui retourne False et qui met fin au jeu
            manche = lose(fenetre)
        
                
        
    mm.getChoixCouleur()
        
    enterpressed = False
    while not enterpressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
              
 
if __name__ == "__main__":
    start()


