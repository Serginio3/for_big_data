#-*-coding: utf-8 -*-

class Highest_combination:
    """
    Returns max combination
    """

    def __init__(self, cards):
        """
        Takes list of 5 cards (list)
        """
        self.__cards = cards.copy()
        self.__cards_value = self.__Cards_value()
        self.__set_of_cards_value = self.__Set_of_cards_value()
        self.__set_of_cards_suit = self.__Set_of_cards_suit()



    def perform(self):
        """Returns the string of best combination.
        The first method that returns string is the answer.
        """
        return  self.is_straight_flush() or \
                self.is_four_of_a_kind() or \
                self.is_full_house() or \
                self.is_flush() or \
                self.is_straight() or \
                self.is_three_of_a_kind() or \
                self.is_two_pairs() or \
                self.is_one_pair() or \
                self.is_highest_card()


    def is_straight_flush(self):
        if self.__set_of_cards_value == 5 and self.__set_of_cards_suit==1: # if straight_flush from A to 5
            if 14 in self.__cards_value:
                new_cards_value=[1] + self.__cards_value[:-1]
                flag=True
                for i in range(4):
                    if new_cards_value[i+1] - new_cards_value[i] != 1:
                        flag=False
                        break
                if flag: return "straight_flush"

            for i in range(4):
                if self.__cards_value[i+1] - self.__cards_value[i] != 1 : return 0
            return "straight_flush"
        return 0


    def is_four_of_a_kind(self):
        if self.__set_of_cards_value == 2:
            if self.__cards_value.count(self.__cards_value[0]) == 1 or \
                    self.__cards_value.count(self.__cards_value[0]) == 4:
                return "four_of_a_kind"
        return 0

    def is_full_house(self):
        if self.__set_of_cards_value == 2:
            if self.__cards_value.count(self.__cards_value[0]) == 2 or \
                    self.__cards_value.count(self.__cards_value[0]) == 3:
                return "full_house"
        return 0


    def is_flush(self):
        if self.__set_of_cards_suit == 1:
            return "flush"


    def is_straight(self):
        if 14 in self.__cards_value:                                 # if straight from A to 5
            new_cards_value = [1] + self.__cards_value[:-1]
            flag = True
            for i in range(4):
                if new_cards_value[i+1] - new_cards_value[i] != 1:
                    flag = False
                    break
            if flag: return "straight"

        for i in range(4):
            if self.__cards[i+1][0] - self.__cards[i][0] != 1: return 0
        return "straight"


    def is_three_of_a_kind(self):
        if self.__set_of_cards_value == 3:
            for i in self.__cards_value:
                if self.__cards_value.count(i) == 3:
                    return "three_of_a_kind"
        return 0


    def is_two_pairs(self):
        if self.__set_of_cards_value == 3:
            return "two_pairs"


    def is_one_pair(self):
        if self.__set_of_cards_value == 4:
            return "one_pair"


    def is_highest_card(self):
        return "highest_card"


    def __Set_of_cards_value(self):
        return len(set(self.__cards_value))


    def __Set_of_cards_suit(self):
        mast_of_cards = [i[1] for i in self.__cards]
        return len(set(mast_of_cards))


    def __sort_cards(self):
        self.__cards.sort(key = lambda x: x[0])


    def __Cards_value(self):
        self.__sort_cards()
        return [i[0] for i in self.__cards]


