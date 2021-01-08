# -*- coding: UTF-8 -*-

import sys

from PySide2 import QtWidgets, QtGui
from interface import Ui_TestTaskWindow

from modules.parser import Parser


class MainWindow(QtWidgets.QMainWindow):
    parser = Parser()
    current_exam = None
    current_direction = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_TestTaskWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(' ')
        self.setWindowIcon(QtGui.QIcon('img/icon.ico'))

        self.ui.exam_combo_box.activated[str].connect(self.exam_cb_changed)
        self.ui.direction_combo_box.activated[str].connect(self.direction_cb_changed)
        self.ui.load_btn.clicked.connect(self.load_data)

    def load_data(self):
        self.ui.exam_combo_box.clear()
        self.ui.direction_combo_box.clear()
        self.ui.text_box.clear()

        self.parser.load()

        self.current_exam = self.parser.get_exams()[0]
        self.current_direction = self.parser.get_directions()[0]
        self.ui.text_box.setText(self.parser.get_info())

        for exam in self.parser.get_exams():
            self.ui.exam_combo_box.addItem(exam)

        for direction in self.parser.get_directions():
            self.ui.direction_combo_box.addItem(direction[1])

    def update_cb(self):
        self.ui.direction_combo_box.clear()
        self.ui.text_box.clear()

        for direction in self.parser.get_directions(self.current_exam):
            self.ui.direction_combo_box.addItem(direction[1])

    def exam_cb_changed(self):
        self.current_exam = self.ui.exam_combo_box.currentText()
        self.update_cb()

    def direction_cb_changed(self):
        self.current_direction = self.ui.direction_combo_box.currentText()

        for direction in self.parser.get_directions():
            if direction[1] == self.current_direction:
                self.current_direction = direction

        info = self.parser.get_info(self.current_direction)
        self.ui.text_box.setText(info)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
