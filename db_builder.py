#!usr/bin/python
'''
Brian Leung
PD 7 SoftDev
(
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
f = "dab.db"
command = ""

csvfile = open("peeps.csv",'rb')
reader = csv.DictReader(csvfile)

command = 'CREATE TABLE peeps(code TEXT, mark INTEGER, id INTEGER)'
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
c.execute(command)
for row in reader:
	command = 'INSERT INTO peeps VALUES("%s",%s,%s)' % (row['name'], row['age'], row['id'])
	c.execute(command)

csvfile = open("courses.csv","rb")
reader = csv.DictReader(csvfile)
command = 'CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)'
c.execute(command)
for row in reader:
	command = 'INSERT INTO courses VALUES("%s",%s,%s)' % (row['code'], row['mark'], row['id'])
	c.execute(command)

#c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database
