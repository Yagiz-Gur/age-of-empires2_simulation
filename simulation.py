import pygame,sys,random


pygame.init()
WİDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode((WİDTH,HEIGHT))
clock = pygame.time.Clock()

#define SCALE and max,min Speed
SCALE=35  
MAX_SPEED=5
pygame.font.init()
TEXT_FONT = pygame.font.SysFont("Arial",35)
#Spawn Setting
TOP_SPAWN_AREA = [WİDTH/4, 2*(WİDTH/4), 0, HEIGHT/4]
RIGHT_SPAWN_AREA = [0,WİDTH/4,HEIGHT/4,3*(HEIGHT/4)]
LEFT_SPAWN_AREA = [3*(WİDTH/4),WİDTH-SCALE,3*(HEIGHT/4),3*(HEIGHT/4)]


#mouse



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
        if game.follow:
            self.chase()

    def collide(self):
        if game.conversion:
            if (pygame.sprite.spritecollide(self,game.bowman_group,False)):
                collided_items = pygame.sprite.spritecollide(self,game.bowman_group,True)    

                huskarl = HUSKARL()
                huskarl.rect =huskarl.huskarl_img.get_rect(center = (collided_items[0].rect.x,collided_items[0].rect.y))
                game.huskarl_group.add(huskarl)
        else:
            (pygame.sprite.spritecollide(self,game.bowman_group,True))
        
    
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

    def chase(self):
        if len(game.bowman_group.sprites()) !=0:
            enemy = min([e for e in game.bowman_group.sprites()], key=lambda e: pow(e.rect.x - self.rect.x, 2) + pow(e.rect.y-self.rect.y, 2))
            pygame.draw.line(SCREEN,(255,0,0),(self.rect.x,self.rect.y), (enemy.rect.x,enemy.rect.y))
            self.velocity_x = ((enemy.rect.x - self.rect.x)/(abs((enemy.rect.x - self.rect.x))+0.1))* random.randint(1,MAX_SPEED)
            self.velocity_y = ((enemy.rect.y - self.rect.y)/(abs((enemy.rect.y - self.rect.y))+0.1))* random.randint(1,MAX_SPEED)

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
        if game.conversion:
            if (pygame.sprite.spritecollide(self,game.teutonic_group,False)):
                collided_items = pygame.sprite.spritecollide(self,game.teutonic_group,True)

                bowman = BOWMAN()
                bowman.rect = bowman.bowman_img.get_rect(center = (collided_items[0].rect.x,collided_items[0].rect.y))
                game.bowman_group.add(bowman)
        else:
            pygame.sprite.spritecollide(self,game.teutonic_group,True)


    def update(self):
        self.move()
        self.check_border()
        self.draw_bowman()
        self.collide()
        if game.follow:
            self.chase()
    
    def draw_bowman(self):
        SCREEN.blit(self.bowman_img,self.rect)       

    def move(self):
        print("df")
        self.rect.x = self.rect.x + self.velocity_x
        self.rect.y = self.rect.y + self.velocity_y
        

    def check_border(self):
        #check vertical border
        if self.rect.x+SCALE > WİDTH or self.rect.x < 0:
            self.velocity_x= self.velocity_x*-1
        #check horizanta border
        if self.rect.y+SCALE> HEIGHT or self.rect.y< 0:
            self.velocity_y= self.velocity_y*-1

    def chase(self):
        if len(game.teutonic_group.sprites()) !=0:
            enemy = min([e for e in game.teutonic_group.sprites()], key=lambda e: pow(e.rect.x - self.rect.x, 2) + pow(e.rect.y-self.rect.y, 2))
            pygame.draw.line(SCREEN,(255,0,0),(self.rect.x,self.rect.y), (enemy.rect.x,enemy.rect.y))
            self.velocity_x = ((enemy.rect.x - self.rect.x)/(abs((enemy.rect.x - self.rect.x))+0.1))* random.randint(1,MAX_SPEED)
            self.velocity_y = ((enemy.rect.y - self.rect.y)/(abs((enemy.rect.y - self.rect.y))+0.1))* random.randint(1,MAX_SPEED)

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
        if game.follow:
            self.chase()

    def collision(self):
        if game.conversion:
            if (pygame.sprite.spritecollide(self,game.huskarl_group,False)):
                collided_items = pygame.sprite.spritecollide(self,game.huskarl_group,True)

                teutonic = TEUTONIC()
                teutonic.rect = teutonic.teutonic_img.get_rect(center = (collided_items[0].rect.x,collided_items[0].rect.y))
                game.teutonic_group.add(teutonic)
        else:
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
    
    def chase(self):
        # !!!! ADD -> Check whether game.bowman_groups is empty or not
        if len(game.huskarl_group.sprites())!= 0:
            enemy = min([e for e in game.huskarl_group.sprites()], key=lambda e: pow(e.rect.x - self.rect.x, 2) + pow(e.rect.y-self.rect.y, 2))
            pygame.draw.line(SCREEN,(255,0,0),(self.rect.x,self.rect.y), (enemy.rect.x,enemy.rect.y))
            self.velocity_x = ((enemy.rect.x - self.rect.x)/(abs((enemy.rect.x - self.rect.x))+0.1))* random.randint(1,MAX_SPEED)
            self.velocity_y = ((enemy.rect.y - self.rect.y)/(abs((enemy.rect.y - self.rect.y))+0.1))* random.randint(1,MAX_SPEED)


class MAIN:
    def __init__(self):
        self.SCALE= 35
        self.text_font =pygame.font.SysFont("Arial",45)
        self.paused = False
        #Game options
        self.follow= False
        self.conversion = False

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


    def main_win_events(self):

        #mouse pos
        
        self.Mx, self.My = pygame.mouse.get_pos()
        self.click=False
        # check interaction 
        for event in pygame.event.get():
            # Quit 
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            


    def game_loop_event(self):

        #mouse pos
        self.Mx, self.My = pygame.mouse.get_pos()
        self.click=False
        
        
        # check interaction 
        for event in pygame.event.get():
            # Quit 
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.paused:
                        print("cont")
                        self.paused=False 
                    else:
                        self.paused =True
                        self.pause_menu()
    def main_menu(self):
        menu_bg = pygame.image.load("Graphics/Backgrounds/menu_bg.jpg").convert()
        menu_bg = pygame.transform.scale(menu_bg,(WİDTH,HEIGHT))
        while True:

            SCREEN.blit(menu_bg,(0,0))
            self.main_win_events()
            # -- Set button
            # Play Button
            self.play_button = Button(WİDTH/2,(HEIGHT/2)-90,150,80,"Start",text_color=(0,25,50))
            self.play_button.draw()
            
            #Exit button
            self.exit_button = Button((WİDTH/2),(HEIGHT/2)+90,150,80,"Exit",(0,25,50))
            self.exit_button.draw()

            #Optinons conversion
            self.conversion_button = Button((WİDTH/2)-85,(HEIGHT/2),150,80,"Convert",(0,25,50))
            self.conversion_button.draw()

            if self.conversion_button.is_clicked():
                if self.conversion:
                    self.conversion = False
                else:
                    self.conversion =True
            #Options follow
            self.follow_button = Button((WİDTH/2)+85,(HEIGHT/2),150,80,"Follow",(0,25,50))
            self.follow_button.draw()

            if self.follow_button.is_clicked():
                if self.follow:
                    self.follow = False
                    print("true")
                else:
                    self.follow = True
                    print("false")



            # -- Set button action

            #play button
            if (self.play_button.is_clicked()):
                self.game_loop()
            #exit button
            if self.exit_button.is_clicked():
                pygame.quit()
                sys.exit()


            clock.tick(60)
            pygame.display.update()
                            
        
    def game_loop(self):
        self.add_sprites()
        while True:
            self.game_loop_event()
            if self.paused:
                self.pause_menu()

            else:
                
                
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
            self.main_win_events()

            #show winner image
            # !!!!!!!!!!!!!!! Fix img load part !!!!!!!!!
            if winner == "Teutonic":
                self.winner_img = pygame.image.load("Graphics/Characters/teutonic_blue.png").convert_alpha()
                
                
            if winner == "Huskarl":
                self.winner_img = pygame.image.load("Graphics/Characters/huskarl_blue.png").convert_alpha()
                
                
            if winner == "Longbowman":
                self.winner_img = pygame.image.load("Graphics/Characters/bowman_blue.png").convert_alpha()

            #winner İmage   
            self.winner_img= pygame.transform.scale(self.winner_img,(SCALE*5,SCALE*5))    
            img_rectangle = self.winner_img.get_rect(center = ((WİDTH/2,HEIGHT/2)))
            

            SCREEN.blit(self.winner_img, img_rectangle)
            pygame.draw.rect(SCREEN, (25,20,220),img_rectangle,5,10)
            text = self.text_font.render("Winner "+ winner,True,(250,250,250))
            text_rectangle = text.get_rect(center =((WİDTH/2,(HEIGHT/2)-SCALE*5)))

            # BUTTON
            self.back2menu = Button(WİDTH/10,HEIGHT/10,185,80,"Back to Menu")
            self.back2menu.draw()
            self.exit_button = Button(WİDTH/10,HEIGHT/10+150,185,80,"Exit")
            self.exit_button.draw()

            if self.back2menu.is_clicked():
                self.main_menu()
            if self.exit_button.is_clicked():
                pygame.quit()
                sys.exit()

            SCREEN.blit(self.winner_img, img_rectangle)

           #catch event
            for event in pygame.event.get():
                #quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #update and set FPS
            pygame.display.update()
            clock.tick(60)

    def pause_menu(self):

        #Create Transparent Grey rectangle on Background
        surface = pygame.Surface((WİDTH,HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surface,(120,120,120,10),[0,0,WİDTH,HEIGHT])
        SCREEN.blit(surface,(0,0))  

        #Buttons

        #Resume button
        resume_button = Button((WİDTH/2)-180,(HEIGHT/2),150,80,"Resume")
        resume_button.draw()
        if resume_button.is_clicked():
            self.paused =0
        
        #Exit button
        exit_button = Button((WİDTH/2),(HEIGHT/2),180,80,"Back to Menu")
        exit_button.draw()
        if exit_button.is_clicked():
            self.paused =0
            self.main_menu()

        #Restart Button 
        restart_button = Button((WİDTH/2+200),(HEIGHT/2),180,80,"Restart")
        restart_button.draw()
        if restart_button.is_clicked():
            self.paused=False
            self.game_loop()

        #text
        #Huskarl
        num_huskarl = len(game.huskarl_group.sprites())
        huskarl_numbers = TEXT_FONT.render(f"Number of Huskarl: {num_huskarl}",True,(255,0,0) )
        SCREEN.blit(huskarl_numbers,[25,25,50,50])
        #Bowman
        num_bowman = len(game.bowman_group.sprites())
        bowman_numbers =TEXT_FONT.render(f"Number of Bowman: {num_bowman}",False,(255,0,0))
        SCREEN.blit(bowman_numbers,[25,60,0,0])
        #Teutonic
        num_teutonic = len(game.teutonic_group.sprites())
        teutonic_numbers = TEXT_FONT.render(f"Number of Teutonic: {num_teutonic}",True,(255,2,0))
        SCREEN.blit(teutonic_numbers,[25,95,0,0])



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

    def is_over(self):
        SCREEN.blit(self.hover_button,self.rect)
        SCREEN.blit(self.text,self.text_rect)

    def is_clicked(self):
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint(mx,my):
            self.is_over()
            if game.click:
                return 1
            
if __name__ == "__main__" :
    game =MAIN()
    game.main_menu()



