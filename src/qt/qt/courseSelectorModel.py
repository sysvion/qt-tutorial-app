from .ui_course_card import Ui_Form as Ui_Course_Card_Form

from PySide6.QtWidgets import QWidget, QHBoxLayout, QTextBrowser, QPushButton

from .followCamCourse import FolowHandMeta


courses = [
    FolowHandMeta()    
]

class CourseSelectorModel(QWidget):
    cards = []
    def __init__(self, interface):
        super().__init__()
        self.layout = QHBoxLayout(self)

        for course in courses:
            card = course_card(
                course.get_course_title(),
                course.get_course_description(),
                lambda _ : interface.set_content(course.get_course_widget())
            )
            self.layout.addWidget(card)



class course_card(QWidget):
    
    def __init__(self, title:str, body:str, on_click, parent=None):
        super(course_card, self).__init__(parent)

        self.m_ui = Ui_Course_Card_Form()
        self.m_ui.setupUi(self)
        self.m_ui.title.setText(title)
        self.m_ui.body.setText(body)
        self.m_ui.pushButton.clicked.connect(on_click)
