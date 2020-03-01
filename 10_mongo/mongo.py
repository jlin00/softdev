#Kenneth Chin, Jackie Lin
#SoftDev1 pd1
#K10 -- Import/Export Bank
#2020-03-04

import json
from pymongo import MongoClient

client = MongoClient()
db = client.test
events = db.events
if (events.count() == 0):
    with open('dataset.json') as file:
        data = json.load(file)
        for event in data['results']:
            events.insert_one(event)

for item in events.find({}).limit(20):
    print(item)
