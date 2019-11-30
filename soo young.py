import requests
import csv

class free_WIFI :
    def __init__(self, address):
        self.address = address

    def juso_to_coor(self):
        self.from_site = requests.get('http://apis.vworld.kr/new2coord.do?q='+self.address+'&apiKey=4BC8BA59-D75D-3BF2-AF93-A0730B4E148E&domain=http://map.vworld.kr/&output=json')
        self.coordinates = self.from_site.json()
        self.X = float(self.coordinates['EPSG_4326_X'])
        self.Y = float(self.coordinates['EPSG_4326_Y'])
#free wifi 는 입력 시에 주소를 받으려고 했으나 open api 트래픽 제한때문에 일단 사용을 안 해봤음

wifi_csv = open('freewifi.csv', 'r', encoding= 'cp949')
read = csv.reader(wifi_csv)
temp_wifi = [row for idx, row in enumerate(read) if idx in range(1, 25419)]

#생각보다 읽는 속도는 얼마 안 걸리는 것 같아
#range (1, 25419)가 처음부터 끝까지 다 읽는 거

free_wifi = [1]
for i in range (1, 30):
    free_wifi.append([temp_wifi[i][1], temp_wifi[i][12], temp_wifi[i][13]])

for i in range(1, 30):
    print(free_wifi[i])
#free_wifi[i] = cxv에서 i번째 행의 [이름, 위도, 경도]