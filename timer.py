import sys
import time
import threading

from pynput import keyboard

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer

from scramble import scramble_3x3


class TimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1080, 720)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        self.create_scramble_label()
        self.create_time_label()
        self.create_timer()



    def keyPressEvent(self, event):
        if not self.timer.isActive() and event.key() == Qt.Key_Space:
            self.timer_ready()
        elif self.timer.isActive():
            self.timer.stop()

            if time.time() - self.start_time > 0.1:
                self.reset()


    def keyReleaseEvent(self, event):
        if not self.timer.isActive() and event.key() == Qt.Key_Space and not self.timer_stopped:
            self.start_time = time.time()
            self.timer.start(10)


    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        self.time_label.setStyleSheet('font-size: 300px; color: black')
        self.time_label.setText(f"{elapsed_time:.1f}")


    def create_scramble_label(self):
        self.scramble_label = QLabel(scramble_3x3(), self)
        self.scramble_label.setStyleSheet('font-size: 30px')
        self.layout.addWidget(self.scramble_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
    
    
    def create_time_label(self):
        self.time_label = QLabel('0.0', self)
        self.time_label.setStyleSheet('font-size: 200px')
        self.layout.addWidget(self.time_label, alignment=Qt.AlignCenter)
    

    def create_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer_stopped = False
    

    def timer_ready(self):
        self.timer_stopped = False
        self.scramble_label.hide()
        self.time_label.setStyleSheet('font-size: 300px; color: green')
        self.time_label.setText('0.0')


    def reset(self):
        self.timer_stopped = True
        self.scramble_label.setText(scramble_3x3())
        self.scramble_label.show()
        self.time_label.setStyleSheet('font-size: 200px')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimerWindow()
    window.show()
    sys.exit(app.exec_())
