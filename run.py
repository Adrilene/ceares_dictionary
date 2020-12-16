from flask import Flask, render_template
#from base_file import words
from bs4 import BeautifulSoup as bs
import random
import requests


app = Flask(__name__)

def transform_word(word):
    return str(word).replace('</h2>', '').split('. ')[1]

@app.route('/', methods=['GET'])
def index():
    page = requests.get("https://www.dicionariopopular.com/dicionario-cearense-girias/")
    soup = bs(page.content, 'html.parser')
    words = list(soup.find_all('h2'))
    words.pop()
    words = [transform_word(word) for word in words]
    word = random.choice(words)
    return render_template('index.html', word=word)

@app.route('/support', methods=['GET'])
def index():
    return "Woeking (Ceares Dictionary)"

if '__main__' ==__name__:
    app.run()