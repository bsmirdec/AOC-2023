from model import CardsSets


def main(input_file):
    with open(input_file, "r") as input:
        cards_set = CardsSets(input.readlines())
        result = cards_set.get_total_cards()
        return result


total_cards = main("day4/input.txt")
print(f"Total des cartes: {total_cards}")
