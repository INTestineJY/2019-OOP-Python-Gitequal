import sys
import json
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

with open('data.json') as data_file:
    data = json.load(data_file)

pprint(data)
#값 하나하나씩 접근
data["map_dict"][0]['gangwon']
data["map_dict"][0]['gyeonggi']
data["map_dict"][0]['chungbuk']
data["map_dict"][0]['chungnam']
data["map_dict"][0]['jeonbuk']
data["map_dict"][0]['gyeongbuk']
data["map_dict"][0]['gyeongnam']
data["map_dict"][0]['jeonnam']
data["map_dict"][0]['seoul']
data["map_dict"][0]['sejong']
data["map_dict"][0]['busan']
data["map_dict"][0]['ulsan']
data["map_dict"][0]['incheon']
data["map_dict"][0]['daejeon']
data["map_dict"][0]['daegu']
data["map_dict"][0]['gwangju']
data["map_dict"][0]['jeju']


