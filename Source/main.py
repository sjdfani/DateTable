from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dateTable import Ui_MainWindow
from AddEvent import Ui_AddWin
from EditEvent import Ui_EditWindow
from setting import Ui_SettingWindow
import backend
from datetime import datetime, date
import time
import _thread
from notifypy import Notify


class settingEvent(QMainWindow):
    handle_info = "close"
    handle_help = "close"
    handle_theme = "close"

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SettingWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(r"photo\logo.png"))
        self.setWindowTitle("Setting Tab")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.theme_frame.hide()
        self.ui.info_frame.hide()
        self.ui.help_frame.hide()
        self.ui.info_btn.clicked.connect(self.info_func)
        self.ui.help_btn.clicked.connect(self.help_func)
        self.ui.theme_btn.clicked.connect(self.theme_func)

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def Anim_frame(self, frame, x, y, width, height, typeFrame, openState):
        if typeFrame == "settingLabel":
            frame = self.ui.label
        if openState:
            self.anim = QPropertyAnimation(frame, b"geometry")
            self.anim.setDuration(500)
            if typeFrame == "theme":
                self.anim.setStartValue(QRect(x, y, width, 0))
                self.anim.setEndValue(QRect(x, y, width, height))
            elif typeFrame == "settingLabel":
                self.anim.setStartValue(QRect(x, y, 0, height))
                self.anim.setEndValue(QRect(x, y, width, height))
            else:
                self.anim.setStartValue(QRect(x, y, 0, height))
                self.anim.setEndValue(QRect(x, y, width, height))
            self.anim.start()
        else:
            self.anim = QPropertyAnimation(frame, b"geometry")
            self.anim.setDuration(500)
            if typeFrame == "theme":
                self.anim.setStartValue(QRect(x, y, width, height))
                self.anim.setEndValue(QRect(x, y, width, 0))
            else:
                self.anim.setStartValue(QRect(x, y, width, height))
                self.anim.setEndValue(QRect(x, y, 0, height))
            self.anim.start()

    def info_func(self):
        if self.handle_info == "close":
            self.ui.info_frame.show()
            self.Anim_frame(self.ui.info_frame, 20, 90, 341, 161, "info", True)
            self.handle_info = "open"
        elif self.handle_info == "open":
            self.Anim_frame(self.ui.info_frame, 20, 90, 341, 161, "info", False)
            self.handle_info = "close"

    def help_func(self):
        if self.handle_help == "close":
            self.ui.help_frame.show()
            self.Anim_frame(self.ui.help_frame, 20, 260, 341, 231, "help", True)
            self.handle_help = "open"
        elif self.handle_help == "open":
            self.Anim_frame(self.ui.help_frame, 20, 260, 341, 231, "help", False)
            self.handle_help = "close"

    def theme_func(self):
        if self.handle_theme == "close":
            self.ui.theme_frame.show()
            self.Anim_frame(self.ui.theme_frame, 376, 290, 111, 201, "theme", True)
            self.handle_theme = "open"
        elif self.handle_theme == "open":
            self.Anim_frame(self.ui.theme_frame, 376, 290, 111, 201, "theme", False)
            self.handle_theme = "close"
        # self.ui.theme_1.clicked.connect(self.theme_1_func)
        # self.ui.theme_2.clicked.connect(self.theme_2_func)
        # self.ui.theme_3.clicked.connect(self.theme_3_func)
        # self.ui.theme_4.clicked.connect(self.theme_4_func)
        # self.ui.theme_5.clicked.connect(self.theme_5_func)

    def theme_1_func(self):
        self.ui.centralwidget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #304352, stop:1 #d7d2cc);\n"
            "border-radius:5px;\n"
            "")

    def theme_2_func(self):
        self.ui.centralwidget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #aa4b6b, stop:0.5 #6b6b83, stop:1 #3b8d99);\n"
            "border-radius:5px;\n"
            "")

    def theme_3_func(self):
        self.ui.centralwidget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #654ea3, stop:1 #eaafc8); \n"
            "border-radius:5px;\n"
            "")

    def theme_4_func(self):
        self.ui.centralwidget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #8A2387, stop:0.5 #E94057, stop:1 #F27121); \n"
            "border-radius:5px;\n"
            "")

    def theme_5_func(self):
        self.ui.centralwidget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #636363,stop:1 #a2ab58); \n"
            "border-radius:5px;\n"
            "")


class editEvent(QMainWindow):
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
    day_28 = 2
    inputFrame = ""

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_EditWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(r"photo\logo.png"))
        self.setWindowTitle("Edit Tab")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.state_lineEdit.setReadOnly(True)
        self.ui.update_btn.clicked.connect(self.update_func)

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def Anim_frame(self, x, y, width, height, openState):
        if openState:
            self.anim = QPropertyAnimation(self.ui.label, b"geometry")
            self.anim.setDuration(700)
            self.anim.setStartValue(QRect(x, y, 0, height))
            self.anim.setEndValue(QRect(x, y, width, height))
            self.anim.start()

    def update_func(self):
        frame = self.inputFrame
        self.ui.title_lineEdit.setText(self.ui.title_lineEdit.text().strip())
        self.ui.des_lineEdit.setText(self.ui.des_lineEdit.text().strip())
        self.ui.day_lineEdit.setText(self.ui.day_lineEdit.text().strip())
        self.ui.month_lineEdit.setText(self.ui.month_lineEdit.text().strip())
        self.ui.year_lineEdit.setText(self.ui.year_lineEdit.text().strip())
        self.ui.sec_lineEdit.setText(self.ui.sec_lineEdit.text().strip())
        self.ui.min_lineEdit.setText(self.ui.min_lineEdit.text().strip())
        self.ui.hour_lineEdit.setText(self.ui.hour_lineEdit.text().strip())
        date_year_now = int(datetime.now().strftime("%Y"))
        date_year_after50 = int(datetime.now().strftime("%Y")) + 50
        date_month_now = int(datetime.now().strftime("%m"))
        date_day_now = int(datetime.now().strftime("%d"))
        if len(self.ui.title_lineEdit.text()) != 0:
            if len(self.ui.hour_lineEdit.text()) != 0:
                if self.ui.hour_lineEdit.text().isnumeric():
                    if 0 <= int(self.ui.hour_lineEdit.text()) <= 23:
                        if len(self.ui.min_lineEdit.text()) != 0:
                            if self.ui.min_lineEdit.text().isnumeric():
                                if 0 <= int(self.ui.min_lineEdit.text()) <= 59:
                                    if len(self.ui.sec_lineEdit.text()) != 0:
                                        if self.ui.sec_lineEdit.text().isnumeric():
                                            if 0 <= int(self.ui.sec_lineEdit.text()) <= 59:
                                                if len(self.ui.year_lineEdit.text()) != 0:
                                                    if self.ui.year_lineEdit.text().isnumeric():
                                                        if date_year_now <= int(
                                                                self.ui.year_lineEdit.text()) <= date_year_after50:
                                                            if len(self.ui.month_lineEdit.text()) != 0:
                                                                if self.ui.month_lineEdit.text().isnumeric():
                                                                    if date_month_now <= int(
                                                                            self.ui.month_lineEdit.text()) <= 12:
                                                                        if len(self.ui.day_lineEdit.text()) != 0:
                                                                            if self.ui.day_lineEdit.text().isnumeric():
                                                                                if int(self.ui.month_lineEdit.text()) in self.day_31:
                                                                                    if date_day_now <= int(
                                                                                            self.ui.day_lineEdit.text()) <= 31:
                                                                                        self.update_event(frame)
                                                                                    else:
                                                                                        self.showError("Day",
                                                                                                       f"Day should be between {date_day_now}-31.")
                                                                                elif int(
                                                                                        self.ui.month_lineEdit.text()) in self.day_30:
                                                                                    if date_day_now <= int(
                                                                                            self.ui.day_lineEdit.text()) <= 30:
                                                                                        self.update_event(frame)
                                                                                    else:
                                                                                        self.showError("Day",
                                                                                                       f"Day should be between {date_day_now}-30.")
                                                                                elif int(
                                                                                        self.ui.month_lineEdit.text()) == self.day_28:
                                                                                    if date_day_now <= int(
                                                                                            self.ui.day_lineEdit.text()) <= 28:
                                                                                        self.update_event(frame)
                                                                                    else:
                                                                                        self.showError("Day",
                                                                                                       f"Day should be between {date_day_now}-28.")
                                                                            else:
                                                                                self.showError("Day type",
                                                                                               "Day should be number.")
                                                                        else:
                                                                            self.showError("Day",
                                                                                           "You should fill day.")
                                                                    else:
                                                                        self.showError("Month",
                                                                                       f"Month should be between {date_month_now}-12.")
                                                                else:
                                                                    self.showError("Month type",
                                                                                   "Month should be number.")
                                                            else:
                                                                self.showError("Month", "You should fill month.")
                                                        else:
                                                            self.showError("Year",
                                                                           f"Year should be between {date_year_now}-{date_year_after50}.")
                                                    else:
                                                        self.showError("Year type", "Year should be number.")
                                                else:
                                                    self.showError("Year", "You should fill year.")
                                            else:
                                                self.showError("Second", "Second should be between 00-59.")
                                        else:
                                            self.showError("Second type", "Second should be number.")
                                    else:
                                        self.showError("Second", "You should fill second.")
                                else:
                                    self.showError("Minute", "Minute should be between 00-59.")
                            else:
                                self.showError("Minute type", "Minute should be number.")
                        else:
                            self.showError("Minute", "You should fill minute.")
                    else:
                        self.showError("Hour", "Hour should be between 00-23.")
                else:
                    self.showError("Hour type", "Hour should be number.")
            else:
                self.showError("Hour", "You should fill hour.")
        else:
            self.showError("Title", "You should fill title.")

    def update_event(self, frame):
        if self.ui.sec_lineEdit.text() == "0":
            self.ui.sec_lineEdit.setText("00")
        elif self.ui.sec_lineEdit.text() == "1":
            self.ui.sec_lineEdit.setText("01")
        elif self.ui.sec_lineEdit.text() == "2":
            self.ui.sec_lineEdit.setText("02")
        elif self.ui.sec_lineEdit.text() == "3":
            self.ui.sec_lineEdit.setText("03")
        elif self.ui.sec_lineEdit.text() == "4":
            self.ui.sec_lineEdit.setText("04")
        elif self.ui.sec_lineEdit.text() == "5":
            self.ui.sec_lineEdit.setText("05")
        elif self.ui.sec_lineEdit.text() == "6":
            self.ui.sec_lineEdit.setText("06")
        elif self.ui.sec_lineEdit.text() == "7":
            self.ui.sec_lineEdit.setText("07")
        elif self.ui.sec_lineEdit.text() == "8":
            self.ui.sec_lineEdit.setText("08")
        elif self.ui.sec_lineEdit.text() == "9":
            self.ui.sec_lineEdit.setText("09")
        if self.ui.min_lineEdit.text() == "0":
            self.ui.min_lineEdit.setText("00")
        elif self.ui.min_lineEdit.text() == "1":
            self.ui.min_lineEdit.setText("01")
        elif self.ui.min_lineEdit.text() == "2":
            self.ui.min_lineEdit.setText("02")
        elif self.ui.min_lineEdit.text() == "3":
            self.ui.min_lineEdit.setText("03")
        elif self.ui.min_lineEdit.text() == "4":
            self.ui.min_lineEdit.setText("04")
        elif self.ui.min_lineEdit.text() == "5":
            self.ui.min_lineEdit.setText("05")
        elif self.ui.min_lineEdit.text() == "6":
            self.ui.min_lineEdit.setText("06")
        elif self.ui.min_lineEdit.text() == "7":
            self.ui.min_lineEdit.setText("07")
        elif self.ui.min_lineEdit.text() == "8":
            self.ui.min_lineEdit.setText("08")
        elif self.ui.min_lineEdit.text() == "9":
            self.ui.min_lineEdit.setText("09")
        if self.ui.hour_lineEdit.text() == "0":
            self.ui.hour_lineEdit.setText("00")
        elif self.ui.hour_lineEdit.text() == "1":
            self.ui.hour_lineEdit.setText("01")
        elif self.ui.hour_lineEdit.text() == "2":
            self.ui.hour_lineEdit.setText("02")
        elif self.ui.hour_lineEdit.text() == "3":
            self.ui.hour_lineEdit.setText("03")
        elif self.ui.hour_lineEdit.text() == "4":
            self.ui.hour_lineEdit.setText("04")
        elif self.ui.hour_lineEdit.text() == "5":
            self.ui.hour_lineEdit.setText("05")
        elif self.ui.hour_lineEdit.text() == "6":
            self.ui.hour_lineEdit.setText("06")
        elif self.ui.hour_lineEdit.text() == "7":
            self.ui.hour_lineEdit.setText("07")
        elif self.ui.hour_lineEdit.text() == "8":
            self.ui.hour_lineEdit.setText("08")
        elif self.ui.hour_lineEdit.text() == "9":
            self.ui.hour_lineEdit.setText("09")
        if self.ui.month_lineEdit.text() == "0":
            self.ui.month_lineEdit.setText("00")
        elif self.ui.month_lineEdit.text() == "1":
            self.ui.month_lineEdit.setText("01")
        elif self.ui.month_lineEdit.text() == "2":
            self.ui.month_lineEdit.setText("02")
        elif self.ui.month_lineEdit.text() == "3":
            self.ui.month_lineEdit.setText("03")
        elif self.ui.month_lineEdit.text() == "4":
            self.ui.month_lineEdit.setText("04")
        elif self.ui.month_lineEdit.text() == "5":
            self.ui.month_lineEdit.setText("05")
        elif self.ui.month_lineEdit.text() == "6":
            self.ui.month_lineEdit.setText("06")
        elif self.ui.month_lineEdit.text() == "7":
            self.ui.month_lineEdit.setText("07")
        elif self.ui.month_lineEdit.text() == "8":
            self.ui.month_lineEdit.setText("08")
        elif self.ui.month_lineEdit.text() == "9":
            self.ui.month_lineEdit.setText("09")
        if self.ui.day_lineEdit.text() == "0":
            self.ui.day_lineEdit.setText("00")
        elif self.ui.day_lineEdit.text() == "1":
            self.ui.day_lineEdit.setText("01")
        elif self.ui.day_lineEdit.text() == "2":
            self.ui.day_lineEdit.setText("02")
        elif self.ui.day_lineEdit.text() == "3":
            self.ui.day_lineEdit.setText("03")
        elif self.ui.day_lineEdit.text() == "4":
            self.ui.day_lineEdit.setText("04")
        elif self.ui.day_lineEdit.text() == "5":
            self.ui.day_lineEdit.setText("05")
        elif self.ui.day_lineEdit.text() == "6":
            self.ui.day_lineEdit.setText("06")
        elif self.ui.day_lineEdit.text() == "7":
            self.ui.day_lineEdit.setText("07")
        elif self.ui.day_lineEdit.text() == "8":
            self.ui.day_lineEdit.setText("08")
        elif self.ui.day_lineEdit.text() == "9":
            self.ui.day_lineEdit.setText("09")
        backend.update(frame, self.ui.title_lineEdit.text(), self.ui.des_lineEdit.text(),
                       self.ui.hour_lineEdit.text(),
                       self.ui.min_lineEdit.text(), self.ui.sec_lineEdit.text(), self.ui.year_lineEdit.text(),
                       self.ui.month_lineEdit.text(), self.ui.day_lineEdit.text(), "active")
        self.showInfo("Update", "Update is successful.")
        self.hide()

    def clear_func(self):
        self.ui.title_lineEdit.setText("")
        self.ui.des_lineEdit.setText("")
        self.ui.hour_lineEdit.setText("")
        self.ui.min_lineEdit.setText("")
        self.ui.sec_lineEdit.setText("")
        self.ui.year_lineEdit.setText("")
        self.ui.month_lineEdit.setText("")
        self.ui.day_lineEdit.setText("")

    def insertInformation(self, frame):
        self.clear_func()
        self.inputFrame = frame
        if self.inputFrame == "1":
            frame_1 = backend.search("1")
            self.ui.event_label.setText("Event 1")
            self.ui.title_lineEdit.setText(frame_1[0][1])
            self.ui.des_lineEdit.setText(frame_1[0][2])
            self.ui.hour_lineEdit.setText(frame_1[0][3])
            self.ui.min_lineEdit.setText(frame_1[0][4])
            self.ui.sec_lineEdit.setText(frame_1[0][5])
            self.ui.year_lineEdit.setText(frame_1[0][6])
            self.ui.month_lineEdit.setText(frame_1[0][7])
            self.ui.day_lineEdit.setText(frame_1[0][8])
            if frame_1[0][9] == "active":
                self.ui.state_lineEdit.setText("Active")
            elif frame_1[0][9] == "deActive":
                self.ui.state_lineEdit.setText("No Active")
        elif self.inputFrame == "2":
            frame_2 = backend.search("2")
            self.ui.event_label.setText("Event 2")
            self.ui.title_lineEdit.setText(frame_2[0][1])
            self.ui.des_lineEdit.setText(frame_2[0][2])
            self.ui.hour_lineEdit.setText(frame_2[0][3])
            self.ui.min_lineEdit.setText(frame_2[0][4])
            self.ui.sec_lineEdit.setText(frame_2[0][5])
            self.ui.year_lineEdit.setText(frame_2[0][6])
            self.ui.month_lineEdit.setText(frame_2[0][7])
            self.ui.day_lineEdit.setText(frame_2[0][8])
            if frame_2[0][9] == "active":
                self.ui.state_lineEdit.setText("Active")
            elif frame_2[0][9] == "deActive":
                self.ui.state_lineEdit.setText("No Active")
        elif self.inputFrame == "3":
            frame_3 = backend.search("3")
            self.ui.event_label.setText("Event 3")
            self.ui.title_lineEdit.setText(frame_3[0][1])
            self.ui.des_lineEdit.setText(frame_3[0][2])
            self.ui.hour_lineEdit.setText(frame_3[0][3])
            self.ui.min_lineEdit.setText(frame_3[0][4])
            self.ui.sec_lineEdit.setText(frame_3[0][5])
            self.ui.year_lineEdit.setText(frame_3[0][6])
            self.ui.month_lineEdit.setText(frame_3[0][7])
            self.ui.day_lineEdit.setText(frame_3[0][8])
            if frame_3[0][9] == "active":
                self.ui.state_lineEdit.setText("Active")
            elif frame_3[0][9] == "deActive":
                self.ui.state_lineEdit.setText("No Active")
        elif self.inputFrame == "4":
            frame_4 = backend.search("4")
            self.ui.event_label.setText("Event 4")
            self.ui.title_lineEdit.setText(frame_4[0][1])
            self.ui.des_lineEdit.setText(frame_4[0][2])
            self.ui.hour_lineEdit.setText(frame_4[0][3])
            self.ui.min_lineEdit.setText(frame_4[0][4])
            self.ui.sec_lineEdit.setText(frame_4[0][5])
            self.ui.year_lineEdit.setText(frame_4[0][6])
            self.ui.month_lineEdit.setText(frame_4[0][7])
            self.ui.day_lineEdit.setText(frame_4[0][8])
            if frame_4[0][9] == "active":
                self.ui.state_lineEdit.setText("Active")
            elif frame_4[0][9] == "deActive":
                self.ui.state_lineEdit.setText("No Active")
        elif self.inputFrame == "5":
            frame_5 = backend.search("5")
            self.ui.event_label.setText("Event 5")
            self.ui.title_lineEdit.setText(frame_5[0][1])
            self.ui.des_lineEdit.setText(frame_5[0][2])
            self.ui.hour_lineEdit.setText(frame_5[0][3])
            self.ui.min_lineEdit.setText(frame_5[0][4])
            self.ui.sec_lineEdit.setText(frame_5[0][5])
            self.ui.year_lineEdit.setText(frame_5[0][6])
            self.ui.month_lineEdit.setText(frame_5[0][7])
            self.ui.day_lineEdit.setText(frame_5[0][8])
            if frame_5[0][9] == "active":
                self.ui.state_lineEdit.setText("Active")
            elif frame_5[0][9] == "deActive":
                self.ui.state_lineEdit.setText("No Active")
        elif self.inputFrame == "6":
            frame_6 = backend.search("6")
            self.ui.event_label.setText("Event 6")
            self.ui.title_lineEdit.setText(frame_6[0][1])
            self.ui.des_lineEdit.setText(frame_6[0][2])
            self.ui.hour_lineEdit.setText(frame_6[0][3])
            self.ui.min_lineEdit.setText(frame_6[0][4])
            self.ui.sec_lineEdit.setText(frame_6[0][5])
            self.ui.year_lineEdit.setText(frame_6[0][6])
            self.ui.month_lineEdit.setText(frame_6[0][7])
            self.ui.day_lineEdit.setText(frame_6[0][8])
            if frame_6[0][9] == "active":
                self.ui.state_lineEdit.setText("Active")
            elif frame_6[0][9] == "deActive":
                self.ui.state_lineEdit.setText("No Active")

    def showInfo(self, title, msg):
        info = QMessageBox(self)
        info.setIcon(QMessageBox.Information)
        info.setText(msg)
        info.setWindowTitle(title)
        info.show()

    def showError(self, title, msg):
        info = QMessageBox(self)
        info.setIcon(QMessageBox.Critical)
        info.setText(msg)
        info.setWindowTitle(title)
        info.show()

    def getCenterWidget(self):
        return self.ui.centralwidget


class addEvent(QMainWindow):
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
    day_28 = 2

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_AddWin()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(r"photo\logo.png"))
        self.setWindowTitle("Add Event")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.clear_btn.clicked.connect(self.clear_func)
        self.ui.submit_btn.clicked.connect(self.submit_func)

    def showInfo(self, title, msg):
        info = QMessageBox(self)
        info.setIcon(QMessageBox.Information)
        info.setText(msg)
        info.setWindowTitle(title)
        info.show()

    def showError(self, title, msg):
        info = QMessageBox(self)
        info.setIcon(QMessageBox.Critical)
        info.setText(msg)
        info.setWindowTitle(title)
        info.show()

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def clear_func(self):
        self.ui.title_lineEdit.setText("")
        self.ui.des_lineEdit.setText("")
        self.ui.hour_lineEdit.setText("")
        self.ui.min_lineEdit.setText("")
        self.ui.sec_lineEdit.setText("")
        self.ui.year_lineEdit.setText("")
        self.ui.month_lineEdit.setText("")
        self.ui.day_lineEdit.setText("")

    @staticmethod
    def check_frame():
        frameState_1 = backend.search("1")
        frameState_2 = backend.search("2")
        frameState_3 = backend.search("3")
        frameState_4 = backend.search("4")
        frameState_5 = backend.search("5")
        frameState_6 = backend.search("6")
        if len(frameState_1) == 0:
            return "1"
        elif len(frameState_2) == 0:
            return "2"
        elif len(frameState_3) == 0:
            return "3"
        elif len(frameState_4) == 0:
            return "4"
        elif len(frameState_5) == 0:
            return "5"
        elif len(frameState_6) == 0:
            return "6"
        else:
            return "None"

    def Add_event(self, frame):
        if frame != "None":
            if self.ui.sec_lineEdit.text() == "0":
                self.ui.sec_lineEdit.setText("00")
            elif self.ui.sec_lineEdit.text() == "1":
                self.ui.sec_lineEdit.setText("01")
            elif self.ui.sec_lineEdit.text() == "2":
                self.ui.sec_lineEdit.setText("02")
            elif self.ui.sec_lineEdit.text() == "3":
                self.ui.sec_lineEdit.setText("03")
            elif self.ui.sec_lineEdit.text() == "4":
                self.ui.sec_lineEdit.setText("04")
            elif self.ui.sec_lineEdit.text() == "5":
                self.ui.sec_lineEdit.setText("05")
            elif self.ui.sec_lineEdit.text() == "6":
                self.ui.sec_lineEdit.setText("06")
            elif self.ui.sec_lineEdit.text() == "7":
                self.ui.sec_lineEdit.setText("07")
            elif self.ui.sec_lineEdit.text() == "8":
                self.ui.sec_lineEdit.setText("08")
            elif self.ui.sec_lineEdit.text() == "9":
                self.ui.sec_lineEdit.setText("09")
            if self.ui.min_lineEdit.text() == "0":
                self.ui.min_lineEdit.setText("00")
            elif self.ui.min_lineEdit.text() == "1":
                self.ui.min_lineEdit.setText("01")
            elif self.ui.min_lineEdit.text() == "2":
                self.ui.min_lineEdit.setText("02")
            elif self.ui.min_lineEdit.text() == "3":
                self.ui.min_lineEdit.setText("03")
            elif self.ui.min_lineEdit.text() == "4":
                self.ui.min_lineEdit.setText("04")
            elif self.ui.min_lineEdit.text() == "5":
                self.ui.min_lineEdit.setText("05")
            elif self.ui.min_lineEdit.text() == "6":
                self.ui.min_lineEdit.setText("06")
            elif self.ui.min_lineEdit.text() == "7":
                self.ui.min_lineEdit.setText("07")
            elif self.ui.min_lineEdit.text() == "8":
                self.ui.min_lineEdit.setText("08")
            elif self.ui.min_lineEdit.text() == "9":
                self.ui.min_lineEdit.setText("09")
            if self.ui.hour_lineEdit.text() == "0":
                self.ui.hour_lineEdit.setText("00")
            elif self.ui.hour_lineEdit.text() == "1":
                self.ui.hour_lineEdit.setText("01")
            elif self.ui.hour_lineEdit.text() == "2":
                self.ui.hour_lineEdit.setText("02")
            elif self.ui.hour_lineEdit.text() == "3":
                self.ui.hour_lineEdit.setText("03")
            elif self.ui.hour_lineEdit.text() == "4":
                self.ui.hour_lineEdit.setText("04")
            elif self.ui.hour_lineEdit.text() == "5":
                self.ui.hour_lineEdit.setText("05")
            elif self.ui.hour_lineEdit.text() == "6":
                self.ui.hour_lineEdit.setText("06")
            elif self.ui.hour_lineEdit.text() == "7":
                self.ui.hour_lineEdit.setText("07")
            elif self.ui.hour_lineEdit.text() == "8":
                self.ui.hour_lineEdit.setText("08")
            elif self.ui.hour_lineEdit.text() == "9":
                self.ui.hour_lineEdit.setText("09")
            if self.ui.month_lineEdit.text() == "0":
                self.ui.month_lineEdit.setText("00")
            elif self.ui.month_lineEdit.text() == "1":
                self.ui.month_lineEdit.setText("01")
            elif self.ui.month_lineEdit.text() == "2":
                self.ui.month_lineEdit.setText("02")
            elif self.ui.month_lineEdit.text() == "3":
                self.ui.month_lineEdit.setText("03")
            elif self.ui.month_lineEdit.text() == "4":
                self.ui.month_lineEdit.setText("04")
            elif self.ui.month_lineEdit.text() == "5":
                self.ui.month_lineEdit.setText("05")
            elif self.ui.month_lineEdit.text() == "6":
                self.ui.month_lineEdit.setText("06")
            elif self.ui.month_lineEdit.text() == "7":
                self.ui.month_lineEdit.setText("07")
            elif self.ui.month_lineEdit.text() == "8":
                self.ui.month_lineEdit.setText("08")
            elif self.ui.month_lineEdit.text() == "9":
                self.ui.month_lineEdit.setText("09")
            if self.ui.day_lineEdit.text() == "0":
                self.ui.day_lineEdit.setText("00")
            elif self.ui.day_lineEdit.text() == "1":
                self.ui.day_lineEdit.setText("01")
            elif self.ui.day_lineEdit.text() == "2":
                self.ui.day_lineEdit.setText("02")
            elif self.ui.day_lineEdit.text() == "3":
                self.ui.day_lineEdit.setText("03")
            elif self.ui.day_lineEdit.text() == "4":
                self.ui.day_lineEdit.setText("04")
            elif self.ui.day_lineEdit.text() == "5":
                self.ui.day_lineEdit.setText("05")
            elif self.ui.day_lineEdit.text() == "6":
                self.ui.day_lineEdit.setText("06")
            elif self.ui.day_lineEdit.text() == "7":
                self.ui.day_lineEdit.setText("07")
            elif self.ui.day_lineEdit.text() == "8":
                self.ui.day_lineEdit.setText("08")
            elif self.ui.day_lineEdit.text() == "9":
                self.ui.day_lineEdit.setText("09")
            backend.insert(frame, self.ui.title_lineEdit.text(), self.ui.des_lineEdit.text(),
                           self.ui.hour_lineEdit.text(),
                           self.ui.min_lineEdit.text(), self.ui.sec_lineEdit.text(), self.ui.year_lineEdit.text(),
                           self.ui.month_lineEdit.text(), self.ui.day_lineEdit.text(), "active")
            self.showInfo("Add", "Add is successful.")
            self.clear_func()
            self.hide()
        else:
            self.showError("Error", "Your list is full.")

    def submit_func(self):
        frame = self.check_frame()
        self.ui.title_lineEdit.setText(self.ui.title_lineEdit.text().strip())
        self.ui.des_lineEdit.setText(self.ui.des_lineEdit.text().strip())
        self.ui.day_lineEdit.setText(self.ui.day_lineEdit.text().strip())
        self.ui.month_lineEdit.setText(self.ui.month_lineEdit.text().strip())
        self.ui.year_lineEdit.setText(self.ui.year_lineEdit.text().strip())
        self.ui.sec_lineEdit.setText(self.ui.sec_lineEdit.text().strip())
        self.ui.min_lineEdit.setText(self.ui.min_lineEdit.text().strip())
        self.ui.hour_lineEdit.setText(self.ui.hour_lineEdit.text().strip())
        date_year_now = int(datetime.now().strftime("%Y"))
        date_year_after50 = int(datetime.now().strftime("%Y")) + 50
        date_month_now = int(datetime.now().strftime("%m"))
        date_day_now = int(datetime.now().strftime("%d"))
        if len(self.ui.title_lineEdit.text()) != 0:
            if len(self.ui.hour_lineEdit.text()) != 0:
                if self.ui.hour_lineEdit.text().isnumeric():
                    if 0 <= int(self.ui.hour_lineEdit.text()) <= 23:
                        if len(self.ui.min_lineEdit.text()) != 0:
                            if self.ui.min_lineEdit.text().isnumeric():
                                if 0 <= int(self.ui.min_lineEdit.text()) <= 59:
                                    if len(self.ui.sec_lineEdit.text()) != 0:
                                        if self.ui.sec_lineEdit.text().isnumeric():
                                            if 0 <= int(self.ui.sec_lineEdit.text()) <= 59:
                                                if len(self.ui.year_lineEdit.text()) != 0:
                                                    if self.ui.year_lineEdit.text().isnumeric():
                                                        if date_year_now <= int(
                                                                self.ui.year_lineEdit.text()) <= date_year_after50:
                                                            if len(self.ui.month_lineEdit.text()) != 0:
                                                                if self.ui.month_lineEdit.text().isnumeric():
                                                                    if date_month_now <= int(
                                                                            self.ui.month_lineEdit.text()) <= 12:
                                                                        if len(self.ui.day_lineEdit.text()) != 0:
                                                                            if self.ui.day_lineEdit.text().isnumeric():
                                                                                if int(self.ui.month_lineEdit.text()) in self.day_31:
                                                                                    if date_day_now <= int(
                                                                                            self.ui.day_lineEdit.text()) <= 31:
                                                                                        self.Add_event(frame)
                                                                                    else:
                                                                                        self.showError("Day",
                                                                                                       f"Day should be between {date_day_now}-31.")
                                                                                elif int(
                                                                                        self.ui.month_lineEdit.text()) in self.day_30:
                                                                                    if date_day_now <= int(
                                                                                            self.ui.day_lineEdit.text()) <= 30:
                                                                                        self.Add_event(frame)
                                                                                    else:
                                                                                        self.showError("Day",
                                                                                                       f"Day should be between {date_day_now}-30.")
                                                                                elif int(
                                                                                        self.ui.month_lineEdit.text()) == self.day_28:
                                                                                    if date_day_now <= int(
                                                                                            self.ui.day_lineEdit.text()) <= 28:
                                                                                        self.Add_event(frame)
                                                                                    else:
                                                                                        self.showError("Day",
                                                                                                       f"Day should be between {date_day_now}-28.")
                                                                            else:
                                                                                self.showError("Day type",
                                                                                               "Day should be number.")
                                                                        else:
                                                                            self.showError("Day",
                                                                                           "You should fill day.")
                                                                    else:
                                                                        self.showError("Month",
                                                                                       f"Month should be between {date_month_now}-12.")
                                                                else:
                                                                    self.showError("Month type",
                                                                                   "Month should be number.")
                                                            else:
                                                                self.showError("Month", "You should fill month.")
                                                        else:
                                                            self.showError("Year",
                                                                           f"Year should be between {date_year_now}-{date_year_after50}.")
                                                    else:
                                                        self.showError("Year type", "Year should be number.")
                                                else:
                                                    self.showError("Year", "You should fill year.")
                                            else:
                                                self.showError("Second", "Second should be between 00-59.")
                                        else:
                                            self.showError("Second type", "Second should be number.")
                                    else:
                                        self.showError("Second", "You should fill second.")
                                else:
                                    self.showError("Minute", "Minute should be between 00-59.")
                            else:
                                self.showError("Minute type", "Minute should be number.")
                        else:
                            self.showError("Minute", "You should fill minute.")
                    else:
                        self.showError("Hour", "Hour should be between 00-23.")
                else:
                    self.showError("Hour type", "Hour should be number.")
            else:
                self.showError("Hour", "You should fill hour.")
        else:
            self.showError("Title", "You should fill title.")

    def Anim_frame(self, x, y, width, height, openState):
        if openState:
            self.anim = QPropertyAnimation(self.ui.label, b"geometry")
            self.anim.setDuration(700)
            self.anim.setStartValue(QRect(x, y, 0, height))
            self.anim.setEndValue(QRect(x, y, width, height))
            self.anim.start()

    def getCenterWidget(self):
        return self.ui.centralwidget


class dateTable(QMainWindow):
    handle_menu = "close"
    handle_timer_frame_1 = 0
    handle_timer_frame_2 = 0
    handle_timer_frame_3 = 0
    handle_timer_frame_4 = 0
    handle_timer_frame_5 = 0
    handle_timer_frame_6 = 0
    deltaDays_1 = 0
    deltaDays_2 = 0
    deltaDays_3 = 0
    deltaDays_4 = 0
    deltaDays_5 = 0
    deltaDays_6 = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.addEventWin = addEvent()
        self.editEventWin = editEvent()
        self.settingEventWin = settingEvent()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Schedule")
        self.setWindowIcon(QIcon(r"photo\logo.png"))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.btn_frame.hide()
        self.ui.frame_1.hide()
        self.ui.frame_2.hide()
        self.ui.frame_3.hide()
        self.ui.frame_4.hide()
        self.ui.frame_5.hide()
        self.ui.frame_6.hide()
        timer = QTimer(self)
        timer.timeout.connect(self.time_mainWin)
        timer.start(1000)
        self.timer_frame_1 = QTimer(self)
        self.timer_frame_2 = QTimer(self)
        self.timer_frame_3 = QTimer(self)
        self.timer_frame_4 = QTimer(self)
        self.timer_frame_5 = QTimer(self)
        self.timer_frame_6 = QTimer(self)
        self.count_add()
        self.activeState()
        self.ui.menu_btn.clicked.connect(self.menu_func)
        self.ui.delete_btn_1.clicked.connect(self.delete_frame_1)
        self.ui.delete_btn_2.clicked.connect(self.delete_frame_2)
        self.ui.delete_btn_3.clicked.connect(self.delete_frame_3)
        self.ui.delete_btn_4.clicked.connect(self.delete_frame_4)
        self.ui.delete_btn_5.clicked.connect(self.delete_frame_5)
        self.ui.delete_btn_6.clicked.connect(self.delete_frame_6)
        self.ui.active_btn_1.clicked.connect(self.active_frame_1)
        self.ui.active_btn_2.clicked.connect(self.active_frame_2)
        self.ui.active_btn_3.clicked.connect(self.active_frame_3)
        self.ui.active_btn_4.clicked.connect(self.active_frame_4)
        self.ui.active_btn_5.clicked.connect(self.active_frame_5)
        self.ui.active_btn_6.clicked.connect(self.active_frame_6)
        self.ui.edit_btn_1.clicked.connect(self.edit_frame_1)
        self.ui.edit_btn_2.clicked.connect(self.edit_frame_2)
        self.ui.edit_btn_3.clicked.connect(self.edit_frame_3)
        self.ui.edit_btn_4.clicked.connect(self.edit_frame_4)
        self.ui.edit_btn_5.clicked.connect(self.edit_frame_5)
        self.ui.edit_btn_6.clicked.connect(self.edit_frame_6)

    def showInfo(self, title, msg):
        info = QMessageBox(self)
        info.setIcon(QMessageBox.Information)
        info.setText(msg)
        info.setWindowTitle(title)
        info.show()

    def showError(self, title, msg):
        info = QMessageBox(self)
        info.setIcon(QMessageBox.Critical)
        info.setText(msg)
        info.setWindowTitle(title)
        info.show()

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def count_add(self):
        alarms = backend.view()
        if len(alarms) == 6:
            self.ui.add_btn.setEnabled(False)
        else:
            self.ui.add_btn.setEnabled(True)

    def menu_func(self):
        if self.handle_menu == "close":
            self.ui.btn_frame.show()
            self.Anim_frame(self.ui.btn_frame, 70, 0, 521, 51, True)
            self.handle_menu = "open"
        elif self.handle_menu == "open":
            self.Anim_frame(self.ui.btn_frame, 70, 0, 521, 51, False)
            self.handle_menu = "close"
        self.ui.add_btn.clicked.connect(self.addEvent_func)
        self.ui.setting_btn.clicked.connect(self.setting_func)
        self.ui.refresh_btn.clicked.connect(self.refresh_func)
        self.ui.process_btn.clicked.connect(self.process_func)

    def Anim_frame(self, frame, x, y, width, height, openState):
        if openState:
            self.anim = QPropertyAnimation(frame, b"geometry")
            self.anim.setDuration(500)
            self.anim.setStartValue(QRect(x, y, 0, height))
            self.anim.setEndValue(QRect(x, y, width, height))
            self.anim.start()
        else:
            self.anim = QPropertyAnimation(frame, b"geometry")
            self.anim.setDuration(500)
            self.anim.setStartValue(QRect(x, y, width, height))
            self.anim.setEndValue(QRect(x, y, 0, height))
            self.anim.start()

    def addEvent_func(self):
        self.addEventWin.Anim_frame(150, 10, 201, 51, True)
        self.addEventWin.show()

    def setting_func(self):
        self.settingEventWin.Anim_frame("", 150, 10, 201, 51, "settingLabel", True)
        self.settingEventWin.show()

    def time_mainWin(self):
        time = QTime.currentTime()
        displayTime = time.toString('hh:mm:ss')
        self.ui.currentTime.setText(displayTime)

    def refresh_func(self):
        frameState_1 = backend.search("1")
        frameState_2 = backend.search("2")
        frameState_3 = backend.search("3")
        frameState_4 = backend.search("4")
        frameState_5 = backend.search("5")
        frameState_6 = backend.search("6")
        self.count_add()
        if len(frameState_1) != 0:
            self.ui.title_frame_1.setText(frameState_1[0][1])
            self.ui.Describtion_frame_1.setText(frameState_1[0][2])
            time1 = f"{frameState_1[0][3]}:{frameState_1[0][4]}:{frameState_1[0][5]}"
            self.ui.inputtime_frame_1.setText(time1)
            self.ui.date_frame_1.setText(f"{frameState_1[0][6]}/{frameState_1[0][7]}/{frameState_1[0][8]}")
            state = self.remainingDay_func("1", frameState_1[0][6], frameState_1[0][7], frameState_1[0][8])
            if state and frameState_1[0][9] == "active":
                self.timer_frame_1.timeout.connect(self.timer_1)
                self.timer_frame_1.start(1000)
                self.setActive_backend("1", True)
            self.ui.frame_1.show()
        if len(frameState_2) != 0:
            self.ui.title_frame_2.setText(frameState_2[0][1])
            self.ui.Describtion_frame_2.setText(frameState_2[0][2])
            time2 = f"{frameState_2[0][3]}:{frameState_2[0][4]}:{frameState_2[0][5]}"
            self.ui.inputtime_frame_2.setText(time2)
            self.ui.date_frame_2.setText(f"{frameState_2[0][6]}/{frameState_2[0][7]}/{frameState_2[0][8]}")
            state = self.remainingDay_func("2", frameState_2[0][6], frameState_2[0][7], frameState_2[0][8])
            if state and frameState_2[0][9] == "active":
                self.timer_frame_2.timeout.connect(self.timer_2)
                self.timer_frame_2.start(1000)
                self.setActive_backend("2", True)
            self.ui.frame_2.show()
        if len(frameState_3) != 0:
            self.ui.title_frame_3.setText(frameState_3[0][1])
            self.ui.Describtion_frame_3.setText(frameState_3[0][2])
            time3 = f"{frameState_3[0][3]}:{frameState_3[0][4]}:{frameState_3[0][5]}"
            self.ui.inputtime_frame_3.setText(time3)
            self.ui.date_frame_3.setText(f"{frameState_3[0][6]}/{frameState_3[0][7]}/{frameState_3[0][8]}")
            state = self.remainingDay_func("3", frameState_3[0][6], frameState_3[0][7], frameState_3[0][8])
            if state and frameState_3[0][9] == "active":
                self.timer_frame_3.timeout.connect(self.timer_3)
                self.timer_frame_3.start(1000)
                self.setActive_backend("3", True)
            self.ui.frame_3.show()
        if len(frameState_4) != 0:
            self.ui.title_frame_4.setText(frameState_4[0][1])
            self.ui.Describtion_frame_4.setText(frameState_4[0][2])
            time4 = f"{frameState_4[0][3]}:{frameState_4[0][4]}:{frameState_4[0][5]}"
            self.ui.inputtime_frame_4.setText(time4)
            self.ui.date_frame_4.setText(f"{frameState_4[0][6]}/{frameState_4[0][7]}/{frameState_4[0][8]}")
            state = self.remainingDay_func("4", frameState_4[0][6], frameState_4[0][7], frameState_4[0][8])
            if state and frameState_4[0][9] == "active":
                self.timer_frame_4.timeout.connect(self.timer_4)
                self.timer_frame_4.start(1000)
                self.setActive_backend("4", True)
            self.ui.frame_4.show()
        if len(frameState_5) != 0:
            self.ui.title_frame_5.setText(frameState_5[0][1])
            self.ui.Describtion_frame_5.setText(frameState_5[0][2])
            time5 = f"{frameState_5[0][3]}:{frameState_5[0][4]}:{frameState_5[0][5]}"
            self.ui.inputtime_frame_5.setText(time5)
            self.ui.date_frame_5.setText(f"{frameState_5[0][6]}/{frameState_5[0][7]}/{frameState_5[0][8]}")
            state = self.remainingDay_func("5", frameState_5[0][6], frameState_5[0][7], frameState_5[0][8])
            if state and frameState_5[0][9] == "active":
                self.timer_frame_5.timeout.connect(self.timer_5)
                self.timer_frame_5.start(1000)
                self.setActive_backend("5", True)
            self.ui.frame_5.show()
        if len(frameState_6) != 0:
            self.ui.title_frame_6.setText(frameState_6[0][1])
            self.ui.Describtion_frame_6.setText(frameState_6[0][2])
            time6 = f"{frameState_6[0][3]}:{frameState_6[0][4]}:{frameState_6[0][5]}"
            self.ui.inputtime_frame_6.setText(time6)
            self.ui.date_frame_6.setText(f"{frameState_6[0][6]}/{frameState_6[0][7]}/{frameState_6[0][8]}")
            state = self.remainingDay_func("6", frameState_6[0][6], frameState_6[0][7], frameState_6[0][8])
            if state and frameState_6[0][9] == "active":
                self.timer_frame_6.timeout.connect(self.timer_6)
                self.timer_frame_6.start(1000)
                self.setActive_backend("6", True)
            self.ui.frame_6.show()

    def activeState(self):
        frameState_1 = backend.search("1")
        frameState_2 = backend.search("2")
        frameState_3 = backend.search("3")
        frameState_4 = backend.search("4")
        frameState_5 = backend.search("5")
        frameState_6 = backend.search("6")
        if len(frameState_1) != 0:
            if frameState_1[0][9] == "deActive":
                self.deltaDays_1 = -1
        elif len(frameState_2) != 0:
            if frameState_2[0][9] == "deActive":
                self.deltaDays_2 = -1
        elif len(frameState_3) != 0:
            if frameState_3[0][9] == "deActive":
                self.deltaDays_3 = -1
        elif len(frameState_4) != 0:
            if frameState_4[0][9] == "deActive":
                self.deltaDays_4 = -1
        elif len(frameState_5) != 0:
            if frameState_5[0][9] == "deActive":
                self.deltaDays_5 = -1
        elif len(frameState_6) != 0:
            if frameState_6[0][9] == "deActive":
                self.deltaDays_6 = -1

    def timer_1(self):
        frameState_1 = backend.search("1")
        inputTime = f"{frameState_1[0][3]}:{frameState_1[0][4]}:{frameState_1[0][5]}"
        formatTime = '%H:%M:%S'
        time1 = QTime.currentTime()
        displayTime = time1.toString('hh:mm:ss')
        deltaTime = datetime.strptime(inputTime, formatTime) - datetime.strptime(displayTime, formatTime)
        self.deltaDays_1 = deltaTime.days
        if deltaTime.days < 0:
            self.ui.retime_frame_1.setText("00:00:00")
            self.timer_frame_1.stop()
            self.setActive_backend("1", False)
            self.handle_timer_frame_1 = 1
        else:
            if self.handle_timer_frame_1 == 0:
                self.ui.retime_frame_1.setText(str(deltaTime))

    def timer_2(self):
        frameState_2 = backend.search("2")
        inputTime = f"{frameState_2[0][3]}:{frameState_2[0][4]}:{frameState_2[0][5]}"
        formatTime = '%H:%M:%S'
        time2 = QTime.currentTime()
        displayTime = time2.toString('hh:mm:ss')
        deltaTime = datetime.strptime(inputTime, formatTime) - datetime.strptime(displayTime, formatTime)
        self.deltaDays_2 = deltaTime.days
        if deltaTime.days < 0:
            self.ui.retime_frame_2.setText("00:00:00")
            self.timer_frame_2.stop()
            self.setActive_backend("2", False)
            self.handle_timer_frame_2 = 1
        else:
            if self.handle_timer_frame_2 == 0:
                self.ui.retime_frame_2.setText(str(deltaTime))

    def timer_3(self):
        frameState_3 = backend.search("3")
        inputTime = f"{frameState_3[0][3]}:{frameState_3[0][4]}:{frameState_3[0][5]}"
        formatTime = '%H:%M:%S'
        time3 = QTime.currentTime()
        displayTime = time3.toString('hh:mm:ss')
        deltaTime = datetime.strptime(inputTime, formatTime) - datetime.strptime(displayTime, formatTime)
        self.deltaDays_3 = deltaTime.days
        if deltaTime.days < 0:
            self.ui.retime_frame_3.setText("00:00:00")
            self.timer_frame_3.stop()
            self.setActive_backend("3", False)
            self.handle_timer_frame_3 = 1
        else:
            if self.handle_timer_frame_3 == 0:
                self.ui.retime_frame_3.setText(str(deltaTime))

    def timer_4(self):
        frameState_4 = backend.search("4")
        inputTime = f"{frameState_4[0][3]}:{frameState_4[0][4]}:{frameState_4[0][5]}"
        formatTime = '%H:%M:%S'
        time4 = QTime.currentTime()
        displayTime = time4.toString('hh:mm:ss')
        deltaTime = datetime.strptime(inputTime, formatTime) - datetime.strptime(displayTime, formatTime)
        self.deltaDays_4 = deltaTime.days
        if deltaTime.days < 0:
            self.ui.retime_frame_4.setText("00:00:00")
            self.timer_frame_4.stop()
            self.setActive_backend("4", False)
            self.handle_timer_frame_4 = 1
        else:
            if self.handle_timer_frame_4 == 0:
                self.ui.retime_frame_4.setText(str(deltaTime))

    def timer_5(self):
        frameState_5 = backend.search("5")
        inputTime = f"{frameState_5[0][3]}:{frameState_5[0][4]}:{frameState_5[0][5]}"
        formatTime = '%H:%M:%S'
        time5 = QTime.currentTime()
        displayTime = time5.toString('hh:mm:ss')
        deltaTime = datetime.strptime(inputTime, formatTime) - datetime.strptime(displayTime, formatTime)
        self.deltaDays_5 = deltaTime.days
        if deltaTime.days < 0:
            self.ui.retime_frame_5.setText("00:00:00")
            self.timer_frame_5.stop()
            self.setActive_backend("5", False)
            self.handle_timer_frame_5 = 1
        else:
            if self.handle_timer_frame_5 == 0:
                self.ui.retime_frame_5.setText(str(deltaTime))

    def timer_6(self):
        frameState_6 = backend.search("6")
        inputTime = f"{frameState_6[0][3]}:{frameState_6[0][4]}:{frameState_6[0][5]}"
        formatTime = '%H:%M:%S'
        time6 = QTime.currentTime()
        displayTime = time6.toString('hh:mm:ss')
        deltaTime = datetime.strptime(inputTime, formatTime) - datetime.strptime(displayTime, formatTime)
        self.deltaDays_6 = deltaTime.days
        if deltaTime.days < 0:
            self.ui.retime_frame_6.setText("00:00:00")
            self.timer_frame_6.stop()
            self.setActive_backend("6", False)
            self.handle_timer_frame_6 = 1
        else:
            if self.handle_timer_frame_6 == 0:
                self.ui.retime_frame_6.setText(str(deltaTime))

    def remainingDay_func(self, frame, year, month, day):
        yearNow = int(datetime.today().strftime("%Y"))
        monthNow = int(datetime.today().strftime("%m"))
        dayNow = int(datetime.today().strftime("%d"))
        inputDate = date(int(year), int(month), int(day))
        currentDate = date(yearNow, monthNow, dayNow)
        delta = inputDate - currentDate
        if frame == "1":
            self.ui.day_re_frame_1.setText(f"{delta.days} d")
            if delta.days < 0:
                self.setActive_backend("1", False)
        elif frame == "2":
            self.ui.day_re_frame_2.setText(f"{delta.days} d")
            if delta.days < 0:
                self.setActive_backend("2", False)
        elif frame == "3":
            self.ui.day_re_frame_3.setText(f"{delta.days} d")
            if delta.days < 0:
                self.setActive_backend("3", False)
        elif frame == "4":
            self.ui.day_re_frame_4.setText(f"{delta.days} d")
            if delta.days < 0:
                self.setActive_backend("4", False)
        elif frame == "5":
            self.ui.day_re_frame_5.setText(f"{delta.days} d")
            if delta.days < 0:
                self.setActive_backend("5", False)
        elif frame == "6":
            self.ui.day_re_frame_6.setText(f"{delta.days} d")
            if delta.days < 0:
                self.setActive_backend("6", False)
        if delta.days == 0:
            return True
        else:
            return False

    def delete_ques(self):
        btnReply = QMessageBox.question(self, "Delete", "Are you sure ?", QMessageBox.Yes | QMessageBox.No)
        if btnReply == QMessageBox.Yes:
            return True
        elif btnReply == QMessageBox.No:
            return False

    def delete_frame_1(self):
        state = self.delete_ques()
        if state:
            self.ui.frame_1.hide()
            self.timer_frame_1.stop()
            backend.delete("1")
            self.count_add()

    def delete_frame_2(self):
        state = self.delete_ques()
        if state:
            self.ui.frame_2.hide()
            self.timer_frame_2.stop()
            backend.delete("2")
            self.count_add()

    def delete_frame_3(self):
        state = self.delete_ques()
        if state:
            self.ui.frame_3.hide()
            self.timer_frame_3.stop()
            backend.delete("3")
            self.count_add()

    def delete_frame_4(self):
        state = self.delete_ques()
        if state:
            self.ui.frame_4.hide()
            self.timer_frame_4.stop()
            backend.delete("4")
            self.count_add()

    def delete_frame_5(self):
        state = self.delete_ques()
        if state:
            self.ui.frame_5.hide()
            self.timer_frame_5.stop()
            backend.delete("5")
            self.count_add()

    def delete_frame_6(self):
        state = self.delete_ques()
        if state:
            self.ui.frame_6.hide()
            self.timer_frame_6.stop()
            backend.delete("6")
            self.count_add()

    def setActive_backend(self, frame, state):
        _translate = QCoreApplication.translate
        if frame == "1":
            if state:
                backend.update_active("1", "active")
                self.ui.active_btn_1.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(7, 161, 4);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_1.setToolTip(_translate("MainWindow", "Active"))
            else:
                backend.update_active("1", "deActive")
                self.ui.active_btn_1.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    	background - color: rgb(115, 115, 115);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_1.setToolTip(_translate("MainWindow", "DeActive"))
        elif frame == "2":
            if state:
                backend.update_active("2", "active")
                self.ui.active_btn_2.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    	background-color: rgb(1, 147, 1);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_2.setToolTip(_translate("MainWindow", "Active"))
            else:
                backend.update_active("2", "deActive")
                self.ui.active_btn_2.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    	background - color: rgb(115, 115, 115);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_2.setToolTip(_translate("MainWindow", "DeActive"))
        elif frame == "3":
            if state:
                backend.update_active("3", "active")
                self.ui.active_btn_3.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(1, 147, 1);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_3.setToolTip(_translate("MainWindow", "Active"))
            else:
                backend.update_active("3", "deActive")
                self.ui.active_btn_3.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(115, 115, 115);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_3.setToolTip(_translate("MainWindow", "DeActive"))
        elif frame == "4":
            if state:
                backend.update_active("4", "active")
                self.ui.active_btn_4.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    	background-color: rgb(1, 147, 1);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_4.setToolTip(_translate("MainWindow", "Active"))
            else:
                backend.update_active("4", "deActive")
                self.ui.active_btn_4.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    	background - color: rgb(115, 115, 115);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_4.setToolTip(_translate("MainWindow", "DeActive"))
        elif frame == "5":
            if state:
                backend.update_active("5", "active")
                self.ui.active_btn_5.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    	background-color: rgb(1, 147, 1);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_5.setToolTip(_translate("MainWindow", "Active"))
            else:
                backend.update_active("5", "deActive")
                self.ui.active_btn_5.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    	background - color: rgb(115, 115, 115);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_5.setToolTip(_translate("MainWindow", "DeActive"))
        elif frame == "6":
            if state:
                backend.update_active("6", "active")
                self.ui.active_btn_6.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    	background-color: rgb(1, 147, 1);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_6.setToolTip(_translate("MainWindow", "Active"))
            else:
                backend.update_active("6", "deActive")
                self.ui.active_btn_6.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    	background - color: rgb(115, 115, 115);\n"
                                                   "border-radius:10px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(85, 85, 85);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
                self.ui.active_btn_6.setToolTip(_translate("MainWindow", "DeActive"))

    def active_frame_1(self):
        frameState_1 = backend.search("1")
        yearNow = int(datetime.today().strftime("%Y"))
        monthNow = int(datetime.today().strftime("%m"))
        dayNow = int(datetime.today().strftime("%d"))
        inputDate = date(int(frameState_1[0][6]), int(frameState_1[0][7]), int(frameState_1[0][8]))
        currentDate = date(yearNow, monthNow, dayNow)
        delta = inputDate - currentDate
        if delta.days >= 0:
            if self.deltaDays_1 >= 0:
                if frameState_1[0][9] == "active":
                    self.setActive_backend("1", False)
                elif frameState_1[0][9] == "deActive":
                    self.setActive_backend("1", True)

    def active_frame_2(self):
        frameState_2 = backend.search("2")
        yearNow = int(datetime.today().strftime("%Y"))
        monthNow = int(datetime.today().strftime("%m"))
        dayNow = int(datetime.today().strftime("%d"))
        inputDate = date(int(frameState_2[0][6]), int(frameState_2[0][7]), int(frameState_2[0][8]))
        currentDate = date(yearNow, monthNow, dayNow)
        delta = inputDate - currentDate
        if delta.days >= 0:
            if self.deltaDays_2 >= 0:
                if frameState_2[0][9] == "active":
                    self.setActive_backend("2", False)
                elif frameState_2[0][9] == "deActive":
                    self.setActive_backend("2", True)

    def active_frame_3(self):
        frameState_3 = backend.search("3")
        yearNow = int(datetime.today().strftime("%Y"))
        monthNow = int(datetime.today().strftime("%m"))
        dayNow = int(datetime.today().strftime("%d"))
        inputDate = date(int(frameState_3[0][6]), int(frameState_3[0][7]), int(frameState_3[0][8]))
        currentDate = date(yearNow, monthNow, dayNow)
        delta = inputDate - currentDate
        if delta.days >= 0:
            if self.deltaDays_3 >= 0:
                if frameState_3[0][9] == "active":
                    self.setActive_backend("3", False)
                elif frameState_3[0][9] == "deActive":
                    self.setActive_backend("3", True)

    def active_frame_4(self):
        frameState_4 = backend.search("4")
        yearNow = int(datetime.today().strftime("%Y"))
        monthNow = int(datetime.today().strftime("%m"))
        dayNow = int(datetime.today().strftime("%d"))
        inputDate = date(int(frameState_4[0][6]), int(frameState_4[0][7]), int(frameState_4[0][8]))
        currentDate = date(yearNow, monthNow, dayNow)
        delta = inputDate - currentDate
        if delta.days >= 0:
            if self.deltaDays_4 >= 0:
                if frameState_4[0][9] == "active":
                    self.setActive_backend("4", False)
                elif frameState_4[0][9] == "deActive":
                    self.setActive_backend("4", True)

    def active_frame_5(self):
        frameState_5 = backend.search("5")
        yearNow = int(datetime.today().strftime("%Y"))
        monthNow = int(datetime.today().strftime("%m"))
        dayNow = int(datetime.today().strftime("%d"))
        inputDate = date(int(frameState_5[0][6]), int(frameState_5[0][7]), int(frameState_5[0][8]))
        currentDate = date(yearNow, monthNow, dayNow)
        delta = inputDate - currentDate
        if delta.days >= 0:
            if self.deltaDays_5 >= 0:
                if frameState_5[0][9] == "active":
                    self.setActive_backend("5", False)
                elif frameState_5[0][9] == "deActive":
                    self.setActive_backend("5", True)

    def active_frame_6(self):
        frameState_6 = backend.search("6")
        yearNow = int(datetime.today().strftime("%Y"))
        monthNow = int(datetime.today().strftime("%m"))
        dayNow = int(datetime.today().strftime("%d"))
        inputDate = date(int(frameState_6[0][6]), int(frameState_6[0][7]), int(frameState_6[0][8]))
        currentDate = date(yearNow, monthNow, dayNow)
        delta = inputDate - currentDate
        if delta.days >= 0:
            if self.deltaDays_6 >= 0:
                if frameState_6[0][9] == "active":
                    self.setActive_backend("6", False)
                elif frameState_6[0][9] == "deActive":
                    self.setActive_backend("6", True)

    def process_func(self):
        dayList = self.getListActiveEvent()
        _thread.start_new_thread(self.process_day, (dayList,))

    def process_day(self, dayList):
        if len(dayList) != 0:
            self.ui.process_btn.setStyleSheet("QPushButton{\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "    \n"
                                              "    background-color: rgb(2, 135, 7);\n"
                                              "border-radius:10px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "    background-color: rgb(95, 95, 95);\n"
                                              "border-radius:5px;\n"
                                              "}")
            while True:
                currentTime = QTime.currentTime()
                hour = int(currentTime.toString("hh"))
                minute = int(currentTime.toString("mm"))
                second = int(currentTime.toString("ss"))
                for event in dayList:
                    if event[9] == "active":
                        if int(event[3]) == hour:
                            if int(event[4]) == minute:
                                if int(event[5]) == second:
                                    self.notify_func(event)
                                    self.setActive_backend(event[0], False)
                                    dayList.remove(event)
                                    time.sleep(0.5)
                if len(dayList) == 0:
                    self.ui.process_btn.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    \n"
                                                      "    background-color: rgb(115, 115, 115);\n"
                                                      "border-radius:10px;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
                    break

    @staticmethod
    def notify_func(event):
        notify_1 = Notify()
        notify_1.title = event[1]
        notify_1.message = f"{event[2]}\nTime : {event[3]}:{event[4]}:{event[5]} - {event[6]}/{event[7]}/{event[8]}"
        notify_1.audio = r"photo\mixkit-tile-game-reveal-960.wav"
        notify_1.send()

    @staticmethod
    def getListActiveEvent():
        AllEvent = backend.view()
        activeList = list()
        YearList = list()
        MonthList = list()
        DayList = list()
        yearNow = int(datetime.today().strftime("%Y"))
        monthNow = int(datetime.today().strftime("%m"))
        dayNow = int(datetime.today().strftime("%d"))
        for event in AllEvent:
            if event[9] == "active":
                activeList.append(event)
        for event in activeList:
            if int(event[6]) == yearNow:
                YearList.append(event)
        for event in activeList:
            if int(event[7]) == monthNow:
                MonthList.append(event)
        for event in activeList:
            if int(event[8]) == dayNow:
                DayList.append(event)
        return DayList

    def edit_frame_1(self):
        self.editEventWin.insertInformation("1")
        self.editEventWin.Anim_frame(150, 10, 201, 51, True)
        self.editEventWin.show()

    def edit_frame_2(self):
        self.editEventWin.insertInformation("2")
        self.editEventWin.Anim_frame(150, 10, 201, 51, True)
        self.editEventWin.show()

    def edit_frame_3(self):
        self.editEventWin.insertInformation("3")
        self.editEventWin.Anim_frame(150, 10, 201, 51, True)
        self.editEventWin.show()

    def edit_frame_4(self):
        self.editEventWin.insertInformation("4")
        self.editEventWin.Anim_frame(150, 10, 201, 51, True)
        self.editEventWin.show()

    def edit_frame_5(self):
        self.editEventWin.insertInformation("5")
        self.editEventWin.Anim_frame(150, 10, 201, 51, True)
        self.editEventWin.show()

    def edit_frame_6(self):
        self.editEventWin.insertInformation("6")
        self.editEventWin.Anim_frame(150, 10, 201, 51, True)
        self.editEventWin.show()

    def getCenterWidget(self):
        return self.ui.centralwidget


def setup():
    app = QApplication([])
    ui = dateTable()
    ui.show()
    app.exec_()


setup()
