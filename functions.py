import pygame

def import_player(character_image,screen_display,character_rect):
    character = pygame.transform.scale(character_image,(character_rect.w,character_rect.h))
    screen_display.blit(character,(character_rect.x,character_rect.y))

def character_movement(character, character_rect, left, right, up, down):
    key_pressed = pygame.key.get_pressed()

    if key_pressed[left]:
        character_rect.x -= 5

    if key_pressed[right]:
        character_rect.x += 5

    if key_pressed[up]:
        character_rect.y -= 5

    if key_pressed[down]:
        character_rect.y += 5


