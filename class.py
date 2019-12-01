import requests
import json1

class inputtomap():
    def __init__(self):
        pass
    def jusotocoorwheninput(self, address):
        self.address = address
        self.from_site = requests.get('http://apis.vworld.kr/new2coord.do?q='+address+'&apiKey=4BC8BA59-D75D-3BF2-AF93-A0730B4E148E&domain=http://map.vworld.kr/&output=json')
        self.coordinates = self.from_site.json()
        try:
            self.X = float(self.coordinates['EPSG_4326_X'])
            self.Y = float(self.coordinates['EPSG_4326_Y'])
        except KeyError:
            print("입력하신 것과 일치하는 도로명주소가 없습니다")
            newadress = input('지도에 새로 추가시킬 장소의 도로명주소를 다시 입력해주세요\n-->')
            wifiadd.jusotocoorwheninput(newadress)
    # def coortomap(self, x, y):
    #

wifiadd = inputtomap()
newadress = input('지도에 새로 추가시킬 장소의 도로명주소를 입력해주세요\n-->')
wifiadd.jusotocoorwheninput(newadress)
print(wifiadd.X)
print(wifiadd.Y)