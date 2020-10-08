from flask import Flask, render_template
from base_file import words
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    word = random.choice(words)
    return render_template('index.html', word=word)


if  __name__ == '__main__':
    app.run()