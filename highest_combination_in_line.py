#-*-coding: utf-8 -*-
from highest_combination import Highest_combination
from itertools import *

class Highest_combination_in_line:
    """
    Returns max combination in the file
    """

    def __init__(self, line):
        """
        Takes a line of cards
        """
        self.__line=line
        self.__list_of_cards=self.__List_of_cards()
        self.__hend_cards=self.__list_of_cards[:5]
        self.__deck_cards = self.__list_of_cards[5:]
        self.__highest_combination=[]
        self.__max_combination=[]
        self.__max_combinations_cards=[]



    def perform(self):
        """
        Returns the string of initial hand, the top five
        cards on the deck, and the best value of hand that is possible
        """
        self.__Highest_combination()
        return self.__answer()


    def __List_of_cards(self):
        """Returns list of cards"""
        dict_of_suit={str(i):i for i in range(2,10)}
        tjqka={"T":10, "J":11, "Q": 12, "K": 13, "A": 14}
        dict_of_suit.update(tjqka)
        return [[dict_of_suit[i[0]], i[1]] for i in self.__line.split()]


    def __Highest_combination(self):
        combin = Highest_combination(self.__deck_cards)
        answer = combin.perform()
        self.__max_combination = self.dict_of_value_of_combination(answer)
        self.__max_combinations_cards = self.__deck_cards
        for i in range(6):
            self.__help_highest_combination(i)


    def __help_highest_combination(self, count_of_cards_from_hand):
        """Combine all variants  """
        for i in combinations(self.__hend_cards, count_of_cards_from_hand):
            comb=self.__deck_cards[:(5-count_of_cards_from_hand)]+list(i)
            combin=Highest_combination(comb)
            answer=combin.perform()
            if self.dict_of_value_of_combination(answer)[1]<self.__max_combination[1]:
                self.__max_combination=self.dict_of_value_of_combination(answer)
                self.__max_combinations_cards = comb



    def dict_of_value_of_combination(self, combin):
        a = ["straight_flush", "four_of_a_kind", "full_house", "flush", "straight",
             "three_of_a_kind", "two_pairs", "one_pair", "highest_card"]
        b={j : i for i,j in enumerate(a)}
        return [combin, b[combin]]


    def __answer(self):
        initial_hand = " ".join(self.__line.split()[:5])
        top_5_on_deck = " ".join(self.__line.split()[5:])
        best_hand = self.__max_combination[0]
        answer="Hand: "+initial_hand+" Deck: "+top_5_on_deck+" Best hend: "+best_hand+"\n"
        return answer









