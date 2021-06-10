
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import firebaseUtils as fU
from PyQt5 import QtWidgets
from start import Ui_MainWindow
from raport import Ui_RaportWindow
from section import Ui_SectionWindow
from raport_edit import Ui_RaportEditWindow

# utils shared by every window
ps = fU.PersonService()
rs = fU.ReportService()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(260, 400)


class ReportWindow(QtWidgets.QMainWindow, Ui_RaportWindow):
    def __init__(self, *args, **kwargs):
        super(ReportWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.prepare(ps, rs)


class SectionWindow(QtWidgets.QMainWindow, Ui_SectionWindow):
    def __init__(self, *args, **kwargs):
        super(SectionWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.prepare(ps, rs)


class ReportEditWindow(QtWidgets.QMainWindow, Ui_RaportEditWindow):
    def __init__(self, *args, **kwargs):
        super(ReportEditWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.prepare(ps, rs)


def switch_window(current_window, new_window):
    new_window.get_value(current_window.give_value())
    current_window.close()
    new_window.refresh()
    new_window.show()


def shutdown(application):
    application.closeAllWindows()


app = QtWidgets.QApplication(sys.argv)

# starting windows
start_window = MainWindow()
report_window = ReportWindow()
section_window = SectionWindow()
report_edit_window = ReportEditWindow()

# code responsible for switching windows (linking to buttons)
start_window.pushButton.clicked.connect(lambda: switch_window(start_window, report_window))
start_window.pushButton_2.clicked.connect(lambda: switch_window(start_window, section_window))
start_window.pushButton_3.clicked.connect(lambda: shutdown(app))

report_window.pushButton_2.clicked.connect(lambda: switch_window(report_window, start_window))
report_window.edit_report_button.clicked.connect(lambda: switch_window(report_window, report_edit_window))

report_edit_window.pushButton_2.clicked.connect(lambda: switch_window(report_edit_window, report_window))

section_window.pushButton_2.clicked.connect(lambda: switch_window(section_window, start_window))

# show the startup window
start_window.show()
app.exec()
