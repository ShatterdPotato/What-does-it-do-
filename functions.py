import pygame

WIDTH, HEIGHT = 850, 575

def import_player(character_image,screen_display,character_rect):
    character = pygame.transform.scale(character_image,(character_rect.w,character_rect.h))
    screen_display.blit(character,(character_rect.x,character_rect.y))

def check_border(left, right, character_rect, max_width, max_depth):
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[right]:
        if character_rect.x + 5 < max_width:
            return True
    
    if keys_pressed[left]:
        if character_rect.x - 5 > 0:
            return True

def press_key():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("YO")

def gravity(up, character_rect):
    keys_pressed = pygame.key.get_pressed()
    if not keys_pressed[up]:
        gravity = 0
        if character_rect.bottom != 600:
            gravity += 5 
            character_rect.y += gravity
            if character_rect.bottom > 600:
                character_rect.bottom = 600

def character_movement(character, character_rect, left, right, up, down):
    key_pressed = pygame.key.get_pressed()

    if key_pressed[left] and check_border(left, right, character_rect, WIDTH, HEIGHT):
        character_rect.x -= 5
 
    if key_pressed[right] and check_border(left, right, character_rect, WIDTH, HEIGHT):
        character_rect.x += 5

    if key_pressed[pygame.K_r]:
        character_rect.y = 50

    if character_rect.bottom != 600:
        gravity(up, character_rect)

def jump(character_rect):
    gravity = 50
    character_rect.y -= gravity
    
    
   


