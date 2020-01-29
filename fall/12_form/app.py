#Jackie Lin
#SoftDev1 pd1
#K12: Echo Echo Echo
#2019-09-25

#Pair Programming
#Team Name: Big Brain
#Roster: Joseph Lee, Jackie Lin

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    print(app)
    print(request)
    print(request.args)
    return render_template('form.html')

@app.route('/auth')
def submission():
    '''
    print("REQUEST")
    print(request)
    print("ARGS")
    print(request.args)
    print("NAME")
    print(request.args['name'])
    print("HEADERS")
    '''
    print(request.headers)
    return render_template('response.html',
                            name=request.args['name'],
                            request=request.method,
                            age=request.args['age'])
    #return (request.args)['name']) print( "\'s brain is ") print( (request.args)['age']) print( " Years Old!"


if __name__ == '__main__':
    app.debug = True
    app.run()
