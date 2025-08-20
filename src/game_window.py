import pygame, player as player_class

# pygame setup
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 420
X_LIMIT = (0, 600)
Y_LIMIT = (0, 380)

game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_clock = pygame.time.Clock()
game_running = True

# instancing shit
player_instanced = player_class.player(SCREEN_WIDTH, SCREEN_HEIGHT)

while game_running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_instanced.move_player_from_input("w")
            elif event.key == pygame.K_s:
                player_instanced.move_player_from_input("s")
            elif event.key == pygame.K_d:
                player_instanced.move_player_from_input("d")
            elif event.key == pygame.K_a:
                player_instanced.move_player_from_input("a")


    # fill the screen with a color to wipe away anything from last frame
    game_screen.fill((0, 0, 0))

    # RENDER YOUR GAME HERE
    player = pygame.draw.rect(game_screen, player_instanced.player_color, (player_instanced.player_pos_x, player_instanced.player_pos_y, player_instanced.player_scale_x, player_instanced.player_scale_y))

    #Debug
    print(player_instanced.player_pos_x)

    # flip() the display to put your work on screen
    pygame.display.flip()
    game_clock.tick(12)  # limits FPS to 60

pygame.quit()