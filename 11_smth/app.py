#Jackie Lin
#SoftDev1 pd1
#K
#2019-09-25

#Pair Programming
#Team Name: Big Brains
#Roster: Joseph Lee, Jackie Lin

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('form.html')

@app.route('/auth')
def submission():
    print(request)
    return (request.args)['name'] + "\'s brain is " + (request.args)['age'] + " Years Old!"


if __name__ == '__main__':
    app.debug = True
    app.run()
