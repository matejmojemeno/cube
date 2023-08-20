import sys
import time
import threading

from pynput import keyboard

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QTimer

from scramble import scramble_3x3


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1080, 720)

        self.scramble_label = QLabel(scramble_3x3(), self)
        self.scramble_label.setGeometry(50, 50, 700, 100)
        self.scramble_label.setStyleSheet('font-size: 30px')
        self.scramble_label.adjustSize()
        self.scramble_label.setAlignment(Qt.AlignCenter)

        self.time_label = QLabel('0.00', self)
        self.time_label.setGeometry(20, 200, 500, 30)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)


    def keyPressEvent(self, event):
        if self.timer.isActive():
            self.timer.stop()
            print('pes')
        elif not self.timer.isActive() and event.key() == Qt.Key_Space:
            self.time_label.setStyleSheet('color: green')
            print('macka')

    def keyReleaseEvent(self, event):
        if not self.timer.isActive() and event.key() == Qt.Key_Space:
            self.start_time = time.time()
            self.timer.start(100)
            self.time_label.setStyleSheet('color: black')


    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        self.time_label.setText(f"{elapsed_time:.2f}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
