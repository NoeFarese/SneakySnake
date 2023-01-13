import pygame, sys, random
import auswahl
from pygame.math import Vector2

class HARD:
    def show(self):
        class FIELD:
            def __init__(self):
                self.random_wall()
                self.random_wall_two()
                self.random_wall_three()
                self.random_wall_four()
                self.random_wall_five()
                self.random_wall_six()
                self.random_wall_seven()
                self.random_wall_eight()
                self.random_wall_nine()
                self.random_wall_ten()

            def draw_wall(self):
                rect_wall = pygame.Rect(int(self.x_wall * cell_size), int(self.y_wall * cell_size), cell_size, cell_size)
                pygame.draw.rect(screen, (255, 0, 0), rect_wall)

                rect_wall_two = pygame.Rect(int(self.x_wall_two * cell_size), int(self.y_wall_two * cell_size), cell_size , cell_size)
                pygame.draw.rect(screen, (255, 0, 0), rect_wall_two)

                rect_wall_three = pygame.Rect(int(self.x_wall_three * cell_size), int(self.y_wall_three * cell_size), cell_size, cell_size)
                pygame.draw.rect(screen, (255, 0, 0), rect_wall_three)

                rect_wall_four = pygame.Rect(int(self.x_wall_four * cell_size), int(self.y_wall_four * cell_size), cell_size, cell_size)
                pygame.draw.rect(screen, (255, 0, 0), rect_wall_four)

                rect_wall_five = pygame.Rect(self.x_wall_five * cell_size, self.y_wall_five * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen,(255, 0, 0), rect_wall_five)

                rect_wall_six = pygame.Rect(self.x_wall_six * cell_size, self.y_wall_six * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen,(255, 0, 0), rect_wall_six)

                rect_wall_seven = pygame.Rect(self.x_wall_seven * cell_size, self.y_wall_seven * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen,(255, 0, 0), rect_wall_seven)

                rect_wall_eight = pygame.Rect(self.x_wall_eight * cell_size, self.y_wall_eight * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen,(255, 0, 0), rect_wall_eight)

                rect_wall_nine = pygame.Rect(self.x_wall_nine * cell_size, self.y_wall_nine * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen,(255, 0, 0), rect_wall_nine)

                rect_wall_ten = pygame.Rect(self.x_wall_ten * cell_size, self.y_wall_ten * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen,(255, 0, 0), rect_wall_ten)

            def random_wall(self):
                self.x_wall = random.randint(0, cell_number -1)
                self.y_wall = random.randint(0, cell_number -1)
                self.pos_wall = Vector2(self.x_wall, self.y_wall)
                #self.posi_wall = Vector2(rect_wall.w, rect_wall.h)
    
            def random_wall_two(self):
                self.x_wall_two = random.randint(0, cell_number -1)    
                self.y_wall_two = random.randint(0, cell_number -1)
                self.pos_wall_two = Vector2(self.x_wall_two, self.y_wall_two)

            def random_wall_three(self):
                self.x_wall_three = random.randint(0, cell_number -1)
                self.y_wall_three = random.randint(0, cell_number -1)
                self.pos_wall_three = Vector2(self.x_wall_three, self.y_wall_three)      

            def random_wall_four(self):
                self.x_wall_four = random.randint(0, cell_number -1)
                self.y_wall_four = random.randint(0, cell_number -1)
                self.pos_wall_four = Vector2(self.x_wall_four, self.y_wall_four)        

            def random_wall_five(self):
                self.x_wall_five = random.randint(0, cell_number -1)
                self.y_wall_five = random.randint(0, cell_number -1)
                self.pos_wall_five = Vector2(self.x_wall_five, self.y_wall_five)     

            def random_wall_six(self):
                self.x_wall_six = random.randint(0, cell_number -1)
                self.y_wall_six = random.randint(0, cell_number -1)
                self.pos_wall_six = Vector2(self.x_wall_six, self.y_wall_six)  

            def random_wall_seven(self):
                self.x_wall_seven = random.randint(0, cell_number -1)
                self.y_wall_seven = random.randint(0, cell_number -1)
                self.pos_wall_seven = Vector2(self.x_wall_seven, self.y_wall_seven)  

            def random_wall_eight(self):
                self.x_wall_eight = random.randint(0, cell_number -1)
                self.y_wall_eight = random.randint(0, cell_number -1)
                self.pos_wall_eight = Vector2(self.x_wall_eight, self.y_wall_eight)  

            def random_wall_nine(self):
                self.x_wall_nine = random.randint(0, cell_number -1)
                self.y_wall_nine = random.randint(0, cell_number -1)
                self.pos_wall_nine = Vector2(self.x_wall_nine, self.y_wall_nine)  

            def random_wall_ten(self):
                self.x_wall_ten = random.randint(0, cell_number -1)
                self.y_wall_ten = random.randint(0, cell_number -1)
                self.pos_wall_ten = Vector2(self.x_wall_ten, self.y_wall_ten)  
           
        class SNAKE:
            def __init__(self):
                self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
                self.direction = Vector2(1,0)
                self.new_block = False

                #self.head = pygame.image.load('Bilder/snake/head.png').convert_alpha()
                #self.tail = pygame.image.load('Bilder/snake/tail.png').convert_alpha()
                #self.body = pygame.image.load('Bilder/snake/body.png').convert_alpha()

                self.head_up = pygame.image.load('Bilder/snake/head_up.png').convert_alpha()
                self.head_down = pygame.image.load('Bilder/snake/head_down.png').convert_alpha()
                self.head_right = pygame.image.load('Bilder/snake/head_right.png').convert_alpha()
                self.head_left = pygame.image.load('Bilder/snake/head_left.png').convert_alpha()
                self.tail_up = pygame.image.load('Bilder/snake/tail_up.png').convert_alpha()
                self.tail_down = pygame.image.load('Bilder/snake/tail_down.png').convert_alpha()
                self.tail_right = pygame.image.load('Bilder/snake/tail_right.png').convert_alpha()
                self.tail_left = pygame.image.load('Bilder/snake/tail_left.png').convert_alpha()
                self.body_vertical = pygame.image.load('Bilder/snake/body_vertical.png').convert_alpha()
                self.body_horizontal = pygame.image.load('Bilder/snake/body_horizontal.png').convert_alpha()
                self.body_tr = pygame.image.load('Bilder/snake/body_tr.png').convert_alpha()
                self.body_tl = pygame.image.load('Bilder/snake/body_tl.png').convert_alpha()
                self.body_br = pygame.image.load('Bilder/snake/body_br.png').convert_alpha()
                self.body_bl = pygame.image.load('Bilder/snake/body_bl.png').convert_alpha()

            def draw_snake(self):
                #for block in self.body:
                # x_pos = int(block.x * cell_size)
                # y_pos = int(block.y * cell_size)
                    #rect_block = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
                    #pygame.draw.rect(screen,(0,136,255),rect_block)

                self.updating_head_graphics()
                self.updating_tail_graphics()

                for index,block in enumerate(self.body):
                    x_pos = int(block.x * cell_size)    
                    y_pos = int(block.y * cell_size)
                    block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

                    if index == 0:
                            screen.blit(self.head,block_rect)
                    elif index == len(self.body) - 1:
                            screen.blit(self.tail, block_rect)
                    else:
                        previous_block = self.body[index + 1] - block
                        next_block = self.body[index -1] - block        
                        if previous_block.x == next_block.x:
                            screen.blit(self.body_vertical, block_rect) 
                        elif previous_block.y == next_block.y:
                            screen.blit(self.body_horizontal, block_rect)     
                        else:
                            if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                                screen.blit(self.body_tl,block_rect)
                            elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: 
                                screen.blit(self.body_bl,block_rect)
                            elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                                screen.blit(self.body_tr,block_rect)
                            elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                                screen.blit(self.body_br,block_rect)        

            def updating_head_graphics(self):
                head_relation = self.body[1] - self.body[0]             
                if head_relation == Vector2(1,0):
                    self.head = self.head_left
                elif head_relation == Vector2(-1,0):
                    self.head = self.head_right
                elif head_relation == Vector2(0,1):
                    self.head = self.head_up
                elif head_relation == Vector2(0,-1):
                    self.head = self.head_down            

            def updating_tail_graphics(self):
                tail_relation = self.body[-2] - self.body[-1]
                if tail_relation == Vector2(1,0):
                    self.tail = self.tail_left
                elif tail_relation == Vector2(-1,0):
                    self.tail = self.tail_right
                elif tail_relation == Vector2(0,1):
                    self.tail = self.tail_up   
                elif tail_relation == Vector2(0,-1):
                    self.tail = self.tail_down         

            def move_snake(self):
                if self.new_block == True:
                    body_copy = self.body[:]   
                    body_copy.insert(0,body_copy[0] + self.direction)  
                    self.body = body_copy[:]
                    self.new_block = False    
                    
                else:
                    body_copy = self.body[:-1]   
                    body_copy.insert(0,body_copy[0] + self.direction)  
                    self.body = body_copy[:]

            ##rotated_head = self.head_up.rotate(90)
            #if event.key == pygame.K_RIGHT:

            def add_block(self):
                self.new_block = True

            def reset_snake(self):
                self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
                self.direction = Vector2(0,0)

        class FRUIT:
            def __init__(self):
                self.randomize()

            def draw_fruit(self):
                rect_fruit = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
                screen.blit(apple, rect_fruit)
                #apple = pygame.transform.scale(apple,(5,5))
                #pygame.draw.rect(screen,(126,166,114),rect_fruit)

            def randomize(self):
                self.x = random.randint(0,cell_number -1)
                self.y = random.randint(0,cell_number -1)
                self.pos = Vector2(self.x,self.y)

        class MAIN: 

            #score_text = 0
            def __init__(self):
                self.snake = SNAKE()
                self.fruit = FRUIT()
                self.wall = FIELD()

            def update (self):
                self.snake.move_snake()
                self.check_collision()
                self.check_loose()

            def draw_elements(self):
                self.fruit.draw_fruit()
                self.snake.draw_snake()
                self.wall.draw_wall()
                self.score()

            def check_collision(self): #checkt ob schlange die frucht berührt und macht die schlange länger
                if self.fruit.pos == self.snake.body[0]:
                    self.fruit.randomize()
                    self.snake.add_block()
                    self.wall.random_wall()
                    self.wall.random_wall_two()
                    self.wall.random_wall_three() 
                    self.wall.random_wall_four()
                    self.wall.random_wall_five()
                    self.wall.random_wall_six()
                    self.wall.random_wall_seven()
                    self.wall.random_wall_eight()
                    self.wall.random_wall_nine()
                    self.wall.random_wall_ten()
                    #score_text += 1

            def check_loose(self): #checkt kollision mit dem rand oder mit der schlange selber
                if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
                    self.wall.random_wall()
                    self.wall.random_wall_two()
                    self.wall.random_wall_three() 
                    self.wall.random_wall_four()
                    self.wall.random_wall_five()
                    self.wall.random_wall_six()
                    self.wall.random_wall_seven()
                    self.wall.random_wall_eight()
                    self.wall.random_wall_nine()
                    self.wall.random_wall_ten()
                    self.game_over()

                for block in self.snake.body[1:]:
                    if block == self.snake.body[0]:
                        self.wall.random_wall()
                        self.wall.random_wall_two()
                        self.wall.random_wall_three() 
                        self.wall.random_wall_four()
                        self.wall.random_wall_five()
                        self.wall.random_wall_six()
                        self.wall.random_wall_seven()
                        self.wall.random_wall_eight()
                        self.wall.random_wall_nine()
                        self.wall.random_wall_ten()
                        self.game_over() 

                if self.wall.pos_wall == self.snake.body[0] or self.wall.pos_wall_two == self.snake.body[0] or self.wall.pos_wall_three == self.snake.body[0] or self.wall.pos_wall_four == self.snake.body[0] or self.wall.pos_wall_five == self.snake.body[0] or self.wall.pos_wall_six == self.snake.body[0] or self.wall.pos_wall_seven == self.snake.body[0] or self.wall.pos_wall_eight == self.snake.body[0] or self.wall.pos_wall_nine == self.snake.body[0] or self.wall.pos_wall_ten == self.snake.body[0]:  
                    self.wall.random_wall()
                    self.wall.random_wall_two()
                    self.wall.random_wall_three() 
                    self.wall.random_wall_four()
                    self.wall.random_wall_five()
                    self.wall.random_wall_six()
                    self.wall.random_wall_seven()
                    self.wall.random_wall_eight()
                    self.wall.random_wall_nine()
                    self.wall.random_wall_ten()
                    self.game_over()

                #if len(self.wall.random_wall) == self.snake.body[0] or len(self.wall.random_wall_two) == self.snake.body[0] or len(self.wall.random_wall_three) == self.snake.body[0] or len(self.wall.random_wall_four) == self.snake.body[0] or len(self.wall.random_wall_five) == self.snake.body[0]:
                 #   self.game_over()

                #if self.snake.body[0].x == self.wall.x_wall and self.snake.body[0].y == self.wall.y_wall:
                #   self.wall.random_wall()
                #  self.wall.random_wall_two()
                # self.game_over()   
                
            def game_over(self):
                self.snake.reset_snake()        

            def score(self):
                #print(score_text)
                score_text = str(len(self.snake.body) -3) #Punkte entsprechen der Länge der Schlange, sie startet schon mit 3 Blöcken (Kopf, körper und das Ende der Schlange), darum -3, dass die Punkte bei 0 anfangen
                score_show = font.render(score_text,True,(0,0,0))
                score_x = int(cell_size / cell_number +50) # cellsize / cellnumber wäre ganz oben links an der Ecke
                score_y = int(cell_size / cell_number +50)
                score_rect = score_show.get_rect(center = (score_x, score_y))
                apple_rect = apple.get_rect(midleft = (score_rect.right, score_rect.centery))
                
                screen.blit(score_show,score_rect)
                screen.blit(apple, apple_rect)

        pygame.init()
        cell_size = 40
        cell_number = 20
        screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
        clock = pygame.time.Clock()
        apple = pygame.image.load('Bilder/apple.png').convert_alpha()
        font = pygame.font.Font('Bilder/full-Pack-2025.ttf', 35)
        self.FPS = 60

        pygame.display.set_caption("SneakySnake Hard")
        self.fruit = FRUIT()
        self.snake = SNAKE()
        self.wall = FIELD()

        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE,150)

        main_game = MAIN()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == SCREEN_UPDATE:
                    main_game.update() 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if main_game.snake.direction.y != 1:
                            main_game.snake.direction = Vector2(0, -1)  

                    if event.key == pygame.K_RIGHT:
                        if main_game.snake.direction.x != -1:
                            main_game.snake.direction = Vector2(1,0)

                    if event.key == pygame.K_LEFT:
                        if main_game.snake.direction.x != 1:
                            main_game.snake.direction = Vector2(-1,0)  

                    if event.key == pygame.K_DOWN:
                        if main_game.snake.direction.y != -1:
                            main_game.snake.direction = Vector2(0,1)    

                    if event.key == pygame.K_ESCAPE:
                        run = False
                         
            screen.fill((0,136,0))
            main_game.draw_elements()
            pygame.display.update()
            clock.tick(60)