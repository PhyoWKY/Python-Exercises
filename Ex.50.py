# Intro to PyQt5 GUI(Graphical User Interface)

import sys
# This sys(system) module import some variables used by Python interpreter

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first cool GUI')
        self.setGeometry(300, 300, 700, 700)
                      # (x, y, width, height) in pixels
        self.setWindowIcon(QIcon('Niko.jpg'))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()