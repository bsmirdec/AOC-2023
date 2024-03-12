from part1 import main as main_part1
from part2 import main as main_part2
from model import CardsSets


def test_get_winning_numbers():
    with open("day4/example.txt", "r") as example:
        cards_sets = CardsSets(example)
        card = cards_sets.cards_list[0]
        assert cards_sets.get_winning_numbers(card) == 4


def test_get_card_point():
    with open("day4/example.txt", "r") as example:
        cards_sets = CardsSets(example)
        card = cards_sets.cards_list[0]
        assert cards_sets.get_card_point(card) == 8


def test_get_points():
    with open("day4/example.txt", "r") as example:
        cards_sets = CardsSets(example)
        assert cards_sets.get_points() == 13


def test_copy_next_card():
    with open("day4/example.txt", "r") as example:
        cards_sets = CardsSets(example)
        index = 0
        card = cards_sets.cards_list[index]
        cards_sets.copy_next_cards(card, index)
        assert cards_sets.cards_list[1]["instances"] == 2
        assert cards_sets.cards_list[2]["instances"] == 2
        assert cards_sets.cards_list[3]["instances"] == 2
        assert cards_sets.cards_list[4]["instances"] == 2


def test_winning_numbers_sum():
    result = main_part1("day4/example.txt")

    assert result == 13


def test_total_cards():
    result = main_part2("day4/example.txt")

    assert result == 30
