#Jackie Lin
#SoftDev1 pd1
#K08: Lemme Flask You Sump’n
#2019-09-19

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested, can change to a different path if you want
def homepage():
    print(__name__) #prints to console
    return "No hablo queso!"

@app.route("/first")
def firstpage():
    print("first page")
    return app.send_static_file('first.html')

@app.route("/second")
def secondpage():
    print("second page")
    return app.send_static_file('second.html')

@app.route("/third")
def thirdpage():
    print("third page")
    return "this is the third page!!! not html lol"

if __name__ == "__main__":
    app.debug = True #reloads the page every time you change the code
    app.run()
