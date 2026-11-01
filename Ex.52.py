# PyQt5 images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first cool GUI')
        self.setGeometry(300, 300, 700, 700)
        self.setWindowIcon(QIcon('Niko.jpg'))

        label = QLabel(self) # 'label' is the children widget, 'self' is 'window' object and the parent widget
        label.setGeometry(0, 0, 460, 250)

        pixmap = QPixmap('PEAK.webp')
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()