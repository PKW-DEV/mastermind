import pygame
import mm


def start():
    pygame.init()
    fenetre = pygame.display.set_mode([800,800])
    fenetre.fill(mm.Blanc)

    myfont = pygame.font.SysFont("monospace", 25)
    lab = myfont.render("MasterMind Groupe Pierre Lilou Chérine",1, mm.Noir)
    fenetre.blit(lab,[50,15])
    pygame.display.update()

    mm.afficherPlateau(fenetre)

    enterpressed = False
    while not enterpressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                enterpressed = keys[pygame.K_RETURN]
                print("appuie sur une touche")
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == "__main__":
    start()
