class player:
    def __init__(self, SCREEN_WIDTH: float, SCREEN_HEIGHT: float):
        self.player_color = (255, 255, 255)
        self.player_scale_x = 100
        self.player_scale_y = 100
        self.player_pos_x = (SCREEN_WIDTH - self.player_scale_x) / 2
        self.player_pos_y = (SCREEN_HEIGHT - self.player_scale_y) / 2
        self.player_speed = 50

    def move_player_from_input(self, input: str):
            if input == "w":
                self.player_pos_y -= 1 * self.player_speed
            elif input == "s":
                self.player_pos_y += 1 * self.player_speed
            elif input == "d":
                self.player_pos_x += 1 * self.player_speed
            elif input == "a":
                self.player_pos_x -= 1 * self.player_speed