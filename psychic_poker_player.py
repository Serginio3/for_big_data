#-*-coding: utf-8 -*-

from highest_combination_in_line import *

class Psychic_poker_player:
    """
    Main class
    """

    def __init__(self):
        """Takes series of lines from file 'file_input.txt'  """
        self.__series_of_lines=self.__input_information()

    def perform(self):
        """ Write the max combination from each line to a file """
        self.__series_of_lines=self.__series_of_lines.split('\n')
        answer=""
        for line in self.__series_of_lines:
            comb=Highest_combination_in_line(line)
            answer+=comb.perform()
        self.__output(answer)


    def __input_information(self):
        """Read file  """
        with open('file_input.txt', 'r') as f:
            read_data=f.read()
        return read_data


    def __output(self, answer):
        """Write answer to a file"""
        with open('file_output.txt', 'w') as f:
            f.write(answer)



Jhon_Galt=Psychic_poker_player()
Jhon_Galt.perform()