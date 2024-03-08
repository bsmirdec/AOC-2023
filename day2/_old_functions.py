def segmentate_game(game):
    """
    str -> (int, list)
    segmentate_game("Game 88: 3 blue, 9 green, 3 red; 2 blue, 15 green; 2 red, 9 green") == (88, [[" 3 blue", " 9 green", " 3 red"], [" 2 blue", " 15 green"], [" 2 red", " 9 green"]])
    """
    picks = []
    x = game.split(":")
    game_id = int(x[0].split()[-1])
    game_picks = x[-1].split(";")
    for pick in game_picks:
        segmented_pick = pick.split(",")
        picks.append(segmented_pick)

    return (game_id, picks)


def sort_pick(pick):
    """
    sort one picking into a tuple (red, green, blue)
    list -> tuple

    sort_pick([" 3 blue, 9 green, 3 red"]) == (3, 9, 3)
    sort_pick([" 2 red, 9 green"]) == (2, 9, 0)
    """
    red = 0
    green = 0
    blue = 0
    for color in pick:
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
    return (red, green, blue)


def format_game(game):
    """str -> list
    translate a game into a specific format
    game = (int, (red, green, blue), (red, green, blue), (red, green, blue))

    format_game("Game 88: 3 blue, 9 green, 3 red; 2 blue, 15 green; 2 red, 9 green") == [88, (3, 9, 3), (0, 15, 2), (2, 9, 0)]
    """
    segmentated_game = segmentate_game(game)
    picks = segmentated_game[1]
    formated_game = [segmentated_game[0]]
    for pick in picks:
        formated_game.append(sort_pick(pick))
    return formated_game


def validate_game(game, bag):
    """
    validate if the maximum number of a color is not superior to the number in the bag set
    should return the id number if ok, and 0 if not possible
    str, tuple -> int

    validate_game("Game 88: 3 blue, 9 green, 3 red; 2 blue, 15 green; 2 red, 9 green", (12, 13, 14)) == 0
    validate_game("Game 88: 3 blue, 9 green, 3 red; 2 blue, 15 green; 2 red, 9 green", (16, 17, 18)) == 88
    """
    formatted_game = format_game(game)
    valid = True
    for pick in formatted_game[1:]:
        for i in range(len(pick)):
            if pick[i] > bag[i]:
                valid = False
            else:
                pass
    if valid:
        return formatted_game[0]
    else:
        return 0


Test = False

if Test:
    print("test segmentate : ", segmentate_game("Game 88: 3 blue, 9 green, 3 red; 2 blue, 15 green; 2 red, 9 green") == (88, [[" 3 blue", " 9 green", " 3 red"], [" 2 blue", " 15 green"], [" 2 red", " 9 green"]]))
    print("test sort_pick1 : ", sort_pick([" 2 red", " 9 green"]) == (2, 9, 0))
    print("test sort_pick2 : ", sort_pick([" 3 blue", " 9 green", " 3 red"]) == (3, 9, 3))
    print("test format : ", format_game("Game 88: 3 blue, 9 green, 3 red; 2 blue, 15 green; 2 red, 9 green") == [88, (3, 9, 3), (0, 15, 2), (2, 9, 0)])
    print("test validate 1 : ", validate_game("Game 88: 3 blue, 9 green, 3 red; 2 blue, 15 green; 2 red, 9 green", (12, 13, 14)) == 0)
    print("test validate 2 : ", validate_game("Game 88: 3 blue, 9 green, 3 red; 2 blue, 15 green; 2 red, 9 green", (16, 17, 18)) == 88)
