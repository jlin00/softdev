import random

#shortened list of names to test out function
KREWES = {
    'orpheus': ['Emily', 'Kevin', 'Vishwaa'],
    'rex': ['William', 'Joseph', 'Calvin'],
    'endymion': ['Grace', "Nahi", 'Derek']
}

def randomName(team):
    print (KREWES[team][random.randint(0, len(KREWES[team]) - 1)])
    #references the team specified by the parameter, then obtains a random number based on the team's length and returns the name at that index

#tests
#randomName('orpheus')
#randomName('rex')
#randomName('endymion')

#different from first function because it does not need team as a parameter, automatically chooses a random team and random name
#this method was explained to me by Peihua Huang from period 2
def randomName(dict):
    teams = list(dict.keys()) #turns dictionary into list
    period = random.choice(teams) #chooses a random index from that list
    print(random.choice(dict[period])) #prints a random index from chosen team

#tests
for i in range(0, 10):
    randomName(KREWES)
