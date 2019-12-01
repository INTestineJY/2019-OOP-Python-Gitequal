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
import json
from collections import OrderedDict

file_data = OrderedDict()

class free_wifi :
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.lati = latitude #lati는 위도
        self.longi = longitude #longi는 경도

    def juso_to_coor(self, address): #도로명 주소 넣으면 위도 경도 찾아주는 거긴 한데 일단 안 쓴 코드
        self.from_site = requests.get(
            'http://apis.vworld.kr/new2coord.do?q=' + address + '&apiKey=4BC8BA59-D75D-3BF2-AF93-A0730B4E148E&domain=http://map.vworld.kr/&output=json')
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
gangwon_wifi = []
busan_wifi = []
ulsan_wifi = []
daegu_wifi = []
incheon_wifi = []
gwangju_wifi = []
daejeon_wifi = []

def wifi_add(check, wifi_list, wifi):
    if wifi[2] == check :
        wifi_list.append(free_wifi(wifi[0], wifi[12], wifi[13]))

for wifi in mywifi :
    wifi_add('서울특별시', seoul_wifi, wifi)
    wifi_add('경기도', gyeonggi_wifi, wifi)
    wifi_add('충청북도', chungbuk_wifi, wifi)
    wifi_add('충청남도', chungnam_wifi, wifi)
    wifi_add('전라북도', jeonbuk_wifi, wifi)
    wifi_add('전라남도', jeonnam_wifi, wifi)
    wifi_add('경상북도', gyeongbuk_wifi, wifi)
    wifi_add('경상남도', gyeongnam_wifi, wifi)
    wifi_add('제주특별자치도', jeju_wifi, wifi)
    wifi_add('세종특별자치시', sejong_wifi, wifi)

    wifi_add('강원도', gangwon_wifi, wifi)
    wifi_add('부산광역시', busan_wifi, wifi)
    wifi_add('울산광역시', ulsan_wifi, wifi)
    wifi_add('대전광역시', daejeon_wifi, wifi)
    wifi_add('광주광역시', gwangju_wifi, wifi)
    wifi_add('인천광역시', incheon_wifi, wifi)
    wifi_add('대구광역시', daegu_wifi, wifi)

    '''
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
'''


#     wifi_add('강원도', gangwon_wifi, wifi)
#     wifi_add('부산광역시', busan_wifi, wifi)
#     wifi_add('울산광역시', ulsan_wifi, wifi)
#     wifi_add('대전광역시', daejeon_wifi, wifi)
#     wifi_add('광주광역시', gwangju_wifi, wifi)
#     wifi_add('인천광역시', incheon_wifi, wifi)
#     wifi_add('대구광역시', daegu_wifi, wifi)


seoul_map = folium.Map([37.540705, 126.956764], zoom_start=11)
gyeonggi_map = folium.Map([37.567167, 127.190292], zoom_start=9)
chungbuk_map = folium.Map([36.628503, 127.929344], zoom_start=9)
chungnam_map = folium.Map([36.557229, 126.779757], zoom_start=9)
jeonbuk_map = folium.Map([35.716705, 127.144185], zoom_start=9)
jeonnam_map = folium.Map([34.819400, 126.893113], zoom_start=9)
gyeongbuk_map = folium.Map([36.248647, 128.664734], zoom_start=9)
gyeongnam_map = folium.Map([35.259787, 128.664734], zoom_start=9)
jeju_map = folium.Map([33.364805, 126.542671], zoom_start=11)
sejong_map = folium.Map([36.5, 127.26667], zoom_start=11)
gangwon_map = folium.Map([37.555837, 128.209315], zoom_start=9)
busan_map = folium.Map([35.198362, 129.053922], zoom_start=11)
ulsan_map = folium.Map([35.519301, 129.239078], zoom_start=11)
daejeon_map = folium.Map([36.321655, 127.378953], zoom_start=11)
gwangju_map = folium.Map([35.126033, 126.831302], zoom_start=11)
incheon_map = folium.Map([37.469221, 126.573234], zoom_start=11)
daegu_map = folium.Map([35.798838, 128.583052], zoom_start=11)



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

for wifi in gangwon_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(gangwon_map)

for wifi in busan_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(busan_map)

for wifi in ulsan_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(ulsan_map)

for wifi in daejeon_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(daejeon_map)

for wifi in gwangju_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(gwangju_map)

for wifi in incheon_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(incheon_map)

for wifi in daegu_wifi:
    folium.Marker([wifi.lati, wifi.longi], popup=wifi.name).add_to(daegu_map)




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
gangwon_map.save("map/gangwon_map.html")
busan_map.save("map/busan_map.html")
ulsan_map.save("map/ulsan_map.html")
daejeon_map.save("map/daejeon_map.html")
gwangju_map.save("map/gwangju_map.html")
incheon_map.save("map/incheon_map.html")
daegu_map.save("map/daegu_map.html")

file_data["map_dict"] = {'gangwon':gangwon_map, 'gyeonggi':gyeonggi_map, 'chungbuk':chungbuk_map, 'chungnam':chungnam_map,
                         'jeonbuk':jeonbuk_map, 'gyeongbuk':gyeongbuk_map, 'gyeongnam':gyeongnam_map, 'jeonnam':jeonnam_map,
                         'seoul':seoul_map, 'sejong':sejong_map, 'busan':busan_map, 'ulsan':ulsan_map, 'incheon':incheon_map,
                         'daejeon':daejeon_map, 'daegu':daegu_map, 'gwangju':gwangju_map, 'jeju':jeju_map}

print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

with open('data.json','w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

# map_dict=[['gangwon',gangwon_map],   ['gyeonggi',gyeonggi_map],   ['chungbuk',chungbuk_map],   ['chungnam',chungnam_map],
#           ['jeonbuk',jeonbuk_map],   ['gyeongbuk',gyeongbuk_map],   ['gyeongnam',gyeongnam_map],   ['jeonnam',jeonnam_map],
#           ['seoul',seoul_map],   ['sejong',sejong_map],   ['busan',busan_map],   ['ulsan',ulsan_map],   ['incheon',incheon_map],
#           ['daejeon',daejeon_map],   ['daegu',daegu_map],   ['gwangju',gwangju_map],   ['jeju',jeju_map]]





