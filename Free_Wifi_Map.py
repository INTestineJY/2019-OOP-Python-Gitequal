import sys
import webbrowser
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




webbrowser.open(html_dict['sejong'])





