#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
peepsL = []
with open('data/peeps.csv') as infile:
    peepsR = csv.DictReader(infile)
    for row in peepsR:
        peepsL.append([row['name'], row['age'], row['id'])
    
with open('data/courses.csv') as infile:
    coursesR = csv.DictReader(infile)

print(peepsR)

command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER);"


#build SQL stmt, save as string

c.execute(command)    #run SQL statement
c.execute("SELECT * FROM peeps;")

#==========================================================

db.commit() #save changes
db.close()  #close database


