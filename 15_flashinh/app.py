'''
I Like Cookies: Xiaojie(Aaron) Li, Angela Tom
SoftDev1 pd6
K15 -- Oh Yes Perhaps I Do...
2018-10-02
'''

# import all the stuffs
from flask import Flask, render_template, request, url_for, session, redirect, flash
import os

# instantiate flask app
app = Flask(__name__)
# generate a random key for session
app.secret_key = os.urandom(32)

# first route is index
@app.route("/", methods = ["POST", "GET"])
def index() :
    # when submit button is clicked:
    if request.method == "POST":
        # if login is wrong, flash an error with message
        if request.form["username"] != "c00lman" or request.form["password"] != "c00lpass":
            if request.form["username"] != "c00lman":
                problem = "username"
            else:
                problem = "password"
            flash("Wrong " + problem + ", try again!")
            return redirect(url_for("index"))
        else: # if login was correct, redirect to welcome page
            session["username"] = "c00lman"
            return redirect(url_for("index"))
    else: # if submit button wasn't clicked:
        if "username" in session: # if user is logged in, return welcome page, else login page
            return render_template("welcome.html", username = session["username"])
        return render_template("login.html")

# second route handles logging out, just drop the session
@app.route("/drop")
def logout():
    session.pop("username", None)
    # redirect to appropriate page in index
    return redirect(url_for("index"))

# run flask
if __name__ == "__main__":
    app.run(debug = True)
