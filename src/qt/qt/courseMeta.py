from PySide6.QtWidgets import QWidget

class CourseMeta:
    """
    This is a abstract class where every course has.
    """

    def __init__(self, course_title):
        self.course_title = course_title

    def get_course_widget() -> QWidget:
        pass
