# JUNESEOK BYUN @juneseokdev.me
import googlegeo as gg
import getpath_cj as cj
import utf8manage as um

import sqlite3

#Database
conn = sqlite3.connect('path_cj_3.db')
curs = conn.cursor()
curs.execute('create table position(pathnum, pathorder, name, time, lat, lng)')

for i in range(6660214363, 6660220000):
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