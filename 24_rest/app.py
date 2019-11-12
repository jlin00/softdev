from flask import Flask
import urllib2, json
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=tcePwmse95ZYuZ2kBWPenl6klaR3BCoKWm86eehP")
    response = u.read()
    data = json.loads(response)
    return render-template("index.html", pic=data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
