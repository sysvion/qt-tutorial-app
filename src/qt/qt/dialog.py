from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLayout, QStackedWidget

class Dialog(QWidget):

    def __init__(self, slides: list[QLayout], parent=None):
        super().__init__(parent)

        if len(slides) == 0:
            raise ValueError("There needs to be at least one slide")

        self.slides = slides

        buttonsLayout = QHBoxLayout()

        self.prevBtn = QPushButton("Previous")
        self.prevBtn.clicked.connect(self.previousSlide)
        buttonsLayout.addWidget(self.prevBtn)

        self.nextBtn = QPushButton("Next")
        self.nextBtn.clicked.connect(self.nextSlide)
        buttonsLayout.addWidget(self.nextBtn)

        mainLayout = QVBoxLayout()
        self.slideWidgets = QStackedWidget()
        for slide in slides:
            slide_widget = QWidget()
            slide_widget.setLayout(slide)
            self.slideWidgets.addWidget(slide_widget)
        

        mainLayout.addWidget(self.slideWidgets)
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)



    def nextSlide(self):
        if (self.slideWidgets.currentIndex() >= self.slideWidgets.count() - 1):
            return
        
        self.slideWidgets.setCurrentIndex(self.slideWidgets.currentIndex()+1)
        
 

    def previousSlide(self):
        if self.slideWidgets.currentIndex() == 0 :
            return
        
        self.slideWidgets.setCurrentIndex(self.slideWidgets.currentIndex()-1)

