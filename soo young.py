'''

import requests

class WIFI :
    def __init__(self, address):
        self.address = address
        self.from_site = requests.get('http://apis.vworld.kr/new2coord.do?q='+address+'&apiKey=4BC8BA59-D75D-3BF2-AF93-A0730B4E148E&domain=http://map.vworld.kr/&output=json')
        self.coordinates = self.from_site.json()
        self.X = float(self.coordinates['EPSG_4326_X'])
        self.Y = float(self.coordinates['EPSG_4326_Y'])

my_home = WIFI("서울특별시 노원구 노원로 62(공릉동, 효성화운트빌)")
my_school = WIFI("세종특별자치시 달빛1로 265(아름동 산8)")

print(my_home.X)
print(my_home.Y)

'''

'''
import requests
import urllib
import urllib3
api_key = 'mX0iqozucA3VWvrS9Os0wF77AYYh6uweensxj8KBTOIxfa5BCkUuNGp%2BHtQc0CpDy56LSHHmw4QW833qfg2aBQ%3D%3D'
url = 'http://api.data.go.kr/openapi/free-wrlsfd-std?serviceKey='+api_key+'&type=json&&totalCount=1'

request = requests.get(url)
rescode = request.getcode(url)
print(rescode)
print(request.json())
'''

import urllib
import requests
import json
from pprint import pprint

ServiceKey = "mX0iqozucA3VWvrS9Os0wF77AYYh6uweensxj8KBTOIxfa5BCkUuNGp%2BHtQc0CpDy56LSHHmw4QW833qfg2aBQ%3D%3D"
url = "http://api.data.go.kr/openapi/free-wrlsfd-std"
result = requests.get(url+'?'+ServiceKey+"&type=json"+"&instlCtprvnNm=서울특별시")
print(result.json())