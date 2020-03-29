from flask import Flask
import socket

app = Flask(__name__)


@app.route('/')
def root():
    http_reply = 'Hello World<br />\n{}'.format(socket.gethostname()) 
    return http_reply


if __name__ == '__main__':
    app.run(port=80)
