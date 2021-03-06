from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SectionWindow(object):
    def __init__(self):
        self.rs = None
        self.ps = None
        self.all_members = None

    def setupUi(self, SectionWindow):
        SectionWindow.setObjectName("SectionWindow")
        SectionWindow.resize(800, 600)
        SectionWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SectionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(390, 10, 16, 551))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 30, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 131, 16))
        self.label_3.setObjectName("label_3")
        self.new_member_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.new_member_name.setGeometry(QtCore.QRect(10, 170, 381, 21))
        self.new_member_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.new_member_name.setObjectName("new_member_name")
        self.new_member_lastname = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.new_member_lastname.setGeometry(QtCore.QRect(10, 230, 381, 21))
        self.new_member_lastname.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.new_member_lastname.setObjectName("new_member_lastname")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 131, 16))
        self.label_4.setObjectName("label_4")
        self.new_section_leader = QtWidgets.QCheckBox(self.centralwidget)
        self.new_section_leader.setGeometry(QtCore.QRect(30, 320, 121, 17))
        self.new_section_leader.setObjectName("new_section_leader")
        self.new_action_leader = QtWidgets.QCheckBox(self.centralwidget)
        self.new_action_leader.setGeometry(QtCore.QRect(30, 350, 151, 17))
        self.new_action_leader.setObjectName("new_action_leader")
        self.new_driver = QtWidgets.QCheckBox(self.centralwidget)
        self.new_driver.setGeometry(QtCore.QRect(30, 380, 141, 17))
        self.new_driver.setObjectName("new_driver")
        self.member_lastname = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.member_lastname.setGeometry(QtCore.QRect(410, 230, 381, 21))
        self.member_lastname.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.member_lastname.setObjectName("member_lastname")
        self.member_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.member_name.setGeometry(QtCore.QRect(410, 170, 381, 21))
        self.member_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.member_name.setObjectName("member_name")
        self.driver = QtWidgets.QCheckBox(self.centralwidget)
        self.driver.setGeometry(QtCore.QRect(420, 380, 141, 17))
        self.driver.setObjectName("driver")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 210, 131, 16))
        self.label_5.setObjectName("label_5")
        self.section_leader = QtWidgets.QCheckBox(self.centralwidget)
        self.section_leader.setGeometry(QtCore.QRect(420, 320, 121, 17))
        self.section_leader.setObjectName("section_leader")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 150, 131, 16))
        self.label_6.setObjectName("label_6")
        self.action_leader = QtWidgets.QCheckBox(self.centralwidget)
        self.action_leader.setGeometry(QtCore.QRect(420, 350, 151, 17))
        self.action_leader.setObjectName("action_leader")
        self.person_to_edit = QtWidgets.QComboBox(self.centralwidget)
        self.person_to_edit.setGeometry(QtCore.QRect(450, 110, 281, 22))
        self.person_to_edit.setObjectName("person_to_edit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 90, 171, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.update_member = QtWidgets.QPushButton(self.centralwidget)
        self.update_member.setGeometry(QtCore.QRect(500, 470, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.update_member.setFont(font)
        self.update_member.setObjectName("update_member")
        self.add_new_member = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_member.setGeometry(QtCore.QRect(80, 470, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_new_member.setFont(font)
        self.add_new_member.setObjectName("add_new_member")
        self.is_active = QtWidgets.QCheckBox(self.centralwidget)
        self.is_active.setGeometry(QtCore.QRect(420, 410, 141, 17))
        self.is_active.setObjectName("is_active")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 260, 131, 16))
        self.label_8.setObjectName("label_8")
        self.new_member_phone = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.new_member_phone.setGeometry(QtCore.QRect(10, 280, 381, 21))
        self.new_member_phone.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.new_member_phone.setObjectName("new_member_phone")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 260, 131, 16))
        self.label_9.setObjectName("label_9")
        self.member_phone = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.member_phone.setGeometry(QtCore.QRect(410, 280, 381, 21))
        self.member_phone.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.member_phone.setObjectName("member_phone")
        SectionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SectionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        SectionWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SectionWindow)
        self.statusbar.setObjectName("statusbar")
        SectionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SectionWindow)
        QtCore.QMetaObject.connectSlotsByName(SectionWindow)

    def retranslateUi(self, SectionWindow):
        _translate = QtCore.QCoreApplication.translate
        SectionWindow.setWindowTitle(_translate("SectionWindow", "Sekcja"))
        self.pushButton_2.setText(_translate("SectionWindow", "Powr??t do menu"))
        self.label.setText(_translate("SectionWindow", "Dodaj cz??onka sekcji"))
        self.label_2.setText(_translate("SectionWindow", "Zmie?? dane cz??onka sekcji"))
        self.label_3.setText(_translate("SectionWindow", "Imi??"))
        self.label_4.setText(_translate("SectionWindow", "Nazwisko"))
        self.new_section_leader.setText(_translate("SectionWindow", "Dow??dca sekcji"))
        self.new_action_leader.setText(_translate("SectionWindow", "Mo??e by?? dow??dc?? akcji"))
        self.new_driver.setText(_translate("SectionWindow", "Mo??e by?? kierowc??"))
        self.driver.setText(_translate("SectionWindow", "Mo??e by?? kierowc??"))
        self.label_5.setText(_translate("SectionWindow", "Nazwisko"))
        self.section_leader.setText(_translate("SectionWindow", "Dow??dca sekcji"))
        self.label_6.setText(_translate("SectionWindow", "Imi??"))
        self.action_leader.setText(_translate("SectionWindow", "Mo??e by?? dow??dc?? akcji"))
        self.label_7.setText(_translate("SectionWindow", "Wybierz cz??onka sekcji do edycji"))
        self.update_member.setText(_translate("SectionWindow", "Zaktualizuj dane"))
        self.add_new_member.setText(_translate("SectionWindow", "Dodaj cz??onka sekcji"))
        self.is_active.setText(_translate("SectionWindow", "Cz??onek aktywny"))
        self.label_8.setText(_translate("SectionWindow", "Numer telefonu"))
        self.label_9.setText(_translate("SectionWindow", "Numer telefonu"))

        self.person_to_edit.currentTextChanged.connect(lambda: self.set_active_info())
        self.update_member.clicked.connect(lambda: self.update_member_data())
        self.add_new_member.clicked.connect(lambda: self.add_member_data())

    def prepare(self, ps, rs):
        self.ps = ps
        self.rs = rs
        self.people_list = ps.get_all_people()
        self.add_all_people()

    def add_all_people(self):
        all_people = self.ps.get_all_people()
        for key, i in all_people.items():
            if i is not None:
                self.person_to_edit.addItem(i.get("FirstName") + "," + i.get("LastName") + "," + str(i.get("PhoneNumber")))

    def set_active_info(self):
        chosen_person = self.person_to_edit.currentText()
        print(chosen_person)
        chosen_person_id = self.ps.translate_to_id(chosen_person)
        chosen_person_data = self.ps.get_person_by_id(chosen_person_id)
        print(chosen_person_data)
        self.member_name.setPlainText(chosen_person_data.get("FirstName"))
        self.member_lastname.setPlainText(chosen_person_data.get("LastName"))
        self.member_phone.setPlainText(str(chosen_person_data.get("PhoneNumber")))
        self.section_leader.setChecked(chosen_person_data.get("IsSectionLeader"))
        self.action_leader.setChecked(chosen_person_data.get("IsActionLeader"))
        self.driver.setChecked(chosen_person_data.get("IsDriver"))
        self.is_active.setChecked(chosen_person_data.get("IsActive"))

    def validate(self, name, lastname, phone):
        if not name or not lastname or not phone:
            return False
        if not phone.isdecimal() or len(phone) != 9:
            return False
        return True

    def update_member_data(self):
        chosen_person = self.person_to_edit.currentText()
        print(chosen_person)
        chosen_person_id = self.ps.translate_to_id(chosen_person)

        if not self.validate(self.member_name.toPlainText(),
                              self.member_lastname.toPlainText(),
                              self.member_phone.toPlainText()):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('B????dne dane cz??onka sekcji! Sprawd?? ponownie imi??, nazwisko i numer telefonu.')
            error_dialog.exec_()
        else:
            self.ps.change_person_data(chosen_person_id,
                                       self.member_name.toPlainText(),
                                       self.member_lastname.toPlainText(),
                                       int(self.member_phone.toPlainText()),
                                       int(self.is_active.isChecked()),
                                       int(self.driver.isChecked()),
                                       int(self.action_leader.isChecked()),
                                       int(self.section_leader.isChecked()))

            new_person_data = self.member_name.toPlainText() + "," + self.member_lastname.toPlainText() + "," + self.member_phone.toPlainText()
            self.person_to_edit.setItemText(self.person_to_edit.currentIndex(), new_person_data)

    def add_member_data(self):
        if not self.validate(self.new_member_name.toPlainText(),
                             self.new_member_lastname.toPlainText(),
                             self.new_member_phone.toPlainText()):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('B????dne dane cz??onka sekcji! Sprawd?? ponownie imi??, nazwisko i numer telefonu.')
            error_dialog.exec_()
        else:
            self.ps.add_person(
                self.new_member_name.toPlainText(),
                self.new_member_lastname.toPlainText(),
                int(self.new_action_leader.isChecked()),
                1,
                int(self.new_driver.isChecked()),
                int(self.new_section_leader.isChecked()),
                int(self.new_member_phone.toPlainText()))

            new_person_data = self.new_member_name.toPlainText() + "," + self.new_member_lastname.toPlainText() + "," + self.new_member_phone.toPlainText()
            self.person_to_edit.addItem(new_person_data)

    def refresh(self):
        pass

    def give_value(self):
        pass

    def get_value(self, report_id):
        pass
