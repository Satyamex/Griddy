class player:

    def __init__(self, SCREEN_WIDTH: float, SCREEN_HEIGHT: float) -> None:
        self.player_color: tuple = (12, 201, 183)
        self.player_scale_x: int = 40
        self.player_scale_y: int = 40
        self.player_pos_x: int = (SCREEN_WIDTH - self.player_scale_x) / 2
        self.player_pos_y: int = (SCREEN_HEIGHT - self.player_scale_y) / 2
        self.player_speed: int = 10
        self.player_snap: int = self.player_speed
        self.score: int = 0

    def move_player_from_input(self, input: str) -> None:
            if input == "w":
                self.player_pos_y -= 1 * self.player_speed
            elif input == "s":
                self.player_pos_y += 1 * self.player_speed
            elif input == "d":
                self.player_pos_x += 1 * self.player_speed
            elif input == "a":
                self.player_pos_x -= 1 * self.player_speed
    
    def increase_score(self) -> None:
         self.score += 1
         # print(self.score)