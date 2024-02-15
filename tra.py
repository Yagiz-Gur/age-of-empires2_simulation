import pygame,sys,random

scale=35  

pygame.init()
Width = 1280
Height = 800
screen = pygame.display.set_mode((Width,Height))
clock = pygame.time.Clock()

class HUSKARL(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x= random.randint(600,Width-500)
        self.y= random.randint(40,Height-660)
        
        self.huskarl_img = pygame.image.load("Graphics/huskarl.png").convert_alpha()
        self.huskarl_img= pygame.transform.scale(self.huskarl_img,(scale,scale))
        self.rect = self.huskarl_img.get_rect(topleft= (self.x,self.y))

        
    
        self.velocity_x = random.randint(1,1)* random.choice([-1,1])
        self.velocity_y = random.randint(1,1) * random.choice([-1,1])
          
    def update(self):
        self.move()
        self.check_border()
        self.draw_huskarl()
        self.collide()

    def collide(self):
        pygame.sprite.spritecollide(self,game.bowman_group,True)
    
    def draw_huskarl(self):
        screen.blit(self.huskarl_img,self.rect)


    def move(self):
        self.rect.x = self.rect.x + self.velocity_x
        self.rect.y = self.rect.y + self.velocity_y
        
    def check_border(self):
        #check vertical border
        if self.rect.x+scale > Width or self.rect.x < 0:
            self.velocity_x= self.velocity_x*-1
        #check horizanta border
        if self.rect.y+scale> Height or self.rect.y< 0:
            self.velocity_y= self.velocity_y*-1
        

class BOWMAN(pygame.sprite.Sprite):   
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x= random.randint(0,Width-scale)
        self.y= random.randint(0,Height-scale)
        
        self.bowman_img= pygame.image.load("Graphics/bowman.png").convert_alpha()
        self.bowman_img = pygame.transform.scale(self.bowman_img,(scale,scale))
        self.rect = self.bowman_img.get_rect(topleft= (self.x,self.y))

        
        
        self.velocity_x = random.randint(1,5)* random.choice([-1,1])
        self.velocity_y = random.randint(1,5) * random.choice([-1,1])

    def collide(self):
        pygame.sprite.spritecollide(self,game.teutonic_group,True)

          
    def update(self):
        self.move()
        self.check_border()
        self.draw_bowman()
        self.collide()
    
    def draw_bowman(self):
        screen.blit(self.bowman_img,self.rect)       

    def move(self):
        self.rect.x = self.rect.x + self.velocity_x
        self.rect.y = self.rect.y + self.velocity_y
        

    def check_border(self):
        #check vertical border
        if self.rect.x+scale > Width or self.rect.x < 0:
            self.velocity_x= self.velocity_x*-1
        #check horizanta border
        if self.rect.y+scale> Height or self.rect.y< 0:
            self.velocity_y= self.velocity_y*-1
    

class TEUTONIC(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.teutonic_img = pygame.image.load("Graphics/teutonic.png").convert_alpha()
        self.teutonic_img= pygame.transform.scale(self.teutonic_img,(scale,scale))

        self.x = random.randint(0,Width-scale)
        self.y = random.randint(0,Height-scale)

        self.rect = self.teutonic_img.get_rect(topleft= (self.x,self.y))

        self.velocity_x = random.randint(1,5)* random.choice([-1,1])
        self.velocity_y = random.randint(1,5) * random.choice([-1,1])

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
        if self.rect.x <0 or self.rect.x > Width-35:
            self.velocity_x = self.velocity_x*-1
        if self.rect.y < 0 or self.rect.y > Height-35:
            self.velocity_y = self.velocity_y*-1

    def draw_teutonic(self):
        screen.blit(self.teutonic_img,self.rect)


class MAIN:
    def __init__(self):
        self.scale= 35
        self.add_sprites()

    def add_sprites(self):
        self.bowman_group = pygame.sprite.Group()
        self.huskarl_group = pygame.sprite.Group()
        self.teutonic_group = pygame.sprite.Group()

        for i in range(10):
            bowman = BOWMAN()
            self.bowman_group.add(bowman)
            
            huskarl = HUSKARL()
            self.huskarl_group.add(huskarl)

            teutonic = TEUTONIC()
            self.teutonic_group.add(teutonic)

    def main_menu(self):
        menu_bg = pygame.image.load("Graphics/menu_bg.png").convert()
        menu_bg = pygame.transform.scale(menu_bg,(Width,Height))
        while True:
             
            screen.blit(menu_bg,(0,0))

            #create buttons and Text
            text_font = pygame.font.SysFont("Arial",45)
            text = text_font.render("Start",True,(250,250,250))
            

            button_1 = pygame.Rect((Width/2)-100,200,200,80)
            button_2 = pygame.Rect((Width/2)-100,300,200,80)
            
            pygame.draw.rect(screen,(125,125,125),button_1)
            pygame.draw.rect(screen,(125,125,125),button_2)

            screen.blit(text,(600,210))
            
            #catch mouse pos
            mx,my = pygame.mouse.get_pos()
            

            #collision
            if button_1.collidepoint(mx,my):
                if click:
                    print("clicked")
                    self.game_loop()

            if button_2.collidepoint(mx,my):
                if click:
                    pygame.quit()
                    sys.exit()
            
            #catch event
            click = False 
            for event in pygame.event.get():
                #quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click=True    
                       
                
            clock.tick(60)
            pygame.display.update()
              
        


                
    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # screen.fill()
            screen.blit(background_img,(0,0))

            self.bowman_group.update()
            self.huskarl_group.update()
            self.teutonic_group.update()

            clock.tick(60)
            pygame.display.update()



    
background_img = pygame.image.load("Graphics/background.png").convert()
background_img = pygame.transform.scale(background_img,(Width,Height))


def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))


     
game =MAIN()
game.main_menu()



