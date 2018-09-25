#Team Penguins -- Kevin Lin, Angela Tom
#SoftDev Pd6
#K10 -- Jinja Tuning
#2018-09-24

import csv, random

def selectRandOccupation():
    reader = csv.reader(open('data/occupations.csv')) #opens and reads the csv file
    next(reader) # skips the headers
    d={} #intialized the dictionary
    for row in reader: #iterates through the csv file and updates the dictionary accordingly
        d[row[0]]=float(row[1])
        d.pop("Total", 0) # gets rid of the last row
    occupations = list(d.keys()) #makes a list of all the occupations
    percentages = list(d.values()) #makes a list of all the percentages
    result = random.choices(occupations, percentages)
    #returns a list of size 1 with a random occupation choosen based on the percentages
    ans = result.pop() #returns the only element in the list
    return ans
	
def createTable():
    lst = [] 
    with open('data/occupations.csv') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            lst.append([row['Job Class'], row['Percentage']])
    return lst
			 
