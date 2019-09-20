import csv
import random

job_dict = dict()


with open('static/occupations.csv') as file:
    next(file)
    reader = csv.reader(file)
    for row in reader:
        job_dict[row[0]] = float(row[1])
del job_dict['Total']


random_sel = lambda: random.choices(population=list(job_dict.keys()), weights=list(job_dict.values()), k=1)[0]
