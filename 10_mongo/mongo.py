#Kenneth Chin, Jackie Lin
#SoftDev1 pd1
#K10 -- Import/Export Bank
#2020-03-04

import json
from pymongo import MongoClient

client = MongoClient()
db = client.croissants
events = db.events
if (events.count() == 0):
    with open('dataset.json') as file:
        data = file.read() #convert file to str
        data = data[30:-3] #clean up file
        data = data.split("\"event\": ") #list of events
        data.pop(0) #empty entry
        for item in data:
            if item[-1] == ' ':
                item = item[0:-2] #formatting JSON object
            item = json.loads(item) #load object
            events.insert_one(item) #insert into database

# for item in events.find({}).limit(20):
#     print(item)

def get_by_place(location):
    results = events.find({"category2" : location})
    print ("Place: {}".format(location))
    print()
    for x in results:
       print("Place:"  + x["category2"] + "\nEvent:" + x["description"])

def get_by_year(year):
    results = events.find({ "date": {'$regex' : str(year)} })
    print("Date: {}".format(year))
    print("Results Found: {}".format(results.count()))
    print()
    for x in results:
      print("Date:" + x["date"] + "\nEvent:" + x["description"])

def get_by_topic(topic):
    '''Returns all events that fall under a certain topic'''
    query = {"category2":{"$regex":topic, "$options": "i"}}
    results = events.find(query, {"_id": 0, "date": 1, "description": 1})
    print("Topic: {}".format(topic))
    print("Results Found: {}".format(results.count()))
    print()
    for x in results:
      print("Date:" + x["date"] + "\nEvent:" + x["description"])

def get_by_keyword():
    print("HELLO WORLD")

def input_timeline():
    print("HELLO WORLD")

get_by_place("Egypt")
get_by_year(2000)
get_by_topic("astronomy")
