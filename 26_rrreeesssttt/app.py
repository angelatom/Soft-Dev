'''
Angela Tom
SoftDev1 pd6
K26 -- Getting More REST
2018-11-16
'''
import json
from urllib import request

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def display():
    #SpaceX
    URL = "https://api.spacexdata.com/v3/launches/latest"
    response = request.urlopen(URL)
    response = response.read()
    data = json.loads(response)
    flight_num = data['flight_number']
    flight_info = data['details']
    #GIPHY
    URL_STUB = "https://api.giphy.com/v1/gifs/random?api_key="
    KEY = "ef7XqC22bPGpVhlve8ldM9I8KS8aCyUi"
    URL = URL_STUB + KEY + "&rating=PG"
    response = request.urlopen(URL)
    response = response.read()
    data = json.loads(response)
    gif = data['data']['embed_url']
    #Poemist
    URL = "https://www.poemist.com/api/v1/randompoems"
    response = request.urlopen(URL)
    response = response.read()
    data = json.loads(response)
    poem_url = data[0]['url']
    return render_template("index.html", flight_num = flight_num, flight_info = flight_info, poem = poem_url, gif = gif)

if __name__ == "__main__":
    app.debug = True
    app.run()
