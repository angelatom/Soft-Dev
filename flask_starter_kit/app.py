from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def flask():
    render_template("index.html") 
    print(app)

if __name__ == "__main__":
    app.debug = True
    app.run()
