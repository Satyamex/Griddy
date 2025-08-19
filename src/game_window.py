import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 420))
game_clock = pygame.time.Clock()
game_running = True

while game_running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # fill the screen with a color to wipe away anything from last frame


    # RENDER YOUR GAME HERE


    # flip() the display to put your work on screen
    pygame.display.flip()
    game_clock.tick(60)  # limits FPS to 60

pygame.quit()