import sys
import json
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
html_dict = {'gangwon': "map/gangwon_map.html", 'gyeonggi': "map/gyeonggi_map.html",
             'chungbuk': "map/chungbuk_map.html", 'chungnam': "map/chungnam_map.html",
             'jeonbuk': "map/jeonbuk_map.html", 'gyeongbuk': "map/gyeongbuk_map.html",
             'gyeongnam': "map/gyeongnam_map.html", 'jeonnam': "map/jeonnam_map.html",
             'seoul': "map/seoul_map.html", 'sejong': "map/sejong_map.html",
             'busan': "map/busan_map.html", 'ulsan': "map/ulsan_map.html",
             'incheon': "map/incheon_map.html", 'daejeon': "map/daejeon_map.html",
             'daegu': "map/daegu_map.html", 'gwangju': "map/gwangju_map.html",
             'jeju': "map/jeju_map.html"}


# with open('data.json') as data_file:
#     data = json.load(data_file)
#
# pprint(data)
# #값 하나하나씩 접근
# data["map_dict"][0]['gangwon']
# data["map_dict"][0]['gyeonggi']
# data["map_dict"][0]['chungbuk']
# data["map_dict"][0]['chungnam']
# data["map_dict"][0]['jeonbuk']
# data["map_dict"][0]['gyeongbuk']
# data["map_dict"][0]['gyeongnam']
# data["map_dict"][0]['jeonnam']
# data["map_dict"][0]['seoul']
# data["map_dict"][0]['sejong']
# data["map_dict"][0]['busan']
# data["map_dict"][0]['ulsan']
# data["map_dict"][0]['incheon']
# data["map_dict"][0]['daejeon']
# data["map_dict"][0]['daegu']
# data["map_dict"][0]['gwangju']
# data["map_dict"][0]['jeju']


