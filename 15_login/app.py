#Michael Lin and Jackie Lin
#SoftDev1 pd1
#K15 -- ?
#2019-10-04

from flask import Flask, render_template, session, url_for, request

app = Flask(__name__)


@app.route("/")
def form():
    #session['username'] = request.args['username']
    print(request.args['username'])
    return render_template("form.html",
                            username = request.args['username'],
                            password = request.args['password'])

@app.route("/auth")
def auth():
    return render_template("response.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
