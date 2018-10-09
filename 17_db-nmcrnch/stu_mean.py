#Real Fact 720 -- Angela Tom & Dennis Chen
#SoftDev1 pd 6
#K17: Average
#10/6/18

import sqlite3
import csv


#========Initializing Files========

DB_FILE="database.db"
db = sqlite3.connect(DB_FILE)
db.text_factory = str
c = db.cursor()                           #allows sqlite to be used on database.db


#==========Function for making a table from csv==========

def makeTable(filename):
    with open(filename, 'r') as csvfile:  #opens database
        reader = csv.DictReader(csvfile)  #creates sequence of dictionaries
        num = 0                           #used to determine if row is first row
        col1 = ""                         #initializes column strings
        col2 = ""
        col3 = ""
        for row in reader:                #goes through each row, adds to table
            if num == 0:                  #if row is first row, names columns based on csv file, uses list of keys to access header names
                col1 = list(row.keys())[0] 
                col2 = list(row.keys())[1]
                col3 = list(row.keys())[2]
                c.execute("CREATE TABLE " + filename[0:-4] + "(" +col1+ "  TEXT, " + col2+ " INTEGER, " +col3+" INTEGER)")  #creates table
                num = num + 1             #increments to indicate first row has been passed
            params = (row[col1],row[col2],row[col3])                                 #creates params for values using row dictionary and column names  
            c.execute("INSERT INTO " + filename[0:-4] + " VALUES(?, ?, ?)", params)  #inserts values in each row into the table
def average():
    #creates a list of the names and grades of the students
    command = 'SELECT name,mark FROM peeps,courses WHERE courses.id = peeps.id'
    cur = c.execute(command)
    tab = cur.fetchall()
    #print(tab)
    #creates a list of names
    command = 'SELECT name from peeps'
    cur = c.execute(command)
    tabl = cur.fetchall()
    #creates a list of ids
    command = 'Select id from peeps'
    cur = c.execute(command)
    #creates a dictionary where the keys are the student names and value is a empty list
    names = dict()
    for each in tabl:
        names[each[0]] = []
    #print(names)
    #puts each student's grades into the empty list in the dictionary
    for name in tab:
        names[name[0]].append(name[1])
    #print(names)
    #replaces the list of grades with a list of their average and id
    for name in names:
        id = cur.fetchone()[0]
        names[name] = [float("{0:.2f}".format(sum(names[name]) / (float(len(names[name]))))),id]
    print(names)
    return names
    
def createIDTable():
    avgD = average() # dictionary of the averages
    c.execute("CREATE TABLE peeps_avg (id INTEGER, average FLOAT)") # create the peeps_avg table
    for values in avgD.values(): 
        id = values[1] 
        #print (id);
        avg = values[0]
        #print (avg)
        params = (id, avg)
        c.execute("INSERT INTO peeps_avg VALUES (?, ?)", params) # fill up the table with id and values

def addRows(code, mark, id):
    params = (code, mark, id)
    c.execute("INSERT INTO courses VALUES (?,?,?)", params)
#==================Calling functions for file names used, saving changes=====================


makeTable("courses.csv")
makeTable("peeps.csv")
print(average())
createIDTable()
addRows("S", 10, 0)
db.commit()       #save changes
db.close()        #close database




