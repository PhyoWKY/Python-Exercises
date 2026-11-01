# PyQt5 interactive button

import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first cool GUI')
        self.setGeometry(300, 300, 700, 700)
        self.setWindowIcon(QIcon('Niko.jpg'))
        self.button = QPushButton('Click Me :)', self)
        self.label = QLabel('Hello', self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(250, 250, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        # This 'self' is to make a class belongs to the main window

        self.label.setGeometry(250, 400, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        self.label.setText("GoodBye!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()