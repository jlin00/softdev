#Jackie Lin
#SoftDev pd1
#K17 -- No Trouble
#2019-10-08

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
with open('courses.csv') as coursefile:
    reader = csv.DictReader(coursefile) #create new dictreader object
    c.execute("create table courses (code text, mark integer, id integer);") #create table
    for row in reader:
        command = "insert into courses values (\"" + row['code'] + "\", " + row['mark'] + ", " + row['id'] + ");"
        c.execute(command)

with open('students.csv') as studentfile:
    reader = csv.DictReader(studentfile) #create new dictreader object
    c.execute("create table students (code text, mark integer, id integer);") #create table
    for row in reader:
        command = "insert into students values (\"" + row['name'] + "\", " + row['age'] + ", " + row['id'] + ");"
        c.execute(command)


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
