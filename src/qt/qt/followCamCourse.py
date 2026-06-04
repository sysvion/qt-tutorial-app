from .courseMeta import CourseMeta
from PySide6.QtWidgets import QTextBrowser, QVBoxLayout
from .dialog import Dialog

class FolowHandMeta(CourseMeta):

    def get_course_title(self):
        return "Basics of ros"

    def get_course_description(self):
        return "Learn the basics of ros2 by following a hand"
    
    def get_course_widget(self):
        return course()
    

class course(Dialog):




    def __init__(self, parent=None):

        # main
        welcome = QVBoxLayout()

        browser = QTextBrowser()

        browser.setHtml("""
hello
                        """)
    
        welcome.addWidget(browser)

        browser2 = QTextBrowser()

        wow = QVBoxLayout()

        browser2.setHtml("""
domo
                        """)
    
        wow.addWidget(browser2)
        
        slides = [
            welcome,
            wow
        ]
        super().__init__(slides,parent=parent)


