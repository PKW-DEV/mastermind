import pygame
import mm2

def win(fenetre, tentative):
    font = pygame.font.SysFont("monospace", 25)
    txt = font.render(f"Bravo tu as gagné en {tentative} tentative(s) ! Félicitations",1, mm2.Rouge)
    fenetre.blit(txt,[20,700])
    pygame.display.update()
    return False


def loose(fenetre):
    font = pygame.font.SysFont("monospace", 25)
    txt = font.render(f"Perdu !", 1, mm2.Rouge)
    fenetre.blit(txt, [400,700])
    pygame.display.update()
    return False


def calcul_res(secret, proposition):
    blanc = 0
    noir = 0
    p2 = proposition.copy()
    for i in range(5):
        if secret[i] == proposition[i]:
            blanc = blanc+1
            p2.remove(proposition[i])
        elif secret[i] in p2:
            noir = noir + 1
            p2.remove(secret[i])
    res = [blanc,noir]
    return res




def start():
    pygame.init()
    fenetre = pygame.display.set_mode([800,800])
    fenetre.fill(mm2.Blanc)

    myfont = pygame.font.SysFont("monospace", 25)
    lab = myfont.render("MasterMind - Pierre Lilou Chérine",1, mm2.Noir)
    fenetre.blit(lab,[100,750])
    pygame.display.update()

    mm2.afficherPlateau(fenetre)
    mm2.afficherChoixCouleur(fenetre)
    secret = mm2.CreationSecret()
    manche = True
    while manche:
        count = 0
        inc = 2
        partie = True
        while inc != 17 and partie:
            count = count + 1
            reponse = mm2.construireProposition(fenetre, inc)
            total =calcul_res(secret, reponse)
            mm2.afficherResultat(fenetre,total,inc)
            if reponse == secret:
                partie = win(fenetre, count)
                manche = False
            inc = inc + 1
        mm2.afficherSecret(fenetre,secret)
        if partie is True:
            manche = loose(fenetre)
        
                
        
    mm2.getChoixCouleur()
        
    enterpressed = False
    while not enterpressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
              
 
if __name__ == "__main__":
    start()


