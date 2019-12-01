import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


html_dict = {'033': "map/gangwon_map.html", '031': "map/gyeonggi_map.html",
             '043': "map/chungbuk_map.html", '041': "map/chungnam_map.html",
             '063': "map/jeonbuk_map.html", '054': "map/gyeongbuk_map.html",
             '055': "map/gyeongnam_map.html", '061': "map/jeonnam_map.html",
             '02': "map/seoul_map.html", '044': "map/sejong_map.html",
             '051': "map/busan_map.html", '052': "map/ulsan_map.html",
             '032': "map/incheon_map.html", '042': "map/daejeon_map.html",
             '053': "map/daegu_map.html", '062': "map/gwangju_map.html",
             '064': "map/jeju_map.html"}


Text = ""

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(448, 40)

        qle = QLineEdit(self)
        qle.move(408, 300)
        qle.textChanged[str].connect(self.onChanged)


        btn = QPushButton('Enter', self)
        btn.move(448, 400)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('MAP')
        self.setWindowIcon(QIcon('map.png'))
        self.resize(960, 540)
        self.show()

    def onChanged(self, text):
        global Text
        self.lbl.setText(text)
        self.lbl.adjustSize()
        print(text)
        Text = text

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec()


try:
    webbrowser.open(html_dict[Text])
except KeyError:
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyApp()
        app.exec ()
