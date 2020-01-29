#Jackie Lin
#SoftDev1 pd1
#K24: A RESTful Journey Skyward
#2019-11-13

from flask import Flask, render_template
import urllib.request as urllib2
#import urllib3 #second method using urllib3
import json
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=tcePwmse95ZYuZ2kBWPenl6klaR3BCoKWm86eehP")
    response = u.read()
    data = json.loads(response)

    #using urllib3

    #url = "https://api.nasa.gov/planetary/earth/imagery/?lon=-74.011146&lat=40.71139&cloud_score=0&api_key=tcePwmse95ZYuZ2kBWPenl6klaR3BCoKWm86eehP"
    #http = urllib3.PoolManager()
    #response = http.request('GET', url)
    #data = json.loads(response.data)

    return render_template("index.html", pic=data['url'], desc=data['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
