#Jackie Lin
#SoftDev1 pd1
#K10: Jinja Tuning
#2019-09-24

#Pair Programming
#Team Name: France
#Roster: Ivan Galakhov, Jackie Lin

import csv
import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/occupyflaskst') #returns html page with table of occupations
def occupyflaskst():
    job_dict = dict()

    with open('static/occupations.csv') as file:
        next(file) #skips first line
        reader = csv.reader(file) #from imports
        for row in reader:
            job_dict[row[0]] = float(row[1]) #key is title and value is percentage
    del job_dict['Total'] #remove last line 

    random_sel = lambda: random.choices(population=list(job_dict.keys()), weights=list(job_dict.values()), k=1)[0]
    #shorthand for a function that uses the built-in choices method to randomly select a key
    #the choices are the dictionary keys and the weights are the values of the key
    #k = 1 selects on item and returns the name

    return render_template('listpage.html',
                           jobs=job_dict.items(),
                           rand_job=random_sel(),
                           title='Occupations') #passes in dictionary and randomly-selected occupations


if __name__ == '__main__':
    app.debug = True
    app.run()
