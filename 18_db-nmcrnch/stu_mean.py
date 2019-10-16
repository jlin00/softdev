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

def create_tbl(tbl_name, headers):
    cmd = "CREATE TABLE {}({})".format(tbl_name, headers)
    c.execute(cmd)

def insertAll(tbl_name, filename):
    with open(filename, newline='') as file:
        fileReader = csv.DictReader(file)
        for row in fileReader:
            headers = list(row.values())
            c.execute("INSERT INTO {} VALUES('{}', {}, {})".format(tbl_name, *headers))

def addCourse(code, mark, id):
    c.execute("INSERT INTO courses VALUES(?, ?, ?)", (code, mark, id))

#thanks to Stack Overflow
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_id(s):
    s = int(s)
    for row in c.execute("SELECT id FROM students"):
        if s == row[0]:
            return True
    return False

#add one course to table
def inputCourse():
    code = input("Enter course code: ")
    while ("'" in code or code == ""):
        #handles single quote exception
        code = input("Please enter a valid course code without single quotes: ")

    mark = input("Enter course mark: ")
    while (not is_number(mark)):
        #handles nonnumber exception
        mark = input("Please enter a valid number: ")

    id = input("Enter student id: ")
    while (not is_number(id) or not is_id(id)):
        id = input("Please enter a valid id: ")

    addCourse(code, mark, id)

#calculate average mark after grouping results by id
def calcAvg():
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

create_tbl("students", "name TEXT NOT NULL, age INT NOT NULL, id INT PRIMARY KEY NOT NULL")
create_tbl("courses", "code TEXT NOT NULL, mark INT NOT NULL,id INT NOT NULL")
insertAll("students", "students.csv")
insertAll("courses", "courses.csv")
inputCourse()
create_tbl("stu_avg", "id INT, avg REAL")
calcAvg()

#==========================================================

db.commit() #save changes
db.close()  #close database
