# from flask_bootstrap import Bootstrap5
import time
from flask import Flask, render_template, Response
from flask_socketio import SocketIO,send,emit
from stream_io import stream
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



@app.route('/')
def index():
    return render_template("index.html")


@socketio.on('video_request')
def video_request(data):
    stream(socketio)



if __name__ == '__main__':
    socketio.run(app,debug=True)

