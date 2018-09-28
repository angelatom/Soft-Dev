# Angela Tom
# SoftDev1 pd6
# K13 -- Echo Echo Echo
# 2018-09-28

from flask import Flask, render_template, request
app = Flask(__name__)    #create Flask object

# Home page
@app.route("/")
def formpage():
    return render_template("form.html") # Render the template

# When the form is submitted
@app.route("/auth")
def authenticate():
    print (app)
    print (request)
    print (request.headers)
    print (request.method)
    print (request.args)
    print (request.form)
    return render_template("auth.html", username = request.args["username"], req = request.method) # Render the auth page



if __name__ == "__main__": 
    app.debug = True 
    app.run()
