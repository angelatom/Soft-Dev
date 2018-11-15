'''
Angela Tom
SoftDev1 pd6
K25 -- Getting More REST
2018-11-14
'''
import json
from urllib import request

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def display():
    KEY = "yFazaMRPA3SbDgv2Y"
    URL_STUB = "http://api.airvisual.com/v2/city?city=New%20York&state=New%20York&country=USA&key="
    URL = URL_STUB + KEY
    response = request.urlopen(URL)
    response = response.read()
    data = json.loads(response)
    print(data)
    info = data['data']['current']
    weather = info['weather']
    ts = weather['ts']
    tp = weather['tp']
    pr = weather['pr']
    hu = weather['hu']
    pollution = info['pollution']
    aqi = pollution['aqius']
    return render_template("index.html", timestamp = ts, temp = tp, pressure = pr, humidity = hu, aqi = aqi)

if __name__ == "__main__":
    app.debug = True
    app.run()
