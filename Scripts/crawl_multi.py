# Juneseok Byun
# byunjuneseok@gmail.com

import googlegeo as gg
import getpath_cj as cj
import utf8manage as um

from datetime import datetime
import sqlite3
import threading

#temporarily...free licence...
apikey = ['&key=AIzaSyD7gj21BMbRtNM7g2eppYav3JTMJfysvkE',
          '&key=AIzaSyDeBDkD0R8QZhpc_tOOwpKy6JZCGzDkJfc']

# Setting File name.
def filename(i):
    now = datetime.now()
    name = str(now.year) + str(now.month).zfill(2) + str(now.day) + str(now.hour).zfill(2) + str(now.minute).zfill(2) + 'th_' + str(i)
    return name

def gentrackingnum(i):
    return range(617601330752 + i, 617982212582 + i, 2)

def crawl(tracking_number_list, apikey, thread_id):
    #Database
    conn = sqlite3.connect(filename(thread_id) + '.db')
    curs = conn.cursor()
    curs.execute('create table position(pathnum, pathorder, name, time, lat, lng)')

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
            curs.executemany('insert into position values(?,?,?,?,?,?)', values)
            conn.commit()

    conn.close()

def main():
    #Threadings!
    threads = []

    # 2 is the numbers of threads
    for id in range(0, 2):
        t = threading.Thread(target=crawl, args=(gentrackingnum(id), apikey[id], id))
        threads.append(t)

    #TO-DO!
    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
