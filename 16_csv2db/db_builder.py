#Random Team Name -- Angela Tom, Kyle Tau
#SoftDev1 pd6
#K16 -- No Trouble
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
peepsL = []
with open('data./peeps.csv') as infile:
    peepsR = csv.DictReader(infile)
    for row in peepsR:
        peepsL.append([row['name'], row['age'], row['id']])
coursesL = []
with open('data/courses.csv') as infile:
    coursesR = csv.DictReader(infile)
    for row in coursesR:
        coursesL.append([row['code'], row['mark'], row['id']])

print(peepsL)
print(coursesL)

for x in peepsL:
    for x in range:


command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER);"          #build SQL stmt, save as string
c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


