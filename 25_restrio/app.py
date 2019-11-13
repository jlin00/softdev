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
    return render_template("main.html")

@app.route("/darksky")
def darksky():
    url = "https://api.darksky.net/forecast/28b607f4a70a742bd83b0931b1590466/42.3601,-71.0589"
    u = urllib2.urlopen(url)
    response = u.read()
    data = json.loads(response)
    return render_template("darksky.html",lat=data['latitude'],long=data['longitude'],timezone=data['timezone'],time=data['currently']['time'],sum=data['currently']['summary'])

@app.route("/omdb")
def omdb():
    url = "http://www.omdbapi.com/?t=handmaiden&apikey=bb27b700"
    u = urllib2.urlopen(url)
    response = u.read()
    data = json.loads(response)
    return render_template("omdb.html",title=data['Title'],year=data['Year'],runtime=data['Runtime'],dir=data['Director'],plot=data['Plot'])

@app.route("/countries")
def countries():
    url = "https://restcountries.eu/rest/v2/alpha/col?fields=name;capital;region;population;latlng;flag"
    u = urllib2.urlopen(url)
    response = u.read()
    data = json.loads(response)
    return render_template("countries.html", name=data['name'],cor=data['latlng'],region=data['region'],capital=data['capital'],pop=data['population'],flag=data['flag'])



if __name__ == "__main__":
    app.debug = True
    app.run()
