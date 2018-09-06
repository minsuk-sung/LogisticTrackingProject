import folium
import sqlite3

import rgbmanage as rm
#data = [(i, k, pathlist[k], datelist[k], coordinate[0], coordinate[1])]


def validarea(x):
    return (33 < x[4]) and (x[4] < 38) and (124 < x[5]) and (x[5] < 132)


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
conn = sqlite3.connect('path_cj_6660210000.db')
curs = conn.cursor()
curs.execute("SELECT * FROM position")

data = curs.fetchall()

map_osm = folium.Map(location = [37.667588, 126.12986])

print(len(data))

'''
for x in range(0, len(data)):
    print(x)
    if data[x][1] == 0:
        startingTime = int(data[x][3])
        y = x
        while data[y][0] == data[y+1][0]:
            endingTime = int(data[y][3])
            y = y + 1
        duration = endingTime - startingTime
        print(duration)


    if data[x][0] != data[x+1][0]:
        pass
    else:
        currentTime = int(data[x][3]) - startingTime
        durationrate = currentTime / duration
        
        print(data[x], durationrate, currentTime, duration)
        colordensity = rm.reddensity(durationrate)
        folium.PolyLine(
            ([data[x][4], data[x][5]],
            [data[x+1][4], data[x+1][5]]
        ),color=colordensity, opacity=0.4).add_to(map_osm)

        
'''
for x in range(0, len(data)):
    print(x)
    if x == 2017:
        break

    if data[x][1] == 0:
        startingTime = int(data[x][3])
        y = x
        while data[y][0] == data[y+1][0]:
            endingTime = int(data[y][3])
            y = y + 1
        duration = endingTime - startingTime
        print(duration)


    if data[x][0] != data[x+1][0]:
        '''x번째 포인트가 경로의 끝점이다'''
        pass
    else:
        if validarea(data[x]) and validarea(data[x+1]):
            currentTime = int(data[x][3]) - startingTime
            durationrate = currentTime / duration
            
            print(data[x], durationrate, currentTime, duration)
            colordensity = rm.reddensity(durationrate)
            folium.PolyLine(
                ([data[x][4], data[x][5]],
                [data[x+1][4], data[x+1][5]]
            ),color=colordensity, weight = 0.8, opacity=0.2).add_to(map_osm)
            map_osm.save('map1_s.html')
        else:
            pass
