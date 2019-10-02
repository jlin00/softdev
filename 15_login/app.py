#Michael Lin and Jackie Lin
#SoftDev1 pd1
#K15 -- ?
#2019-10-04

from flask import Flask, render_template, session, url_for, request, redirect
import os

app = Flask(__name__)
#session secret key, code from Stack Overflow
app.config['SECRET_KEY'] = os.urandom(32)

#hard-coded credentials
username = 'guest'
password = '123'

@app.route("/")
def root():
    #session['username'] = request.args['username']
    if ("username" in session): #if username key exists in session, return welcome page
        return redirect("/welcome")
    else:
        return redirect("/login") #if user is not logged in, redirect to login form

@app.route("/auth")
def auth():
    return "auth page"

@app.route("/welcome")
def welcome():
    if ("username" in session): #passes in username from session
        username = session['username']
    else: #if user is not logged in and navigates to welcome page manually
        username = "None"
    return render_template("welcome.html",
                            username = username)

@app.route("/login")
def login():
    return render_template("form.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
