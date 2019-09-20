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

    with open('static/occupations.csv') as file: #see comments in csvreader.py file
        next(file)
        reader = csv.reader(file)
        for row in reader:
            job_dict[row[0]] = float(row[1])
    del job_dict['Total']

    random_sel = lambda: random.choices(population=list(job_dict.keys()), weights=list(job_dict.values()), k=1)[0]

    return render_template('listpage.html',
                           jobs=job_dict.items(),
                           rand_job=random_sel(),
                           title='Occupations') #passes in dictionary and randomly-selected occupations 


if __name__ == '__main__':
    app.debug = True
    app.run()
