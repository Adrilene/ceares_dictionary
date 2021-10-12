from flask import Flask, render_template

# from base_file import words
from bs4 import BeautifulSoup as bs
import random
import requests


app = Flask(__name__)


def transform_word(word):
    return str(word).replace("</h2>", "").split(". ")[1]

def transform_definition(definition):
    return str(definition).replace('<p class="text-justify">', "").replace('</p>', "").strip()


@app.route("/", methods=["GET"])
def index():
    page = requests.get("https://www.dicionariopopular.com/dicionario-cearense-girias/")
    soup = bs(page.content, "html.parser")
    words = list(soup.find_all("h2"))
    words.pop()
    words = [transform_word(word) for word in words]
    word = random.choice(words)

    page = requests.get(f"https://www.dicionarioinformal.com.br/{word}")
    soup = bs(page.content, "html.parser")
    try:
        definition = transform_definition(soup.find_all("p", {"class": "text-justify"})[0])
    except:
        definition = "Did not find definition"
    # print(f'WORD:{word} \n DEFINITION:{definition}')
    return render_template("index.html", word=word, definition=definition)


@app.route("/health_check", methods=["GET"])
def health_check():
    return "Working (Ceares Dictionary)"


if "__main__" == __name__:
    app.run(debug=True)