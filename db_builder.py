#!usr/bin/python
'''
Brian Leung
PD 7 SoftDev

'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

csvfile = open("testcase.csv",'rb')
reader = csv.reader(csvfile)
redRow = reader.next()
pr
("")
redRo[0] = 
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

000
command = ""          #put SQL statement in this string
c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database
