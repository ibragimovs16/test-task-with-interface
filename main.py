# -*- coding: UTF-8 -*-

import sys
from os import remove

from PySide2 import QtWidgets, QtGui
from interface import Ui_TestTaskWindow

from modules.dbHandler import DataBaseHandler


class MainWindow(QtWidgets.QMainWindow):
    current_exam = None
    current_direction = None
    db = DataBaseHandler()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_TestTaskWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(' ')
        self.setWindowIcon(QtGui.QIcon('img/icon.ico'))

        self.ui.exam_combo_box.activated[str].connect(self.exam_cb_changed)
        self.ui.direction_combo_box.activated[str].connect(self.direction_cb_changed)
        self.ui.load_btn.clicked.connect(self.load_data)

    def __error(self):
        QtWidgets.QMessageBox.critical(self, 'Ошибка',
                                       'Произошла ошибка, подождите немного...',
                                       QtWidgets.QMessageBox.Ok)
        self.db.repair()

    def load_data(self):
        self.ui.exam_combo_box.clear()
        self.ui.direction_combo_box.clear()
        self.ui.text_box.clear()

        try:
            self.current_exam = self.db.get_exams()[0]
            self.current_direction = self.db.get_directions(self.current_exam)[0]
            self.ui.text_box.setText(self.db.get_info(self.current_direction)[0])
        except Exception:
            self.__error()

        for exam in self.db.get_exams():
            self.ui.exam_combo_box.addItem(exam)

        for direction in self.db.get_directions(self.current_exam):
            self.ui.direction_combo_box.addItem(direction)

    def update_cb(self):
        self.ui.direction_combo_box.clear()
        self.ui.text_box.clear()

        for direction in self.db.get_directions(self.current_exam):
            self.ui.direction_combo_box.addItem(direction)

    def exam_cb_changed(self):
        self.current_exam = self.ui.exam_combo_box.currentText()
        self.update_cb()

    def direction_cb_changed(self):
        self.current_direction = self.ui.direction_combo_box.currentText()

        for direction in self.db.get_directions(self.current_exam):
            if direction[1] == self.current_direction:
                self.current_direction = direction

        info = self.db.get_info(self.current_direction)
        self.ui.text_box.setText(info[0])


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
