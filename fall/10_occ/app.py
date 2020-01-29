# Jackie Lin
# SoftDev1 pd1
# K10: Jinja Tuning
# 2019-09-24

# Pair Programming
# Team Name: France
# Roster: Ivan Galakhov, Jackie Lin

import csv
import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/occupyflaskst')  # returns html page with table of occupations
def occupyflaskst():
    job_dict = dict()

    with open('static/occupations.csv') as file:
        next(file)  # skips first line
        reader = csv.reader(file)  # from imports
        for row in reader:
            job_dict[row[0]] = (float(row[1]), (row[2]))  # key is title and value is a tuple consisting of percentage and links
    del job_dict['Total']  # remove last line

    # lambda is shorthand for a function, lets you write fxn on one line
    # uses random.choices method, which takes values from a list as parameter 1 and weights as parameter 2 and chooses a random one
    # for loop just says for every entry in the dictionary, extract this value
    # the population/given list is taking from each entry the name of the occupation, i, and the link, which is the second index of the tuple
    # the weight is taking from each entry the first index of the tuple where percentage is stored)
    # k = 1 selects one item
    # function returns the name and link of the occupation in the form of ANOTHER tuple
    random_sel = lambda: random.choices(population=[(i, job_dict[i][1]) for i in list(job_dict.keys())],
                                        weights=[i[0] for i in list(job_dict.values())], k=1)[0]

    return render_template('listpage.html',
                           jobs=job_dict.items(),
                           rand_job=random_sel(),
                           title='Occupations')  # passes in dictionary and randomly-selected occupations


if __name__ == '__main__':
    app.debug = True
    app.run()
