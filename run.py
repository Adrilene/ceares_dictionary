from flask import Flask


app = Flask(__name__)

def index('/', methods=['GET']):
    return 'OK'


if  __name__ == '__main__':
    app.run()