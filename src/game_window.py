import pygame, player as player_class, score_point as scorepoint, utilities, random

# pygame setup
pygame.init()

SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 420

LIMIT_OFFSET: int = 10
X_LIMIT_MIN: int = 0 + LIMIT_OFFSET
X_LIMIT_MAX: int = 600 - LIMIT_OFFSET
Y_LIMIT_MIN: int = 0 + LIMIT_OFFSET
Y_LIMIT_MAX: int = 380 - LIMIT_OFFSET

score_point_xpos: int = 0
score_point_ypos: int = 0

pygame.display.set_caption("Griddy!")
game_screen: pygame.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_clock: pygame.time = pygame.time.Clock()
game_running: bool = True

# instancing stuff
player_instanced: player_class = player_class.player(SCREEN_WIDTH, SCREEN_HEIGHT)
score_point: scorepoint = scorepoint.score_point()

# Temp utilities
def get_random_score_position_x() -> None:
    global score_point_xpos
    x_rand_pos: int = random.randint(X_LIMIT_MIN, X_LIMIT_MAX)
    x_rand_pos: int = utilities.snap_according_to_game_grid(x_rand_pos)
    score_point_xpos = x_rand_pos

def get_random_score_position_y() -> None:
    global score_point_ypos
    y_rand_pos: int = random.randint(Y_LIMIT_MIN, Y_LIMIT_MAX)
    y_rand_pos: int = utilities.snap_according_to_game_grid(y_rand_pos)
    score_point_ypos = y_rand_pos

get_random_score_position_x()
get_random_score_position_y()

while game_running:

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and player_instanced.player_pos_y >= Y_LIMIT_MIN:
                player_instanced.move_player_from_input("w")
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and player_instanced.player_pos_y <= Y_LIMIT_MAX:
                player_instanced.move_player_from_input("s")
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and player_instanced.player_pos_x <= X_LIMIT_MAX:
                player_instanced.move_player_from_input("d")
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and player_instanced.player_pos_x >= X_LIMIT_MIN:
                player_instanced.move_player_from_input("a")

    # fill the screen with a color to wipe away anything from last frame
    game_screen.fill((28, 28, 28))

    # PRE_RENDER setup
    player_to_spawn: tuple = (player_instanced.player_pos_x, player_instanced.player_pos_y, player_instanced.player_scale_x, player_instanced.player_scale_y)
    score_point_to_spawn: tuple = (score_point_xpos, score_point_ypos, score_point.scale_x, score_point.scale_y)
    score_text_font: pygame.font = pygame.font.Font(None, 60)
    score_text_surface: pygame.surface = score_text_font.render(str(player_instanced.score), True, (255, 255, 255))
    score_text_rect: pygame.rect = score_text_surface.get_rect(center=(40, 40)) 

    # RENDER YOUR GAME HERE
    player_spawned: pygame.draw = pygame.draw.rect(game_screen, player_instanced.player_color, player_to_spawn)
    score_point_spawned: pygame.draw = pygame.draw.rect(game_screen, score_point.color, score_point_to_spawn)
    game_screen.blit(score_text_surface, score_text_rect)

    # Collision detection
    if player_spawned.colliderect(score_point_spawned):
        player_instanced.increase_score()
        get_random_score_position_x()
        get_random_score_position_y()

    # Debug
    # print(player_instanced.player_pos_x)

    # flip() the display to put your work on screen
    pygame.display.flip()
    game_clock.tick(24)  # limits FPS to 24 frames per second

pygame.quit()