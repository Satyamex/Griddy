import player

plyr: player = player.player(0, 0)

def snap_according_to_game_grid(n) -> int:
    return round(n / plyr.player_speed) * plyr.player_speed