import pymongo
import sqlite3


def validarea(x):
    return (33 < x[4]) and (x[4] < 38) and (124 < x[5]) and (x[5] < 132)



connection = pymongo.MongoClient("localhost", 27017)
db = connection.CJ
collection  = db.testCollection

#sqlite3
conn = sqlite3.connect('path_cj_6660210000.db')
curs = conn.cursor()
curs.execute("SELECT * FROM position")
litedata = curs.fetchall()

for x in litedata:
    if validarea(x):
        path = {'lat' : x[4], 'lng' : x[5], 'time' : x[3], 'name' : x[2], 'pathno' : x[0], 'order' : x[1]}
        print(path)
        collection.insert(path)
    else:
        pass