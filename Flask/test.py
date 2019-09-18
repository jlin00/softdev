from flask import Flask
app = Flask(__name__) #create instance of class Flask

def print_more():
    return "Yo quiero hamburguesa!"

@app.route("/") #assign following fxn to run when root route requested, can change to a different path if you want
def hello_world():
    print(__name__) #where will this go? --> console
    print(print_more())  #when you refresh, this goes into the console
    print("new stuff")
    return "No hablo queso!"
    #return app.send_static_file('first.html')

if __name__ == "__main__":
    app.debug = True #reloads the page every time you change the code
    app.run()
