import pygame, player as player_class, random, score_point as scorepoint, score_point_spawner, utilities

# pygame setup
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 420

LIMIT_OFFSET = 10
X_LIMIT_MIN = 0 + LIMIT_OFFSET
X_LIMIT_MAX = 600 - LIMIT_OFFSET
Y_LIMIT_MIN = 0 + LIMIT_OFFSET
Y_LIMIT_MAX = 380 - LIMIT_OFFSET

x_rand_pos = random.randint(X_LIMIT_MIN, X_LIMIT_MAX)
y_rand_pos = random.randint(Y_LIMIT_MIN, Y_LIMIT_MAX)
x_rand_pos = utilities.snap_according_to_game_grid(x_rand_pos)
y_rand_pos = utilities.snap_according_to_game_grid(y_rand_pos)

pygame.display.set_caption("Griddy!")
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_clock = pygame.time.Clock()
game_running = True

# instancing shit
player_instanced = player_class.player(SCREEN_WIDTH, SCREEN_HEIGHT)
score_point = scorepoint.score_point()

while game_running:

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player_instanced.player_pos_y >= Y_LIMIT_MIN:
                player_instanced.move_player_from_input("w")
            elif event.key == pygame.K_s and player_instanced.player_pos_y <= Y_LIMIT_MAX:
                player_instanced.move_player_from_input("s")
            elif event.key == pygame.K_d and player_instanced.player_pos_x <= X_LIMIT_MAX:
                player_instanced.move_player_from_input("d")
            elif event.key == pygame.K_a  and player_instanced.player_pos_x >= X_LIMIT_MIN:
                player_instanced.move_player_from_input("a")

    # fill the screen with a color to wipe away anything from last frame
    game_screen.fill((0, 0, 0))

    # RENDER YOUR GAME HERE
    player = pygame.draw.rect(game_screen, player_instanced.player_color, (player_instanced.player_pos_x, player_instanced.player_pos_y, player_instanced.player_scale_x, player_instanced.player_scale_y))
    pygame.draw.rect(game_screen, score_point.color, (x_rand_pos, y_rand_pos, score_point.scale_x, score_point.scale_y))

    # Debug
    # print(player_instanced.player_pos_x)

    # flip() the display to put your work on screen
    pygame.display.flip()
    game_clock.tick(12)  # limits FPS to 12

pygame.quit()