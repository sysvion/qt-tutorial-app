# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'course.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 147)
        Form.setStyleSheet(u"#course_layout{\n"
"background: #aaa;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")

        self.verticalLayout_2.addWidget(self.title)

        self.body = QLabel(Form)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"background:#eee;\n"
"")

        self.verticalLayout_2.addWidget(self.body)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"title", None))
        self.body.setText(QCoreApplication.translate("Form", u"body", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"open", None))
    # retranslateUi

