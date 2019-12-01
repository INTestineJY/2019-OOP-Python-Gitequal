import sys
import json
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

with open('data.json') as data_file:
    data = json.load(data_file)