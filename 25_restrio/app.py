#Jackie Lin
#SoftDev1 pd1
#K25: Getting More REST
#2019-11-13

from flask import Flask, render_template
import urllib.request as urllib2
import json
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=tcePwmse95ZYuZ2kBWPenl6klaR3BCoKWm86eehP")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", pic=data['url'], desc=data['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
