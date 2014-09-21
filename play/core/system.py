'''
API to the system sound to change volume level
Author: Lucio Martínez <luciomartinez at openmailbox dot org>
'''

import os


class System:

    def __init__(self):
        self.client_settings = 'amixer -D pulse sset Master'
        self.range = '20%'

    def __set(self, option):
        os.system(self.client_settings + ' ' + self.range + option)

    def volume_up(self):
        self.__set('+')

    def volume_down(self):
        self.__set('-')