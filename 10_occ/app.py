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


@app.route('/occupyflaskst')
def occupyflaskst():
    job_dict = dict()

    with open('static/occupations.csv') as file:
        next(file)
        reader = csv.reader(file)
        for row in reader:
            job_dict[row[0]] = float(row[1])
    del job_dict['Total']

    random_sel = lambda: random.choices(population=list(job_dict.keys()), weights=list(job_dict.values()), k=1)[0]

    return render_template('listpage.html',
                           jobs=job_dict.items(),
                           rand_job=random_sel(),
                           title='Occupations')


if __name__ == '__main__':
    app.debug = True
    app.run()
