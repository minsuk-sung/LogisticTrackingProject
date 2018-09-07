#-*- encoding: utf-8 -*-
# JUNESEOK BYUN @juneseokdev.me
import folium
import json
import requests
import time
#from bs4 import BeautifulSoup

googleurl = 'https://maps.googleapis.com/maps/api/geocode/json?address='

#temporarily...free licence
googleapi = '&key=AIzaSyD7gj21BMbRtNM7g2eppYav3JTMJfysvkE'


def getGoogleAddress(x):
    keyword = x
    address = googleurl + keyword + googleapi
    return address

def getCoordinate(x):
    time.sleep(1.3)
    url = getGoogleAddress(x)
    response = requests.get(url)
    resp_json_payload = response.json()
    if checkZero(resp_json_payload):
        return [0, 0]
    else:
        point = resp_json_payload['results'][0]['geometry']['location']
        lat = point['lat']
        lng = point['lng']
        return [lat, lng]

def checkZero(x):
    return x['status'] == 'ZERO_RESULTS'

