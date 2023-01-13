import pygame, auswahl

pygame.init()


run = True

while run:

    a = auswahl.Auswahl()
    a.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()

pygame.quit()         