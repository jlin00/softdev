#Team Spooky Szn
#Jackie Lin && Yaru Luo
#SoftDev1 pd1
#K18 -- Average
#2019-10-09

import sqlite3 #enable control of an sqlite database
import csv #facilitate CSV I/O

#Must delete this every time this py file is run!
DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#students.csv
c.execute(
    "CREATE TABLE students(name TEXT NOT NULL, age INT NOT NULL, id INT PRIMARY KEY NOT NULL)"
)

with open('students.csv', newline='') as students:
    stuReader = csv.DictReader(students)
    for row in stuReader:
        c.execute("INSERT INTO students VALUES(?, ?, ?)", (row['name'], row['age'], row['id']))

#courses.csv
c.execute(
    "CREATE TABLE courses(code TEXT NOT NULL, mark INT NOT NULL,id INT NOT NULL)"
)

with open('courses.csv', newline='') as courses:
    courseReader = csv.DictReader(courses)

    for row in courseReader:
        c.execute("INSERT INTO courses VALUES(?, ?, ?)", (row['code'], row['mark'], row['id']))

#==========================================================

db.commit() #save changes
db.close()  #close database
