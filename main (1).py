import math

import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

play_button_img = pygame.image.load('start.png')
quit_button_img = pygame.image.load('exit.png')
options_button = pygame.image.load('option.png')

def move_player(player_rect, speed):
    mouse_pos = pygame.mouse.get_pos()
    x_diff = mouse_pos[0] - player_rect.x
    y_diff = mouse_pos[1] - player_rect.y
    distance = math.sqrt(x_diff**2 + y_diff**2)

    if distance > 0:
        player_rect.x += (x_diff / distance) * speed
        player_rect.y += (y_diff / distance) * speed

    return player_rect
def move_mob(mob):
    mob_image, mob_rect, mob_speed, mob_direction = mob
    mob_rect.x += mob_speed * mob_direction

    if mob_rect.left < 0 or mob_rect.right > 800:
        mob_direction = -mob_direction

    return mob_image, mob_rect, mob_speed, mob_direction

def game_screen():
    mobs = []
    mob_spawn_time = 1000  # время между появлениями мобов в миллисекундах
    mob_spawn_timer = 0
    desert_color = (139, 69, 19)
    player_image = pygame.image.load('prsonag2.png')
    player_image = pygame.transform.scale(player_image, (60, 70))
    player_rect = player_image.get_rect(topleft=(350, 450))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(desert_color)

        player_rect = move_player(player_rect, 5)

        for mob in mobs:
            mob_image, mob_rect, mob_speed, mob_direction = move_mob(mob)
            screen.blit(mob_image, mob_rect)

        screen.blit(player_image, player_rect)

        pygame.display.update()

        clock = pygame.time.Clock()
        clock.tick(30)

        mob_spawn_timer += clock.get_time()
        if mob_spawn_timer >= mob_spawn_time:
            mobs.append(create_mob())
            mob_spawn_timer = 0

        for mob in mobs:
            mob_image, mob_rect, mob_speed, mob_direction = move_mob(mob)
            if mob_rect.colliderect(player_rect):
                mobs.remove(mob)

def create_mob():
    mob_image = pygame.image.load('mob_pixian_ai.png')
    mob_image = pygame.transform.scale(mob_image, (50, 50))
    mob_rect = mob_image.get_rect(topleft=(random.randint(0, 800), random.randint(0, 600)))
    mob_speed = random.randint(1, 5)
    mob_direction = random.choice([-1, 1])
    return mob_image, mob_rect, mob_speed, mob_direction

def main_menu():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                play_button_rect = play_button_img.get_rect(topleft=(310, 300))
                quit_button_rect = quit_button_img.get_rect(topleft=(300, 430))
                options_button_rect = options_button.get_rect(topleft=(280, 360))
                if play_button_rect.collidepoint(mouse_pos):
                    game_screen()

        screen.fill((255, 255, 255))
        screen.blit(play_button_img, (310, 300))
        screen.blit(quit_button_img, (300, 430))
        screen.blit(options_button, (280, 360))

        pygame.display.update()
        clock.tick(30)

main_menu()