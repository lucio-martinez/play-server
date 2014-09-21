'''
API to the Rhythmbox client to control the player
Author: Lucio Martínez <luciomartinez at openmailbox dot org>
'''

import subprocess


class Player:

    def __init__(self):
        self.client = 'rhythmbox-client'

    def __exec(self, command):
        return subprocess.check_output(command, shell=True)

    def __action(self, action, format=''):
        return self.__exec(self.client + ' ' + '--' + action + ' ' + format)

    def play(self):
        self.__action('play')

    def pause(self):
        self.__action('pause')

    def play_or_pause(self):
        self.__action('play-pause')

    def volume_up(self):
        self.__action('volume-up')

    def volume_down(self):
        self.__action('volume-down')

    def next(self):
        self.__action('next')

    def previous(self):
        self.__action('previous')

    def quit(self):
        self.__action('quit')

    def repeat(self):
        self.__action('repeat')

    def no_repeat(self):
        self.__action('no-repeat')

    def shuffle(self):
        self.__action('shuffle')

    def no_shuffle(self):
        self.__action('no-shuffle')

    '''
    Set the Rating for the current song
    @param rating Integer with a value from 0 to 5
    '''
    def set_rating(self, rating):
        self.__action('set-rating', str(rating))

    '''
    Get the artist for the current song
    @return string
    '''
    def get_artist(self):
        return self.__action('print-playing-format', '%ta')

    '''
    Get the track name for the current song
    @return string
    '''
    def get_track(self):
        return self.__action('print-playing-format', '%tt')
