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
    if ("user" in session): #if username key exists in session, return welcome page
        return redirect("/welcome")
    else:
        return redirect("/login") #if user is not logged in, redirect to login form

@app.route("/auth")
def auth():
    if (username == request.args['username']): #takes in username from form data
        if (password == request.args['password']): #same thing, but with pswd
            session['user'] = username #user has successfully logged in
            return redirect("/welcome") #go to welcome page
        else:
            return render_template("error.html", msg="bad password") #wrong password
    else:
        return render_template("error.html", msg="bad username") #wrong username

@app.route("/welcome")
def welcome():
    if ("user" in session): #passes in username from session
        name = session['user']
    else: #if user is not logged in and navigates to welcome page manually
        name = "None"
    return render_template("welcome.html", user = name)

@app.route("/login")
def login():
    return render_template("form.html") #returns login form

@app.route("/logout")
def logout():
    if ("user" in session):
        session.pop('user') #remove user from session
    return redirect("/") #return to home page

if __name__ == "__main__":
    app.debug = True
    app.run()
