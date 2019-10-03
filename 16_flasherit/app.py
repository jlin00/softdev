#Michael Lin and Jackie Lin
#SoftDev1 pd1
#K16 -- Oh yes, perhaps I do...
#2019-10-04

from flask import Flask, render_template, session, url_for, request, redirect, flash
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
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('login')) #if user is not logged in, redirect to login form

@app.route("/auth")
def auth():
    if (username == request.args['username']): #takes in username from form data
        if (password == request.args['password']): #same thing, but with pswd
            session['user'] = username #user has successfully logged in
            flash("You were successfully logged in.")
            return redirect(url_for('welcome')) #go to welcome page
        else:
            flash("Bad Password")
            return render_template("error.html") #wrong password
    else:
        flash("Bad Username")
        return render_template("error.html") #wrong username

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
    return redirect(url_for('root')) #return to home page

if __name__ == "__main__":
    app.debug = True
    app.run()
