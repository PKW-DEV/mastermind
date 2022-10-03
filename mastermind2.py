import pygame
import mm2

def win(fenetre, tentative):
    font = pygame.font.SysFont("monospace", 25)
    txt = font.render(f"Bravo tu as gagné en {tentative} tentative(s) ! Félicitations",1, mm2.Rouge)
    fenetre.blit(txt,[20,700])
    pygame.display.update()
    print("C'est gagné !")

    return False


def calcul_res(secret, proposition):
    blanc = 0
    noir = 0
    i = 0
    j = 0
    rm = []
    while i != 5:
        if secret[i] == proposition[i]:
            rm.append(i)
            blanc = blanc+1
        i = i+1
    while j != 5:
        if secret[j] in proposition and j not in rm:
            noir = noir + 1
        j = j+1
    res = [blanc,noir]
    return res


def loose(fenetre):
    font = pygame.font.SysFont("monospace", 25)
    txt = font.render(f"Perdu !", 1, mm2.Rouge)
    fenetre.blit(txt, [400,700])
    pygame.display.update()
    return False


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
    mm2.afficherSecret(fenetre,secret)

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
            inc = inc + 1
        mm2.afficherSecret(fenetre,secret)
        manche = loose()


        
    mm2.getChoixCouleur()
        
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
