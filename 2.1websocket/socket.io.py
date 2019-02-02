from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('/echo')
def echo_socket(ws):
    message = ws.receive()
    send(message)

if __name__ == '__main__':
    socketio.run(app)