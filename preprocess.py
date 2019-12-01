#preprocess program



#freewifi.csv open_수영

#csv 파일에서 도로명주소, 장소 이름 추출_수영

#도로명주소->좌표 변환 API 사용_수영

#여기까지 만든 뒤 위도 경도 이름 세 가지 변수에 저장해두면 내가 지도에 추가하는거 만들어줄께

#folium 이용해 map에 핀 추가_재연

#HTML로 저장 후 gui로 preprocess done 메세지 출력_재연

import csv
import folium
import requests
import webbrowser

class free_wifi :
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.lati = latitude #lati는 위도
        self.longi = longitude #longi는 경도

    def juso_to_coor(self, address): #도로명 주소 넣으면 위도 경도 찾아주는 거긴 한데 일단 안 쓴 코드
        self.from_site = requests.get(
            'http://apis.vworld.kr/new2coord.do?q=' + self.address + '&apiKey=4BC8BA59-D75D-3BF2-AF93-A0730B4E148E&domain=http://map.vworld.kr/&output=json')
        self.coordinates = self.from_site.json()
        self.X = float(self.coordinates['EPSG_4326_X'])
        self.Y = float(self.coordinates['EPSG_4326_Y'])

wifi_file = open('freewifi.csv', 'r', encoding= 'cp949')
rdr = csv.reader(wifi_file)
mywifi = [row for idx, row in enumerate(rdr) if idx in range(1, 25419)]

seoul_wifi = []
gyeonggi_wifi = []
chungbuk_wifi = []
chungnam_wifi = []
jeonbuk_wifi = []
jeonnam_wifi = []
gyeongbuk_wifi = []
gyeongnam_wifi = []
jeju_wifi = []
sejong_wifi = []

for wifi in mywifi :
    if wifi[2] == '서울특별시' :
        seoul_wifi.append(free_wifi(wifi[0], wifi[12], wifi[13]))
    elif wifi[2] == '경기도' :
        gyeonggi_wifi.append(free_wifi(wifi[0], wifi[12], wifi[13]))
    elif wifi[2] == '충청북도' :
        chungbuk_wifi.append(free_wifi(wifi[0], wifi[12], wifi[13]))
    elif wifi[2] == '충청남도' :
        chungnam_wifi.append(free_wifi(wifi[0], wifi[12], wifi[13]))
    elif wifi[2] == '전라북도' :
        jeonbuk_wifi.append(free_wifi(wifi[0], wifi[12], wifi[13]))
    elif wifi[2] == '전라남도' :
        jeonnam_wifi.append(free_wifi(wifi[0], wifi[12], wifi[13]))
    elif wifi[2] == '경상북도' :
        gyeongbuk_wifi.append(free_wifi(wifi[0], wifi[12], wifi[13]))
    elif wifi[2] == '경상남도' :
        gyeongnam_wifi.append(free_wifi(wifi[0], wifi[12], wifi[13]))
    elif wifi[2] == '제주특별자치도' :
        jeju_wifi.append(free_wifi(wifi[0], wifi[12], wifi[13]))
    elif wifi[2] == '세종특별자치시':
        sejong_wifi.append(free_wifi(wifi[0], wifi[12], wifi[13]))
#wifi_list[csv 파일에서의 순서(0부터)].name, lati, longi로 각각 이름, 위도, 경도 인식 가능

seoul_map = folium.Map([36.6, 128], zoom_start=8)
gyeonggi_map = folium.Map([36.6, 128], zoom_start=8)
chungbuk_map = folium.Map([36.6, 128], zoom_start=8)
chungnam_map = folium.Map([36.6, 128], zoom_start=8)
jeonbuk_map = folium.Map([36.6, 128], zoom_start=8)
jeonnam_map = folium.Map([36.6, 128], zoom_start=8)
gyeongbuk_map = folium.Map([36.6, 128], zoom_start=8)
gyeongnam_map = folium.Map([36.6, 128], zoom_start=8)
jeju_map = folium.Map([36.6, 128], zoom_start=8)
sejong_map = folium.Map([36.6, 128], zoom_start=8)



# for wifi in wifi_list:
#     folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(m)


for wifi in seoul_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(seoul_map)

for wifi in gyeonggi_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(gyeonggi_map)

for wifi in chungbuk_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(chungbuk_map)

for wifi in chungnam_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(chungnam_map)

for wifi in jeonbuk_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(jeonbuk_map)

for wifi in jeonnam_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(jeonnam_map)

for wifi in gyeongbuk_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(gyeongbuk_map)

for wifi in gyeongnam_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(gyeongnam_map)

for wifi in jeju_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(jeju_map)

for wifi in sejong_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(sejong_map)


seoul_map.save("map/seoul_map.html")
gyeonggi_map.save("map/gyeonggi_map.html")
chungbuk_map.save("map/chungbuk_map.html")
chungnam_map.save("map/chungnam_map.html")
jeonbuk_map.save("map/jeonbuk_map.html")
jeonnam_map.save("map/jeonnam_map.html")
gyeongbuk_map.save("map/gyeongbuk_map.html")
gyeongnam_map.save("map/gyeongnam_map.html")
jeju_map.save("map/jeju_map.html")
sejong_map.save("map/sejong_map.html")

html_file='sejong_map.html'



webbrowser.open(html_file)

