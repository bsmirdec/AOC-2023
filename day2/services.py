from objects import Games, Picks


def create_game(txt):
    """txt --> game"""
    game_txt = txt.split(":")
    game_id = int(game_txt[0].split()[-1])
    game_picks = game_txt[-1].split(";")
    game = Games(game_id=game_id)
    for i in range(len(game_picks)):
        game.add_pick(create_pick(game_picks[i], game_id, pick_id=i+1))
    return game


def create_pick(pick_txt, game_id, pick_id):
    red = 0
    green = 0
    blue = 0
    pick_list = pick_txt.split(",")
    for color in pick_list:
        number = color[1]
        if color[2].isdigit():
            number = number + color[2]
        number = int(number)
        if "red" in color:
            red = number
        elif "green" in color:
            green = number
        elif "blue" in color:
            blue = number
        else:
            print("erreur: le format n'est pas bon")
    pick = Picks(game_id=game_id, pick_id=pick_id, red=red, green=green, blue=blue)
    return pick


def validate_game_part1(game, bag):
    game = create_game(game)
    if game.is_valid_part1(bag):
        return game.game_id
    else:
        return 0


def power_game_part2(game):
    game = create_game(game)
    return game.power_part2()


Test = False

if Test:
    print(create_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
    print(validate_game_part1("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", (12, 13, 14)))
    print(validate_game_part1("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", (12, 13, 14)))
    print(validate_game_part1("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", (12, 13, 14)))
    print(validate_game_part1("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", (12, 13, 14)))
    print(validate_game_part1("Game 100: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", (12, 13, 14)))
    print(power_game_part2("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"))
    print(power_game_part2("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"))
    print(power_game_part2("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"))
    print(power_game_part2("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"))
    print(power_game_part2("Game 100: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
