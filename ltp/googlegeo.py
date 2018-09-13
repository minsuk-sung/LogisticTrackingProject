#-*- encoding: utf-8 -*-
# JUNESEOK BYUN @juneseokdev.me
import folium
import json
import requests
import time
#from bs4 import BeautifulSoup

googleurl = 'https://maps.googleapis.com/maps/api/geocode/json?address='

def getGoogleAddress(x, apikey):
    keyword = x
    address = googleurl + keyword + apikey
    return address

def getCoordinate(x, apikey):
    time.sleep(1.3)
    url = getGoogleAddress(x, apikey)
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

