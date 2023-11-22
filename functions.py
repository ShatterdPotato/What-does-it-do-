import pygame

def import_player(character_image,screen_display):
    character = pygame.transform.scale(character_image,(55,100))
    screen_display.blit(character,(300,300))
