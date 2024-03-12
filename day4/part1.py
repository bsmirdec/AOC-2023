from model import CardsSets


def main(input_file):
    with open(input_file, "r") as input:
        cards_set = CardsSets(input.readlines())
        result = cards_set.get_points()
        return result


total_points = main("day4/input.txt")
print(total_points)
