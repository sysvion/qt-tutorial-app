from .application import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

import sys
import rclpy

def main():
    print("Starting app")

    rclpy.init()
    
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    timer = QTimer()
    timer.timeout.connect(lambda: rclpy.spin_once(window, timeout_sec=0.01))
    timer.start(10)

    returncode = app.exec()

    timer.stop()
    rclpy.shutdown()

    sys.exit(returncode)

if __name__ == '__main__':

    main()
