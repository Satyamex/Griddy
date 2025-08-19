import pygame

# pygame setup
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 420

game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_clock = pygame.time.Clock()
game_running = True

# fields
player_color = (255, 255, 255)
player_scale_x = 100
player_scale_y = 100
player_defpostion_x = (SCREEN_WIDTH - player_scale_x) / 2
player_defpostion_y = (SCREEN_HEIGHT - player_scale_y) / 2
player_pos_x = player_defpostion_x
player_pos_y = player_defpostion_y
player_speed = 50

while game_running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_pos_y -= 1 * player_speed
            if event.key == pygame.K_s:
                player_pos_y += 1 * player_speed
            if event.key == pygame.K_d:
                player_pos_x += 1 * player_speed
            if event.key == pygame.K_a:
                player_pos_x -= 1 * player_speed


    # fill the screen with a color to wipe away anything from last frame
    game_screen.fill((0, 0, 0))

    # RENDER YOUR GAME HERE
    player = pygame.draw.rect(game_screen, player_color, (player_pos_x, player_pos_y, player_scale_x, player_scale_y))

    # flip() the display to put your work on screen
    pygame.display.flip()
    game_clock.tick(60)  # limits FPS to 60

pygame.quit()