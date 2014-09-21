'''
Run a bottle server to control a player remotelly
'''


from bottle import route, run, view
from core.player import Player
from core.system import System

def main():
    player = Player()
    system = System()

    @route('/play')
    def play():
        player.play()

    @route('/pause')
    def play():
        player.pause()

    @route('/play_pause')
    def play_pause():
        player.play_or_pause()

    @route('/up')
    def up():
        player.volume_up()

    @route('/down')
    def down():
        player.volume_down()

    @route('/next')
    def next():
        player.next()

    @route('/previous')
    def previous():
        player.previous()

    @route('/artist')
    def artist():
        return player.get_artist()

    @route('/track')
    def track():
        return player.get_track()

    @route('/enable_shuffle')
    def enable_shuffle():
        player.shuffle()

    @route('/disable_shuffle')
    def disable_shuffle():
        player.no_shuffle()

    @route('/enable_repeat')
    def enable_repeat():
        player.repeat()

    @route('/disable_repeat')
    def disable_repeat():
        player.no_repeat()

    @route('/rating/<value:int>')
    def rating(value):
        player.set_rating(value)

    @route('/quit')
    def quit():
        player.quit()

    @route('/system_up')
    def system_up():
        system.volume_up()

    @route('/system_down')
    def system_down():
        system.volume_down()

    run(host='0.0.0.0', port=3000, debug=True, reloader=True)

if __name__ == '__main__':
    main()
