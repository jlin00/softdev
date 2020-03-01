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

def display_categories():
    category_one = list(events.find({}, {'_id': 0, 'category1': 1}))
    set = set()
    for item in category_one:
        set.add(item['category1'])
    print(set)

display_categories()
