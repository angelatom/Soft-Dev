#Angela Tom
#SoftDev1 pd6
#K09 -- Solidify
#2018-09-20

from flask import Flask
app = Flask(__name__)

@app.route("/")
def link():
    return "<a href='/static/ello.html'>Yeet</a>"

if __name__ == "__main__":
    app.run()
