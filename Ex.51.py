# PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first cool GUI')
        self.setGeometry(300, 300, 700, 700)
        self.setWindowIcon(QIcon('Niko.jpg'))

        label = QLabel("Hello", self)
        label.setFont(QFont('Arial', 20))
        label.setGeometry(0, 0, 700, 100)
        label.setStyleSheet("color: #100C01;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        # (You can use the RGB value or # value for specific color

        # label.setAlignment(Qt.AlignmentFlag.AlignTop) # Vertically Top
        # label.setAlignment(Qt.AlignmentFlag.AlignBottom) # Vertically Bottom
        # label.setAlignment(Qt.AlignmentFlag.AlignVCenter) # Vertically Center

        # label.setAlignment(Qt.AlignmentFlag.AlignRight) # Horizontally Right
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter) # Horizontally Center
        # label.setAlignment(Qt.AlignmentFlag.AlignLeft) # Horizontally Left

        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom) # Center & Bottom
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Center & Center
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) # Center & Center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()