import random

KREWES = {
    'orpheus': ['Emily', 'Kevin', 'Vishwaa'],
    'rex': ['William', 'Joseph', 'Calvin'],
    'endymion': ['Grace', "Nahi", 'Derek']
}

def randomName(team):
    print (KREWES[team][random.randint(0, len(KREWES[team]) - 1)])

randomName('orpheus')
randomName('rex')
randomName('endymion')
