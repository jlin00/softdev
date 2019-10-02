#Michael Lin and Jackie Lin
#SoftDev1 pd1
#K15 -- ?
#2019-10-04

from flask import Flask, render_template, session, url_for, request

app = Flask(__name__)

#hard-coded credentials
username = 'guest'
password = '123'

@app.route("/")
def root():
    #session['username'] = request.args['username']
    return "root page"

@app.route("/auth")
def auth():
    return "auth page"

if __name__ == "__main__":
    app.debug = True
    app.run()
