# from flask_bootstrap import Bootstrap5
import time
from flask import Flask, render_template, Response
# from flask_socketio import SocketIO,send,emit
from stream_multi import Stream
from threading import Thread

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)


stream = Stream()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/video_rgb')
def video_rgb():
    return Response(stream.stream_rgb(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_flir')
def video_flir():
    return Response(stream.stream_flir(), mimetype='multipart/x-mixed-replace; boundary=frame')


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    for x in range(10):
        emit("hello ke {}".format(x))



if __name__ == '__main__':
    # stream.start()
    Thread(target=app.run,args=("0.0.0.0",False)).start()
 
