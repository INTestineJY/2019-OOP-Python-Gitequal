#preprocess program



#freewifi.csv open_수영

#csv 파일에서 도로명주소, 장소 이름 추출_수영

#도로명주소->좌표 변환 API 사용_수영

#여기까지 만든 뒤 위도 경도 이름 세 가지 변수에 저장해두면 내가 지도에 추가하는거 만들어줄께


#folium 이용해 map에 핀 추가_재연

#HTML로 저장 후 gui로 preprocess done 메세지 출력_재연

import csv
import requests

class free_wifi :
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.lati = latitude #lati는 위도
        self.longi = longitude #longi는 경도

    def juso_to_coor(self, address): #도로명 주소 넣으면 위도 경도 찾아주는 거긴 한데 일단 안 쓴 함수
        self.from_site = requests.get(
            'http://apis.vworld.kr/new2coord.do?q=' + address + '&apiKey=4BC8BA59-D75D-3BF2-AF93-A0730B4E148E&domain=http://map.vworld.kr/&output=json')
        self.coordinates = self.from_site.json()
        self.X = float(self.coordinates['EPSG_4326_X'])
        self.Y = float(self.coordinates['EPSG_4326_Y'])

wifi_file = open('freewifi.csv', 'r', encoding= 'cp949')
rdr = csv.reader(wifi_file)
mywifi = [row for idx, row in enumerate(rdr) if idx in range(1, 25419)]

wifi_list = []
for wifi in mywifi :
    wifi_list.append(free_wifi(wifi[0], wifi[12], wifi[13]))
#wifi_list[csv 파일에서의 순서(0부터)].name, lati, longi로 각각 이름, 위도, 경도 인식 가능

print(wifi_list[0].name, wifi_list[0].lati, wifi_list[0].longi) #사용 예시