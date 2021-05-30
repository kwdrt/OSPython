
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
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(260, 400)


class RaportWindow(QtWidgets.QMainWindow, Ui_RaportWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(RaportWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.prepare(ps, rs)


class SectionWindow(QtWidgets.QMainWindow, Ui_SectionWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(SectionWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.prepare(ps, rs)


class RaportEditWindow(QtWidgets.QMainWindow, Ui_RaportEditWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(RaportEditWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.prepare(ps, rs)


def switch_window(currentWindow, newWindow):
    newWindow.getValue(currentWindow.giveValue())
    currentWindow.close()
    newWindow.refresh()
    newWindow.show()

def shutdown(app):
    app.closeAllWindows()

app = QtWidgets.QApplication(sys.argv)

# starting windows
start_window = MainWindow()
raport_window = RaportWindow()
section_window = SectionWindow()
raport_edit_window = RaportEditWindow()

# code responsible for switching windows (linking to buttons)
start_window.pushButton.clicked.connect(lambda: switch_window(start_window, raport_window))
start_window.pushButton_2.clicked.connect(lambda: switch_window(start_window, section_window))
start_window.pushButton_3.clicked.connect(lambda: shutdown(app))

raport_window.pushButton_2.clicked.connect(lambda: switch_window(raport_window, start_window))
raport_window.edit_report_button.clicked.connect(lambda: switch_window(raport_window, raport_edit_window))

raport_edit_window.pushButton_2.clicked.connect(lambda: switch_window(raport_edit_window, raport_window))

section_window.pushButton_2.clicked.connect(lambda: switch_window(section_window, start_window))

# show the startup window
start_window.show()
app.exec()
