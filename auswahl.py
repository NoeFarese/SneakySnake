import pygame, sys
import easy, hard

class Auswahl: 
    def show(self):
        pygame.init()

        black = (0, 0, 0)

        Screen_Height = 600
        Screen_Width = 740
        screen = pygame.display.set_mode((Screen_Width, Screen_Height))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Auswahlmenü")
        main_font = pygame.font.SysFont("cambria", 50)

        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        text = font.render('Wählen Sie das Level aus', black, black)

        textRect = text.get_rect()
        textRect.center = (370, 100)

        easy_img = pygame.image.load("Bilder/button_easy.png").convert_alpha()
        hard_img = pygame.image.load("Bilder/button_hard.png").convert_alpha()
        exit_img = pygame.image.load("Bilder/quit_button.png").convert_alpha()

        class Button():
            def __init__(self, x, y, image, scale):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

            def button(self):
                action = False
                  
                pos = pygame.mouse.get_pos()
                
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == True and action == False :
                        self.clicked = True
                        action = True

               

                    pygame.mouse.get_pressed() == False

                screen.blit(self.image, (self.rect.x, self.rect.y))
                return action
               

        easy_button = Button(250, 150, easy_img, 0.8)
        hard_button = Button(260, 300, hard_img, 0.8)
        exit_button = Button(260, 450, exit_img, 0.65)
            
        run = True
        while run:

            screen.fill("grey")
            screen.blit(text, textRect)

            if easy_button.button():
                e = easy.EASY()
                e.show()

            if hard_button.button():
                h = hard.HARD()
                h.show()

            if exit_button.button():
                pygame.quit()
                sys.exit()
            #if easy_button.clicked:
             #   print('easy_button_clicked')

            #if hard_button.clicked:
             #   print('hard_button_clicked')
               
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

               # if event.type == pygame.MOUSEBUTTONDOWN:
                  #      print("clicked uf loggere")    
                ##    if event.button == 1:

                pygame.display.update()

        pygame.quit()         