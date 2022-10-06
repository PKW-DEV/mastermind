import pygame
import mm

def win(fenetre, tentative):
    font = pygame.font.SysFont("monospace", 25)
    txt = font.render(f"Bravo tu as gagné en {tentative} tentative(s) ! Félicitations",1, mm.Rouge)
    fenetre.blit(txt,[20,700])
    pygame.display.update()
    return False


def loose(fenetre):
    font = pygame.font.SysFont("monospace", 25)
    txt = font.render(f"Perdu !", 1, mm.Rouge)
    fenetre.blit(txt, [400,700])
    pygame.display.update()
    return False

def calcul_res(secret, proposition):
    blanc = 0
    noir = 0
    i = 0
    j = 0
    for i in range(5):
        if proposition[i] == secret[i]:
            blanc = blanc + 1
        elif proposition[i] in secret:
            noir = noir + 1
    res = [blanc,noir]
    return res



def start():
    pygame.init()
    fenetre = pygame.display.set_mode([800,800])
    fenetre.fill(mm.Blanc)

    myfont = pygame.font.SysFont("monospace", 25)
    lab = myfont.render("MasterMind - Pierre Lilou Chérine",1, mm.Noir)
    fenetre.blit(lab,[100,750])
    pygame.display.update()

    mm.afficherPlateau(fenetre)
    mm.afficherChoixCouleur(fenetre)
    secret = mm.CreationSecret()
    #mm.afficherSecret(fenetre, secret)
    manche = True
    while manche:
        count = 0
        inc = 2
        partie = True
        while inc != 17 and partie:
            count = count + 1
            reponse = mm.construireProposition(fenetre, inc)
            total =calcul_res(secret, reponse)
            mm.afficherResultat(fenetre,total,inc)
            if reponse == secret:
                partie = win(fenetre, count)
                manche = False
            inc = inc + 1
        mm.afficherSecret(fenetre,secret)
        if partie is True:
            manche = loose(fenetre)
        
                
        
    mm.getChoixCouleur()
        
    enterpressed = False
    while not enterpressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                enterpressed = keys[pygame.K_RETURN]
                print("Appuie sur une touche")
            if event.type == pygame.QUIT:
                pygame.quit()
              
 
if __name__ == "__main__":
    start()

