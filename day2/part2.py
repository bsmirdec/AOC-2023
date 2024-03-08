from services import power_game_part2

with open("day2/games.txt", "r") as games:
    gamelist = games.readlines()

    total = 0

    for game in gamelist:
        total += power_game_part2(game)

print("total final : ", total)
