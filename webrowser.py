from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('BleedMySelfBrowser')
        self.setWindowIcon(QIcon('broken-heart.png'))

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar('Navigation')
        navtb.setIconSize(QSize(16, 16))
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect('')
        navtb.addWidget(self.urlbar)

        

        

        

app = QApplication(sys.argv)
window = MainWindow()
app.setApplicationName('BleedMySelfBrowser')
window.show()
app.exec_()
