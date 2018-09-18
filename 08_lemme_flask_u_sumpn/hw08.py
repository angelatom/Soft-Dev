#Angela Tom
#SoftDev1 pd6
#K08 -- Fill Yer Flask
#2018-09-18

from flask import Flask
app = Flask(__name__)

@app.route("/")
def header():
    return "<h1>Links to other pages below:</h1> <br/> <a href='/hello'>Hello</a> <br/> <a href='/bye'>Bye</a>"

@app.route("/hello")
def hello():
    return "<h1>HELLO</h1> <a href='/'>Back</a>"

@app.route("/bye")
def bye():
    return "<h1>BYE</h1> <a href='/'>Back</a>"

if __name__ == "__main__":
    app.run()
