import pygame


WİDTH = 1280
HEIGHT = 720
SCALE=35  
MAX_SPEED=5

TOP_SPAWN_AREA = [WİDTH/4, 2*(WİDTH/4), 0, HEIGHT/4]
RIGHT_SPAWN_AREA = [0,WİDTH/4,HEIGHT/4,3*(HEIGHT/4)]
LEFT_SPAWN_AREA = [3*(WİDTH/4),WİDTH-SCALE,3*(HEIGHT/4),3*(HEIGHT/4)]


pygame.init()

SCREEN = pygame.display.set_mode((WİDTH,HEIGHT))
pygame.display.set_caption("AoE2 Simulation")
clock = pygame.time.Clock()

#define SCALE and max,min Speed

pygame.font.init()
TEXT_FONT = pygame.font.SysFont("Arial",35)



#Music Setting  
pygame.mixer.init()
pygame.mixer.music.load("Sounds/theme.mp3")
pygame.mixer.music.play(loops=0,start=10,fade_ms=50000)

background_img = pygame.image.load("Graphics/Backgrounds/background.png").convert()
background_img = pygame.transform.scale(background_img,(WİDTH,HEIGHT))