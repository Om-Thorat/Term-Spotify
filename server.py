from flask import Flask
from flask_socketio import SocketIO
import os
# create a Socket.IO server
app = Flask(__name__)
sio = SocketIO(app, cors_allowed_origins='*')

@sio.on('message')
def handle(data):
    print(data)

@sio.on('command')
def again(data):
    print(data)
    x = input()
    sio.emit("input",x)

if __name__ == "__main__":
    sio.run(app, host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 443)), debug=False)
