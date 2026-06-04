from PySide6.QtWidgets import QWidget

class CourseMeta:
    """
    This is a abstract class where every course has.
    """

    def get_course_title() -> str:
        raise NotImplemented()
    
    def get_course_description() -> str:
        raise NotImplemented()
    
    def get_course_widget() -> QWidget:
        raise NotImplemented()
