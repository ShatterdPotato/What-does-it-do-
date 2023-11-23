import pygame

def import_player(character_image,screen_display,character_rect):
    character = pygame.transform.scale(character_image,(character_rect.w,character_rect.h))
    screen_display.blit(character,(character_rect.x,character_rect.y))

def check_border(character_rect, max_width, max_depth):
    if character_rect.x + 5 < max_witdh:
        return True
    if character_rect.x - 5 > 0:
        return True
    if character_rect.y + 5 < max_depth:
        return True
    if character_rect.y - 5 > 0:
        return True

def character_movement(character, character_rect, left, right, up, down):
    key_pressed = pygame.key.get_pressed()

    if key_pressed[left]:
        check_border(character_rect, WIDTH, HEIGHT)
        character_rect.x -= 5

    if key_pressed[right]:
        check_border(character_rect, WIDTH, HEIGHT)
        character_rect.x += 5

    if key_pressed[up]:
        check_border(character_rect, WIDTH, HEIGHT)
        character_rect.y -= 5

    if key_pressed[down]:
        check_border(character_rect, WIDTH, HEIGHT)
        character_rect.y += 5


