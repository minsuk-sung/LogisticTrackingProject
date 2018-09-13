# JUNESEOK BYUN @juneseokdev.me
import googlegeo as gg
import getpath_cj as cj
import utf8manage as um
from datetime import datetime

import sqlite3


# Setting File name.
now = datetime.now()
filename = str(now.year) + str(now.month).zfill(2) + str(now.day) + str(now.hour).zfill(2) + str(now.minute).zfill(2)
print(filename)

#Database
conn = sqlite3.connect(filename + '.db')
curs = conn.cursor()
curs.execute('create table position(pathnum, pathorder, name, time, lat, lng)')




for i in range(617601330752, 617982212582):
    add = str(i)
    pathlist, datelist = cj.cj_listreturn(add)
    l = len(pathlist)
    if len(pathlist) == 0:
        pass
    for k in range(0, l):
        coordinate = gg.getCoordinate(pathlist[k])
        if coordinate == [0, 0]:
            coordinate = gg.getCoordinate(um.cutKorean(pathlist[k],2))
        if coordinate == [0, 0]:
            pass
        values = [(i, k, pathlist[k], datelist[k], coordinate[0], coordinate[1])]

        print(values)
        curs.executemany('insert into position values(?,?,?,?,?,?)', values)
        conn.commit()

conn.close()