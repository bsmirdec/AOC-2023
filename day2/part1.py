from services import validate_game

with open("day2/games.txt", "r") as games:
    gamelist = games.readlines()

    bag = (12, 13, 14)
    total = 0

    for game in gamelist:
        total += validate_game(game, bag)

print("total final : ", total)