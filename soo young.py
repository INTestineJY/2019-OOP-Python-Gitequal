import requests
import json

class WIFI :
    def __init__(self):
        pass

    def juso_to_coor(self, address):
        self.address = address
        self.from_site = requests.get('http://apis.vworld.kr/new2coord.do?q='+address+'&apiKey=4BC8BA59-D75D-3BF2-AF93-A0730B4E148E&domain=http://map.vworld.kr/&output=json')
        self.coordinates = self.from_site.json()
        self.X = float(self.coordinates['EPSG_4326_X'])
        self.Y = float(self.coordinates['EPSG_4326_Y'])

my_home = WIFI()
my_school = WIFI()

my_home.juso_to_coor('서울특별시 노원구 노원로 62(공릉동, 효성화운트빌')
print(my_home.X)
print(my_home.Y)
'''

import json

with open('wifidata.json', ) as f:
    root = json.load(f)
'''