import csv
import random

job_dict = dict()


with open('static/occupations.csv') as file: #opens csv file
    next(file) #skips first line
    reader = csv.reader(file)
    for row in reader: #iterates through each row in file
        job_dict[row[0]] = float(row[1]) #adds entry in dictionary
del job_dict['Total'] #delete last row


random_sel = lambda: random.choices(population=list(job_dict.keys()), weights=list(job_dict.values()), k=1)[0]
#uses the choices function, which takes in the keys as options and weights them, then chooses a random one and returns the job title
