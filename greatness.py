from functions import *
import pygame
import os

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PLACEHOLDER FOR CAPTIONS LATER")

FPS = 60
WHITE = (255, 255, 255)

#Characters here
player_width, player_height = 55,100
derp_dude = pygame.image.load(os.path.join('Assets', 'derp_dude.png'))
rage_dude = pygame.image.load(os.path.join('Assets', 'rage_dude.png'))
derp_dude_rect = pygame.Rect(100, 300, player_width, player_height)
rage_dude_rect = pygame.Rect(100, 300, player_width, player_height)


def draw_update():
    WIN.fill(WHITE)
    import_player(derp_dude, WIN, derp_dude_rect)
    import_player(rage_dude, WIN, rage_dude_rect)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            while event.type == pygame.KEYDOWN:
                if rage_dude_rect.bottom == 600:
                    if event.key == pygame.K_w:
                        gravity(pygame.K_w, rage_dude_rect)
                        jump(rage_dude_rect)
                    
        character_movement(derp_dude, derp_dude_rect, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        character_movement(rage_dude, rage_dude_rect, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        draw_update()
        
main() 
