from functions import *
import pygame
import os

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PLACEHOLDER FOR CAPTIONS LATER")
FPS = 60
WHITE = (255, 255, 255)

#Characters here
derp_dude = pygame.image.load(os.path.join('Assets', 'derp_dude.png'))
rage_dude = pygame.image.load(os.path.join('Assets', 'rage_dude.png'))

def draw_update():
    WIN.fill(WHITE)
    import_player(derp_dude, WIN)
    import_player(rage_dude, WIN)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_update()

main() 
