from flask import Flask
from flask_uwsgi_websocket import GeventWebSocket

app = Flask(__name__)
websocket = GeventWebSocket(app)

@websocket.route('/echo')
def echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
                ws.send(msg)
        else:return

if __name__ == '__main__':
    app.run(debug=True,gevent=100)