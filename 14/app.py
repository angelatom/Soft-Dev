from flask import Flask, render_template, session, url_for, redirect, request
import os
app = Flask(__name__)

app.secret_key = os.urandom(32)
@app.route("/", methods = ["POST", "GET"])
def home():
	
	if 'user' in session:
		return render_template("loggedin.html")
	else:
		return render_template("login.html")
		

@app.route("/login", methods = ["POST", "GET"])
def login():
	user = request.cookies.get('user')
	password = request.cookies.get('pass')
	session['user'] = password
	
	print(url_for("home"))
	return redirect(url_for("home"))
	
if __name__ == "__main__":
	app.debug = True
	app.run()