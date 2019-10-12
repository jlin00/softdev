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


print("If you would like to stop adding courses, don't input anything and just press enter.")
#takes inputs from users and adds to course table
while (True):
    code = input("Enter course code: ")
    if code == "":
        break
    mark = input("Enter course mark: ")
    if mark == "":
        break
    id = input("Enter student id: ")
    if id == "":
        break
    c.execute("INSERT INTO courses VALUES(?, ?, ?)", (code, mark, id))

#create student grades table
c.execute(
    "CREATE TABLE stu_avg(id INT, avg REAL)"
)

#calculate average mark after grouping results by id
c.execute("""
            SELECT name, students.id, avg(mark)
            FROM students, courses
            WHERE students.id = courses.id
            GROUP BY students.id
            """)
rows = c.fetchall()
for row in rows:
    #print statement used to display each student's name, id, and avg
    print(("{}, {}: {}").format(row[0], row[1], row[2]))
    c.execute("INSERT INTO stu_avg VALUES(?, ?)", (row[1], row[2]))

#==========================================================

db.commit() #save changes
db.close()  #close database
