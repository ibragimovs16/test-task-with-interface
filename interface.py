# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TestTaskWindow(object):
    def setupUi(self, TestTaskWindow):
        if not TestTaskWindow.objectName():
            TestTaskWindow.setObjectName(u"TestTaskWindow")
        TestTaskWindow.resize(800, 600)
        TestTaskWindow.setMinimumSize(QSize(800, 600))
        TestTaskWindow.setMaximumSize(QSize(800, 600))
        self.mainWidget = QWidget(TestTaskWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setStyleSheet(u"background-color: #121212;")
        self.label = QLabel(self.mainWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 171, 16))
        self.label.setStyleSheet(u"QLabel {\n"
"	color: #fff;\n"
"}")
        self.exam_combo_box = QComboBox(self.mainWidget)
        self.exam_combo_box.setObjectName(u"exam_combo_box")
        self.exam_combo_box.setGeometry(QRect(190, 20, 521, 22))
        self.exam_combo_box.setStyleSheet(u"QComboBox {\n"
"	background-color: #1E1E1E;\n"
"	selection-background-color: #1E1E1E;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: #2E2E2E;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QListView {\n"
"	color: #fff;\n"
"	background-color: #1E1E1E;\n"
"	selection-background-color: #2E2E2E;\n"
"}")
        self.exam_combo_box.setInsertPolicy(QComboBox.InsertAfterCurrent)
        self.label_2 = QLabel(self.mainWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 141, 16))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: #fff;\n"
"}")
        self.direction_combo_box = QComboBox(self.mainWidget)
        self.direction_combo_box.setObjectName(u"direction_combo_box")
        self.direction_combo_box.setGeometry(QRect(160, 70, 551, 22))
        self.direction_combo_box.setStyleSheet(u"QComboBox {\n"
"	background-color: #1E1E1E;\n"
"	selection-background-color: #1E1E1E;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: #2E2E2E;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QListView {\n"
"	color: #fff;\n"
"	background-color: #1E1E1E;\n"
"	selection-background-color: #2E2E2E;\n"
"}")
        self.scrollArea = QScrollArea(self.mainWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 100, 781, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 779, 489))
        self.text_box = QTextBrowser(self.scrollAreaWidgetContents)
        self.text_box.setObjectName(u"text_box")
        self.text_box.setGeometry(QRect(0, 0, 781, 491))
        self.text_box.setStyleSheet(u"background-color: #1E1E1E;\n"
"color: #fff;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.load_btn = QPushButton(self.mainWidget)
        self.load_btn.setObjectName(u"load_btn")
        self.load_btn.setGeometry(QRect(720, 10, 71, 81))
        self.load_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #1E1E1E;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2E2E2E;\n"
"}")
        TestTaskWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(TestTaskWindow)

        QMetaObject.connectSlotsByName(TestTaskWindow)
    # setupUi

    def retranslateUi(self, TestTaskWindow):
        TestTaskWindow.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("TestTaskWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u044d\u043a\u0437\u0430\u043c\u0435\u043d:", None))
        self.label_2.setText(QCoreApplication.translate("TestTaskWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435:", None))
        self.load_btn.setText(QCoreApplication.translate("TestTaskWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c\n"
" \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

