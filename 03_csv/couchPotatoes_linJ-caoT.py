def createDict():
    dict = {}; #initialize a new dictionary structure
    file = open("occupations.csv", "r") #open up csv file for reading purposes
    content = file.readlines() #parse through file by line
    print(content) #test

createDict();
