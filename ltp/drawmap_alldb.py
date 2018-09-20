import drawmap
import glob
import folium
import sqlite3
import rgbmanage as rm

def drawmapwithmultifiles(filelist):

    # create map. (first view is Seoul)
    map_osm = folium.Map(location=[37.667588, 126.12986])

    #Database
    for dbfile in filelist:
        conn = sqlite3.connect(dbfile)
        curs = conn.cursor()
        curs.execute("SELECT * FROM position")
        data = curs.fetchall()


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
                    folium.PolyLine(edge, color=color, weight=0.5, opacity=0.1).add_to(map_osm)
                path = []

            else:
                '''do nothing'''

            if drawmap.validarea(data[x]) and drawmap.validarea(data[x+1]):
                path.append([[data[x][4], data[x][5]], [data[x+1][4], data[x+1][5]]])

            else:
                print('[WARNING] INVALID PATH DETECTED')
                pass

    map_osm.save('map1_s.html')


def main():

    files = glob.glob('sqlite_dbdata/*')
    drawmapwithmultifiles(files)

if __name__ == "__main__":
    main()