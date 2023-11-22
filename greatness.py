from functions import *
import pygame
import os

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PLACEHOLDER FOR CAPTIONS LATER")

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main() 
test_run()
test_run_2()
