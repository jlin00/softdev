#Jackie Lin
#SoftDev1 pd1
#K009: ’Tis Not a Race -- But You Will Go Faster
#2019-09-19

#Pair Programming
#Team Name: France
#Roster: Ivan Galakhov, Jackie Lin

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    print('index!!')
    return 'whatever'


@app.route('/html')
def html():
    print('html!!')
    return app.send_static_file('index.html')


@app.route('/template')
def template():
    print('template')
    coll = [0, 1, 1, 2, 3, 5, 8]
    return render_template('listpage.html', title='Hello!', coll=coll)


if __name__ == '__main__':
    app.debug = True
    app.run()
