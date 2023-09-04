import sys
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen

from scramble import scramble_3x3
from scramble_visual import ScrambleVisual


class TimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1920, 1080)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        self.create_scramble_label()
        self.create_time_label()
        self.create_timer()

        self.painted = True

    def keyPressEvent(self, event):
        if not self.timer.isActive() and event.key() == Qt.Key.Key_Space:
            self.timer_ready()
        elif self.timer.isActive():
            self.timer.stop()

            if time.time() - self.start_time > 0.1:
                self.reset()

    def keyReleaseEvent(self, event):
        if (
            not self.timer.isActive()
            and event.key() == Qt.Key.Key_Space
            and not self.timer_stopped
        ):
            self.start_time = time.time()
            self.timer.start(10)

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        self.time_label.setStyleSheet("font-size: 300px; color: white")
        self.time_label.setText(f"{elapsed_time:.1f}s")

    def create_scramble_label(self):
        self.scramble = scramble_3x3()
        self.scramble_label = QLabel(self.scramble, self)
        self.scramble_label.setStyleSheet("font-size: 30px")
        self.layout.addWidget(
            self.scramble_label,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter,
        )

    def create_time_label(self):
        self.time_label = QLabel("0.0s", self)
        self.time_label.setStyleSheet("font-size: 200px")
        self.layout.addWidget(self.time_label, alignment=Qt.AlignmentFlag.AlignCenter)

    def create_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer_stopped = False

    def timer_ready(self):
        self.painted = False
        self.timer_stopped = False
        self.scramble_label.hide()
        self.time_label.setStyleSheet("font-size: 300px; color: green")
        self.time_label.setText("0.0s")
        self.update()

    def reset(self):
        self.painted = True
        self.timer_stopped = True
        self.scramble = scramble_3x3()
        self.scramble_label.setText(self.scramble)
        self.scramble_label.show()
        self.time_label.setStyleSheet("font-size: 200px")
        self.update()

    def paintEvent(self, event):
        if not self.painted:
            return
        
        painter = QPainter(self)
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(3)
        pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(pen)

        scrambled_cube = ScrambleVisual().apply_scramble(self.scramble.split())

        for i in range(3):
            for j in range(3):
                painter.setBrush(ScrambleVisual.COLORS[scrambled_cube[0][j, i]])
                painter.drawRect(800 + i*60, 120 + j*60, 60, 60)
        
        for i in range(4):
            for j in range(3):
                for k in range(3):
                    painter.setBrush(ScrambleVisual.COLORS[scrambled_cube[i + 1][k, j]])
                    painter.drawRect(620 + i*180 + j*60, 300 + k*60, 60, 60)
        
        for i in range(3):
            for j in range(3):
                painter.setBrush(ScrambleVisual.COLORS[scrambled_cube[5][j, i]])
                painter.drawRect(800 + i*60, 480 + j*60, 60, 60)             


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimerWindow()
    window.show()
    sys.exit(app.exec())
