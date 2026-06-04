from PySide6.QtWidgets import QMainWindow, QWidget
from .ui_mainWindow import Ui_MainWindow
from .courseSelectorModel import CourseSelectorModel
#import rclpy
from rclpy.node import Node

class MainWindow(Node, QMainWindow):
    def __init__(self):
        Node.__init__(self, node_name='gui')
        QMainWindow.__init__(self)
        print("MainWindow object instantiated")
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._currentWidget = CourseSelectorModel(interface=self)
        self.ui.main_layout.addWidget(self._currentWidget)

    def set_content(self, widget: QWidget):
        self.ui.main_layout.replaceWidget(self._currentWidget, widget)
        self._currentWidget.setParent(None)
        self._currentWidget = widget


