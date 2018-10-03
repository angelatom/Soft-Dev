#I Like Cookies -- Angela Tom and Xiaojie(Aaron) Li
#SoftDev1 pd6
#K14 -- Do I Know You?
#2018-10-01


# import all the things we need
from flask import Flask, render_template, session, url_for, redirect, request
import os
app = Flask(__name__) # creates instance of a flask app

app.secret_key = os.urandom(32) 
# hard coded username and password
username = "Test"
passwd = "password"

@app.route("/", methods = ["POST", "GET"])
def home():
	if "user" in session: # if the key, user, is in session, then...
		return render_template("loggedin.html", user = username) # go to logged in page 
	else:
		return render_template("login.html") # the start page

@app.route("/login", methods = ["POST", "GET"]) # things to do when user presses submit on login page
def login():
    if request.form["user"] != username or request.form["pass"] != passwd: 
        return render_template("login.html") # username/password are incorrect
    else:
        session["user"] = username # add user to session
        return redirect(url_for("home")) 
		
@app.route("/logout", methods = ["POST", "GET"]) 
def logout():
	session.pop("user") # remove user from session
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run()
