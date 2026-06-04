from PySide6.QtWidgets import QWidget, QHBoxLayout, QTextBrowser, QPushButton
#from .application import MainWindow
courses = [
    
]

class CourseSelectorModel(QWidget):
    def __init__(self, interface):
        super().__init__()
        self.layout = QHBoxLayout(self)

        selectable_text = QTextBrowser()
        selectable_text.setHtml("""
<h1>Hello World!</h1>
""")
        
        button = QPushButton()
        button.setText("Open")
        button.clicked.connect(lambda: interface.set_content(QPushButton()))

        self.layout.addWidget(selectable_text)
        self.layout.addWidget(button)