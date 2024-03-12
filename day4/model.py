class CardsSets:
    def __init__(self, input):
        self.cards_list = []
        for line in input:
            line = line.strip()
            card_number = line.split(":")[0].split()[-1]
            winning_numbers = line.split(":")[1].split("|")[0].split()
            numbers = line.split(":")[1].split("|")[1].split()
            self.cards_list.append({"card_number": card_number, "instances": 1, "winning_numbers": winning_numbers, "numbers": numbers})

    def get_winning_numbers(self, card) -> int:
        total_winning_numbers = 0
        for number in card["numbers"]:
            if number in card["winning_numbers"]:
                total_winning_numbers += 1
        return total_winning_numbers

    def get_card_point(self, card):
        total = self.get_winning_numbers(card)
        if total:
            points = 2 ** (total-1)
            return points
        else:
            return 0

    def get_points(self):
        total_points = 0
        for card in self.cards_list:
            total_points += self.get_card_point(card)
        return total_points

    def copy_next_cards(self, card, index):
        number_of_copy = self.get_winning_numbers(card)
        while number_of_copy > 0:
            self.cards_list[index+number_of_copy]["instances"] += 1
            number_of_copy -= 1

    def copy_cards(self):
        for i in range(len(self.cards_list)):
            index = i
            card = self.cards_list[index]
            number_of_instance_left = card["instances"]
            while number_of_instance_left > 0:
                self.copy_next_cards(card, index)
                number_of_instance_left -= 1

    def get_total_cards(self):
        self.copy_cards()
        total_cards = 0
        for card in self.cards_list:
            total_cards += card["instances"]
        return total_cards
