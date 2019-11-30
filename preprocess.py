#preprocess program



#freewifi.csv open_수영

#csv 파일에서 도로명주소, 장소 이름 추출_수영

#도로명주소->좌표 변환 API 사용_수영

#여기까지 만든 뒤 위도 경도 이름 세 가지 변수에 저장해두면 내가 지도에 추가하는거 만들어줄께


#folium 이용해 map에 핀 추가_재연

#HTML로 저장 후 gui로 preprocess done 메세지 출력_재연

import csv

free_wifi = open('freewifi.csv', 'r', encoding= 'cp949')
rdr = csv.reader(free_wifi)
mywifi = [row for idx, row in enumerate(rdr) if idx in range(1, 3)]


for wifi in mywifi:
    wifiName=wifi[0]
    wifiLocation=wifi[8]

