from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested, can change to a different path if you want
def hello_world():
    print(__name__) #prints to console
    return "No hablo queso!"
    #return app.send_static_file('first.html')



if __name__ == "__main__":
    app.debug = True #reloads the page every time you change the code
    app.run()
