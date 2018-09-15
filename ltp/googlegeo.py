#-*- encoding: utf-8 -*-
# JUNESEOK BYUN @juneseokdev.me
import apikeychain

import folium
import json
#from bs4 import BeautifulSoup

import requests
import time

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

    elif checkQuota(resp_json_payload):
        return [0, 0]

    else:
        point = resp_json_payload['results'][0]['geometry']['location']
        lat = point['lat']
        lng = point['lng']
        return [lat, lng]

def checkZero(x):
    return x['status'] == 'ZERO_RESULTS'

def checkQuota(x):
    return 'error_message' in x

def testcode(apikeylist):
    for id in range(len(apikeylist)):
        x = getCoordinate('상수역', apikeylist[id])
        if ((33 < x[0]) and (x[0] < 38) and (124 < x[1]) and (x[1] < 132)):
            print('[PASSED] API KEY', id, ':', x)
        else:
            print('[FAILED] API KEY', id, 'IS INVALID.')

if __name__ == "__main__":
    testcode(apikeychain.apikey)