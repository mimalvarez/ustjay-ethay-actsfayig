import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def get_piglatin(fact):
    response = requests.post('http://hidden-journey-62459.herokuapp.com/piglatinize/',
                             data = {"input_text":fact})
    return response.url


@app.route('/')
def home():
    fact = get_fact().strip()
    body = get_piglatin(fact)
    #return Response(response=body)
    return body

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

