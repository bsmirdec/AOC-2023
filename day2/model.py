class Games:
    def __init__(self, game_id, *picks):
        self.game_id = game_id
        self.picks = list(picks)

    def __str__(self) -> str:
        picks_str = ', '.join(str(pick) for pick in self.picks)
        return f"Game {self.game_id}: {picks_str}"

    def add_pick(self, pick):
        self.picks.append(pick)

    def max_cubes(self) -> tuple:
        max_red = 0
        max_green = 0
        max_blue = 0
        for pick in self.picks:
            if pick.red > max_red:
                max_red = pick.red
            if pick.green > max_green:
                max_green = pick.green
            if pick.blue > max_blue:
                max_blue = pick.blue
        return (max_red, max_green, max_blue)

    def is_valid_part1(self, bag) -> bool:
        valid = True
        for i in range(len(bag)):
            if self.max_cubes()[i] > bag[i]:
                valid = False
        return valid

    def power_part2(self) -> tuple:
        power = 1
        max = self.max_cubes()
        for i in range(len(max)):
            if max[i] != 0:
                power = power * max[i]
        return power


class Picks:
    def __init__(self, game_id, pick_id, red, green, blue):
        self.game_id = game_id
        self.pick_id = pick_id
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self) -> str:
        return f"pick n°{self.pick_id}: (r: {self.red}, g: {self.green}, b: {self.blue})"