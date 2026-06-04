from .application import MainWindow
from PySide6.QtWidgets import QApplication

import sys
import rclpy

def main():
    print("Starting app")

    rclpy.init()
    
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    returncode = app.exec()

    rclpy.shutdown()

    sys.exit(returncode)

if __name__ == '__main__':

    main()
