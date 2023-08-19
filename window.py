import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from scramble import scramble_3x3

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 720, 480)

        self.scramble = QLabel(scramble_3x3(), self)
        self.scramble.setGeometry(20, 20, 500, 30)
    

    def time(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
