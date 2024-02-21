import pygame,sys,random


pygame.init()
WİDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode((WİDTH,HEIGHT))
clock = pygame.time.Clock()

#define SCALE and max,min Speed
SCALE=35  
MAX_SPEED=8
pygame.font.init()
TEXT_FONT = pygame.font.SysFont("Arial",35)
#Spawn Setting
TOP_SPAWN_AREA = [WİDTH/4, 3*(WİDTH/4), 0, HEIGHT/4]
RIGHT_SPAWN_AREA = [0,WİDTH/4,HEIGHT/4,3*(HEIGHT/4)]
LEFT_SPAWN_AREA = [3*(WİDTH/4),WİDTH-SCALE,HEIGHT/4,3*(HEIGHT/4)]

#Music Setting 
pygame.mixer.init()
pygame.mixer.music.load("Sounds/theme.mp3")
pygame.mixer.music.play(loops=0,start=10,fade_ms=50000)

background_img = pygame.image.load("Graphics/Backgrounds/background.png").convert()
background_img = pygame.transform.scale(background_img,(WİDTH,HEIGHT))



class HUSKARL(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        SPAWN_AREA = TOP_SPAWN_AREA
        self.x= random.randint(SPAWN_AREA[0],SPAWN_AREA[1])
        self.y= random.randint(SPAWN_AREA[2],SPAWN_AREA[3])
        
        self.huskarl_img = pygame.image.load("Graphics/Characters/huskarl_purple.png").convert_alpha()
        self.huskarl_img= pygame.transform.scale(self.huskarl_img,(SCALE,SCALE))
        self.rect = self.huskarl_img.get_rect(topleft= (self.x,self.y))

        
    
        self.velocity_x = random.randint(1,MAX_SPEED)* random.choice([-1,1])
        self.velocity_y = random.randint(1,MAX_SPEED) * random.choice([-1,1])
          
    def update(self):
        self.move()
        self.check_border()
        self.draw_huskarl()
        self.collide()

    def collide(self):
        if (pygame.sprite.spritecollide(self,game.bowman_group,False)):
            collided_items = pygame.sprite.spritecollide(self,game.bowman_group,True)    

            huskarl = HUSKARL()
            huskarl.rect =huskarl.huskarl_img.get_rect(center = (collided_items[0].rect.x,collided_items[0].rect.y))
            game.huskarl_group.add(huskarl)

    def draw_huskarl(self):
        SCREEN.blit(self.huskarl_img,self.rect)


    def move(self):
        self.rect.x = self.rect.x + self.velocity_x
        self.rect.y = self.rect.y + self.velocity_y
        
    def check_border(self):
        #check vertical border
        if self.rect.x+SCALE > WİDTH or self.rect.x < 0:
            self.velocity_x= self.velocity_x*-1
        #check horizanta border
        if self.rect.y+SCALE> HEIGHT or self.rect.y< 0:
            self.velocity_y= self.velocity_y*-1
        
class BOWMAN(pygame.sprite.Sprite):   
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        SPAWN_AREA = RIGHT_SPAWN_AREA
        self.x= random.randint(SPAWN_AREA[0],SPAWN_AREA[1])
        self.y= random.randint(SPAWN_AREA[2],SPAWN_AREA[3])
        
        self.bowman_img= pygame.image.load("Graphics/Characters/bowman_red.png").convert_alpha()
        self.bowman_img = pygame.transform.scale(self.bowman_img,(SCALE,SCALE))
        self.rect = self.bowman_img.get_rect(topleft= (self.x,self.y))

        
        
        self.velocity_x = random.randint(1,MAX_SPEED)* random.choice([-1,1])
        self.velocity_y = random.randint(1,MAX_SPEED) * random.choice([-1,1])

    def collide(self):
        if (pygame.sprite.spritecollide(self,game.teutonic_group,False)):
            collided_items = pygame.sprite.spritecollide(self,game.teutonic_group,True)

            bowman = BOWMAN()
            bowman.rect = bowman.bowman_img.get_rect(center = (collided_items[0].rect.x,collided_items[0].rect.y))
            game.bowman_group.add(bowman)
          
    def update(self):
        self.move()
        self.check_border()
        self.draw_bowman()
        self.collide()
    
    def draw_bowman(self):
        SCREEN.blit(self.bowman_img,self.rect)       

    def move(self):
        self.rect.x = self.rect.x + self.velocity_x
        self.rect.y = self.rect.y + self.velocity_y
        

    def check_border(self):
        #check vertical border
        if self.rect.x+SCALE > WİDTH or self.rect.x < 0:
            self.velocity_x= self.velocity_x*-1
        #check horizanta border
        if self.rect.y+SCALE> HEIGHT or self.rect.y< 0:
            self.velocity_y= self.velocity_y*-1
    
class TEUTONIC(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.teutonic_img = pygame.image.load("Graphics/Characters/teutonic_blue.png").convert_alpha()
        self.teutonic_img= pygame.transform.scale(self.teutonic_img,(SCALE,SCALE))

        SPAWN_AREA = LEFT_SPAWN_AREA
        self.x = random.randint(SPAWN_AREA[0],SPAWN_AREA[1])
        self.y = random.randint(SPAWN_AREA[2],SPAWN_AREA[3])

        self.rect = self.teutonic_img.get_rect(topleft= (self.x,self.y))

        self.velocity_x = random.randint(1,MAX_SPEED)* random.choice([-1,1])
        self.velocity_y = random.randint(1,MAX_SPEED) * random.choice([-1,1])

    def update(self):
        self.move()
        self.check_border()
        self.draw_teutonic()
        self.collision()

    def collision(self):
        pygame.sprite.spritecollide(self,game.huskarl_group,True)
    
    def move(self):
        self.rect.x = self.rect.x + self.velocity_x
        self.rect.y = self.rect.y + self.velocity_y

    def check_border(self):
        if self.rect.x <0 or self.rect.x > WİDTH-35:
            self.velocity_x = self.velocity_x*-1
        if self.rect.y < 0 or self.rect.y > HEIGHT-35:
            self.velocity_y = self.velocity_y*-1

    def draw_teutonic(self):
        SCREEN.blit(self.teutonic_img,self.rect)

class MAIN:
    def __init__(self):
        self.SCALE= 35
        self.text_font =pygame.font.SysFont("Arial",45)

    
    def win_check(self):
        if len(self.huskarl_group.sprites())==0 and len(self.bowman_group.sprites())==0 :
            self.win_state("Teutonic")
        if len(self.huskarl_group.sprites())==0 and len(self.teutonic_group.sprites())==0:
            self.win_state("Longbowman")
        if len(self.bowman_group.sprites())==0 and len(self.teutonic_group.sprites())==0:
            self.win_state("Huskarl")

    def add_sprites(self):
        self.bowman_group = pygame.sprite.Group()
        self.huskarl_group = pygame.sprite.Group()
        self.teutonic_group = pygame.sprite.Group()

        for i in range(50):
            bowman = BOWMAN()
            self.bowman_group.add(bowman)
            
            huskarl = HUSKARL()
            self.huskarl_group.add(huskarl)

            teutonic = TEUTONIC()
            self.teutonic_group.add(teutonic)


    def check_event(self):

        #mouse pos
        mx,my = pygame.mouse.get_pos()

        click=False
        # check interaction 
        for event in pygame.event.get():
            # Quit 
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        # check collision
        # Check play button            
        if self.play_button.rect.collidepoint(mx,my):
            self.play_button.clicked()
            if click:                
                self.game_loop()

        if self.exit_button.rect.collidepoint(mx,my):
            self.exit_button.clicked()
            if click:
                pygame.quit()
                sys.exit()
            
    def main_menu(self):
        menu_bg = pygame.image.load("Graphics/Backgrounds/menu_bg.jpg").convert()
        menu_bg = pygame.transform.scale(menu_bg,(WİDTH,HEIGHT))
        while True:
             
            SCREEN.blit(menu_bg,(0,0))
            
            self.play_button = Button(WİDTH/2,(HEIGHT/2)-90,150,80,"Start",text_color=(250,250,250))
            self.play_button.draw()

            self.exit_button = Button((WİDTH/2),(HEIGHT/2),150,80,"Exit",(0,26,58))
            self.exit_button.draw()

            self.check_event()


            clock.tick(60)
            pygame.display.update()
                            
        
    def game_loop(self):
        self.add_sprites()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # SCREEN.fill()
            SCREEN.blit(background_img,(0,0))

            self.bowman_group.update()
            self.huskarl_group.update()
            self.teutonic_group.update()

            self.win_check()

            clock.tick(60)
            pygame.display.update()
       
    def win_state(self,winner=None):

        while True:
            
            

            #Background and Winner text        
            SCREEN.fill((125,125,125))

            text = self.text_font.render("winner "+ winner,True,(250,250,250))
            SCREEN.blit(text,(600,120))

            #show winner image
            # !!!!!!!!!!!!!!! Fix img load part !!!!!!!!!
            if winner == "Teutonic":
                self.teutonic_img = pygame.image.load("Graphics/Characters/teutonic_blue.png").convert_alpha()
                self.teutonic_img= pygame.transform.scale(self.teutonic_img,(100,100))
                SCREEN.blit(self.teutonic_img, (600,400))
            if winner == "Huskarl":
                self.huskarl_img = pygame.image.load("Graphics/Characters/huskarl_blue.png").convert_alpha()
                self.huskarl_img= pygame.transform.scale(self.huskarl_img,(100,100))
                SCREEN.blit(self.huskarl_img, (600,400))
            if winner == "Longbowman":
                self.bowman_img = pygame.image.load("Graphics/Characters/bowman_blue.png").convert_alpha()
                self.bowman_img= pygame.transform.scale(self.bowman_img,(100,100))
                SCREEN.blit(self.bowman_img, (600,400))
            
            

            #catch event
            for event in pygame.event.get():
                #quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #update and set FPS
            pygame.display.update()
            clock.tick(60)



class Button:
    def __init__(self,x,y,width,height,text="text",text_color=(255,255,255)):
        #set button background
        self.default_button = pygame.image.load("Graphics/Buttons/Default.png").convert()
        self.default_button = pygame.transform.scale(self.default_button,(width,height))
        self.rect = self.default_button.get_rect(center = (x,y))

        self.hover_button = pygame.image.load("Graphics/Buttons/Hover.png").convert()
        self.hover_button = pygame.transform.scale(self.hover_button,(width,height))
        
        #set Text
        self.text = TEXT_FONT.render(text,True,text_color)
        self.text_rect= self.text.get_rect(center=(x,y))

    def draw(self):

        #draw button
        SCREEN.blit(self.default_button,self.rect)
        SCREEN.blit(self.text,self.text_rect)

    def clicked(self):
        SCREEN.blit(self.hover_button,self.rect)
        SCREEN.blit(self.text,self.text_rect)


if __name__ == "__main__" :
    game =MAIN()
    game.main_menu()



