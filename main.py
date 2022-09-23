import pygame
import os
import random


WIDTH, HEIGHT = 900, 500
# creating window and setting dimensions
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BLUE = (13, 35, 131)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

SPACE = pygame.image.load(os.path.join('Assets', 'space.jpg'))
SPACESHIP = pygame.image.load(
    os.path.join('Assets', 'spaceship.png'))
SPACESHIP = pygame.transform.scale(SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
ENEMY = pygame.image.load(
    os.path.join('Assets', 'enemy_spaceship.png'))
ENEMY = pygame.transform.scale(ENEMY, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))


# creating the game loop, constantly refreshing the window

FPS = 60
VEL = 5
SHIP_WIDTH, SHIP_HEIGHT = 55, 40
ENEMY_POS = random.randint(100, 800)
ENEMY_WIDTH, ENEMY_HEIGHT = ENEMY_POS, 0
ENEMY_VEL = 1
MAX_ENEMIES = 10
VEL = 5


def draw_window(spaceship, enemies):
    WINDOW.blit(SPACE, (0, 0))

    for i in enemies:
        WINDOW.blit(ENEMY, (i.x, i.y))
    WINDOW.blit(SPACESHIP, (spaceship.x, spaceship.y))

    pygame.display.update()


def handle_movement(keys_pressed, space, enemy):
    if keys_pressed[pygame.K_LEFT] and space.x - VEL > 0:
        space.x -= VEL
    elif keys_pressed[pygame.K_RIGHT] and space.x + VEL < WIDTH - 50:
        space.x += VEL
    for i in enemy:
        i.y += ENEMY_VEL


def main():
    spaceship = pygame.Rect(WIDTH/2, 450, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    enemies = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():  # checks for events occurring in pygame
            if event.type == pygame.QUIT:
                run = False
        if len(enemies) < MAX_ENEMIES:
            pos = random.randint(100, 800)
            enemy = pygame.Rect(pos, ENEMY_HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
            enemies.append(enemy)
        draw_window(spaceship, enemies)
        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed, spaceship, enemies)

    pygame.quit()


if __name__ == "__main__":
    main()
