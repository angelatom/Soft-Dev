'''
Angela Tom
SoftDev1 pd6
K24 -- A RESTful Journey Skyward
2018-11-14
'''

from urllib import request, parse
from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route("/")
def display():
    req = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=dzhewdza2a1W44bJDAB1Nb5v6WxgmXnoTRPxWvM4").read()
    reqD = json.loads(req)
    pic = reqD['url']
    return render_template("index.html", image = pic)

if __name__ == "__main__":
    app.debug = True
    app.run()
