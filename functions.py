import pygame

WIDTH, HEIGHT = 900, 600


def import_player(character_image, screen_display, character_rect):
    character = pygame.transform.scale(
        character_image, (character_rect.w, character_rect.h))
    screen_display.blit(character, (character_rect.x, character_rect.y))


def check_border(left, right, up, character_rect, max_width, max_depth):
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[right]:
        if character_rect.right + 5 < max_width:
            return True
        else:
            return False

    if keys_pressed[left]:
        if character_rect.left - 5 > 0:
            return True
        else:
            return False

    if keys_pressed[up]:
        if character_rect.top - 5 > 0:
            return True
        else:
            return False


def press_key():

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("YO")


def character_movement(character, character_rect, left, right, up, down, HEIGHT, velocity, jumping):
    key_pressed = pygame.key.get_pressed()

    def gravity(character_rect, HEIGHT, GRAVITY, velocity):
        if character_rect.bottom < HEIGHT:
            character_rect.y += velocity

            return velocity + GRAVITY

        if character_rect.y != HEIGHT:
            character_rect.bottom = HEIGHT

    if not key_pressed[up]:
        velocity = gravity(character_rect, HEIGHT, .25, velocity)

    else:
        velocity = 0

    if key_pressed[left] and check_border(left, right, up, character_rect, WIDTH, HEIGHT):
        character_rect.x -= 5

    if key_pressed[right] and check_border(left, right, up, character_rect, WIDTH, HEIGHT):
        character_rect.x += 5

    if key_pressed[up] and check_border(left, right, up, character_rect, WIDTH, HEIGHT) and jumping:
        character_rect.y -= 15

    return velocity
