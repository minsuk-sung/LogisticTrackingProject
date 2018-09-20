import folium
import sqlite3
import rgbmanage as rm

#data = [(i, k, pathlist[k], datelist[k], coordinate[0], coordinate[1])]


def validarea(x):
    return (33 < x[4]) and (x[4] < 38) and (124 < x[5]) and (x[5] < 132)


def main(dbfile):
    '''
    l = len(testdata)

    startingTime = int(testdata[0][3])
    endingTime = int(testdata[l-1][3])
    duration = endingTime - startingTime

    map_osm = folium.Map(location = [37.667588, 126.12986])

    for i in range(1, l):
        currentTime = int(testdata[i][3]) - startingTime
        durationrate = currentTime / duration
        colordensity = rm.reddensity(durationrate)
        folium.PolyLine(([testdata[i][4], testdata[i][5]], [testdata[i-1][4], testdata[i-1][5]]),color=colordensity, opacity=0.4).add_to(map_osm)
        map_osm.save('map1.html')
        '''

    #Database

    conn = sqlite3.connect(dbfile)
    curs = conn.cursor()
    curs.execute("SELECT * FROM position")
    data = curs.fetchall()

    #create map. (first view is Seoul)
    map_osm = folium.Map(location = [37.667588, 126.12986])

    print("[SUCCESS] READ DATA FROM", dbfile, "AND THE DATA SIZE IS", len(data))

    #### data = [(i, k, pathlist[k], datelist[k], coordinate[0], coordinate[1])]
    ####

    tracknumbefore = 0
    path = []

    for x in range(0, len(data) - 1):
        print("[PROGRESS]", x, "/", len(data))
        if tracknumbefore !=  data[x][0]:

            color = rm.randomcolor()
            for edge in path:
                folium.PolyLine(edge, color=color, weight=0.8, opacity=0.3).add_to(map_osm)
            path = []

        else:
            '''do nothing'''

        if validarea(data[x]) and validarea(data[x+1]):
            path.append([[data[x][4], data[x][5]], [data[x+1][4], data[x+1][5]]])

        else:
            print('[WARNING] INVALID PATH DETECTED')
            pass

    print('save')
    map_osm.save('map1_s.html')



if __name__ == "__main__":
    main('test_db.db')