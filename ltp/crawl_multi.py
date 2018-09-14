# Juneseok Byun
# byunjuneseok@gmail.com


import googlegeo as gg
import getpath_cj as cj
import utf8manage as um
import apikeychain

from datetime import datetime
import sqlite3
import threading

#temporarily...free licence...


# Setting File name.
def filename(i):
    now = datetime.now()
    name = str(now.year) + str(now.month).zfill(2) + str(now.day) + str(now.hour).zfill(2) + str(now.minute).zfill(2) + 'th_' + str(i)
    return name

def gentrackingnum(start, end, thread_num, thread_id):
    return range(start + thread_id, end + thread_id, thread_num)

def crawl(tracking_number_list, apikey, thread_id):
    
    #Database
    query = "CREATE TABLE IF NOT EXISTS position(pathnum, pathorder, name, time, lat, lng)"
    conn = sqlite3.connect(filename(thread_id) + '.db')
    curs = conn.cursor()
    curs.execute(query)

    for i in tracking_number_list:
        add = str(i)
        pathlist, datelist = cj.cj_listreturn(add)
        l = len(pathlist)
        if len(pathlist) == 0:
            pass
        for k in range(0, l):
            coordinate = gg.getCoordinate(pathlist[k], apikey)
            if coordinate == [0, 0]:
                coordinate = gg.getCoordinate(um.cutKorean(pathlist[k],2), apikey)
            if coordinate == [0, 0]:
                pass
            values = [(i, k, pathlist[k], datelist[k], coordinate[0], coordinate[1])]

            print(values)
            curs.executemany('INSERT INTO position VALUES(?,?,?,?,?,?)', values)
            conn.commit()

    conn.close()
    print("Thread " + str(thread_id) + " is end.")

def main(start, end):
    #Threadings!
    threads = []

    # 2 is the numbers of threads
    for id in range(0, 2):
#        t = threading.Thread(target=crawl, args=(gentrackingnum(617601330752, 617982212582, 2, id), apikey[id], id))

        t = threading.Thread(target=crawl, args=(gentrackingnum(start, end, 2, id), apikeychain.apikey[id], id))

        threads.append(t)

    #TO-DO!
    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main(617601330752, 617982212582)
