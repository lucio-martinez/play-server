'''
Run a bottle server to control a player remotelly
'''


from bottle import Bottle, route, run, response, request, view
import cherrypy
from core.player import Player
from core.system import System

app = Bottle()

'''
Decorator to enable CORS for specific routes
Thanks to ron.rothman! (http://stackoverflow.com/a/17262900)
'''
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

def main():
    player = Player()
    system = System()

    @app.route('/play')
    def play():
        player.play()

    @app.route('/pause')
    def play():
        player.pause()

    @app.route('/play_pause')
    def play_pause():
        player.play_or_pause()

    @app.route('/up')
    def up():
        player.volume_up()

    @app.route('/down')
    def down():
        player.volume_down()

    @app.route('/next')
    def next():
        player.next()

    @app.route('/previous')
    def previous():
        player.previous()

    @app.route('/artist')
    @enable_cors
    def artist():
        return player.get_artist()

    @app.route('/track')
    @enable_cors
    def track():
        return player.get_track()

    @app.route('/enable_shuffle')
    def enable_shuffle():
        player.shuffle()

    @app.route('/disable_shuffle')
    def disable_shuffle():
        player.no_shuffle()

    @app.route('/enable_repeat')
    def enable_repeat():
        player.repeat()

    @app.route('/disable_repeat')
    def disable_repeat():
        player.no_repeat()

    @app.route('/rating/<value:int>')
    def rating(value):
        player.set_rating(value)

    @app.route('/quit')
    def quit():
        player.quit()

    @app.route('/system_up')
    def system_up():
        system.volume_up()

    @app.route('/system_down')
    def system_down():
        system.volume_down()

    run(app, server='cherrypy', host='0.0.0.0', port=3000, debug=True)

if __name__ == '__main__':
    main()
