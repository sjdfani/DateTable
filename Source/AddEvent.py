# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddEvent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddWin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 495)
        MainWindow.setMaximumSize(QtCore.QSize(491, 495))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(491, 495))
        self.centralwidget.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #304352, stop:1 #d7d2cc);\n"
            "border-radius:5px;")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:none;\n"
                                 "border-Bottom:1px solid black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:none;")
        self.label_2.setObjectName("label_2")
        self.title_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.title_lineEdit.setGeometry(QtCore.QRect(97, 102, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.title_lineEdit.setFont(font)
        self.title_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius:15px;")
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:none;")
        self.label_3.setObjectName("label_3")
        self.des_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.des_lineEdit.setGeometry(QtCore.QRect(100, 210, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.des_lineEdit.setFont(font)
        self.des_lineEdit.setToolTip("")
        self.des_lineEdit.setStatusTip("")
        self.des_lineEdit.setWhatsThis("")
        self.des_lineEdit.setAccessibleName("")
        self.des_lineEdit.setAccessibleDescription("")
        self.des_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:15px;")
        self.des_lineEdit.setObjectName("des_lineEdit")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(440, 10, 41, 21))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                "border-radius:10px;")
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 279, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:none;")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(104, 260, 271, 61))
        self.frame.setStyleSheet("background-color: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.hour_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.hour_lineEdit.setGeometry(QtCore.QRect(21, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.hour_lineEdit.setFont(font)
        self.hour_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius:15px;")
        self.hour_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_lineEdit.setObjectName("hour_lineEdit")
        self.min_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.min_lineEdit.setGeometry(QtCore.QRect(107, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.min_lineEdit.setFont(font)
        self.min_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:15px;")
        self.min_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.min_lineEdit.setObjectName("min_lineEdit")
        self.sec_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.sec_lineEdit.setGeometry(QtCore.QRect(200, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.sec_lineEdit.setFont(font)
        self.sec_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:15px;")
        self.sec_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.sec_lineEdit.setObjectName("sec_lineEdit")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(173, 18, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: none;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(83, 18, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:none;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(383, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: none;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 366, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:none;")
        self.label_8.setObjectName("label_8")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(104, 350, 271, 61))
        self.frame_2.setStyleSheet("background-color:none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.year_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.year_lineEdit.setGeometry(QtCore.QRect(21, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.year_lineEdit.setFont(font)
        self.year_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius:15px;")
        self.year_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.year_lineEdit.setObjectName("year_lineEdit")
        self.month_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.month_lineEdit.setGeometry(QtCore.QRect(110, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.month_lineEdit.setFont(font)
        self.month_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius:15px;")
        self.month_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.month_lineEdit.setObjectName("month_lineEdit")
        self.day_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.day_lineEdit.setGeometry(QtCore.QRect(200, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.day_lineEdit.setFont(font)
        self.day_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:15px;")
        self.day_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.day_lineEdit.setObjectName("day_lineEdit")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(81, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:none;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(170, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: none;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(380, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: none;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(120, 440, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.clear_btn.setFont(font)
        self.clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_btn.setStyleSheet("QPushButton{\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/outline_clear_all_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_btn.setIcon(icon)
        self.clear_btn.setIconSize(QtCore.QSize(32, 32))
        self.clear_btn.setObjectName("clear_btn")
        self.submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.submit_btn.setGeometry(QtCore.QRect(300, 440, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.submit_btn.setFont(font)
        self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_btn.setStyleSheet("QPushButton{\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("photo/outline_done_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit_btn.setIcon(icon1)
        self.submit_btn.setIconSize(QtCore.QSize(32, 32))
        self.submit_btn.setObjectName("submit_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Add Event Tab"))
        self.label_2.setText(_translate("MainWindow", "Title :"))
        self.label_3.setText(_translate("MainWindow", "Description :"))
        self.label_4.setText(_translate("MainWindow", "Time :"))
        self.label_6.setText(_translate("MainWindow", ":"))
        self.label_5.setText(_translate("MainWindow", ":"))
        self.label_7.setText(_translate("MainWindow", "( hh-mm-ss )"))
        self.label_8.setText(_translate("MainWindow", "Date : "))
        self.label_9.setText(_translate("MainWindow", "/"))
        self.label_10.setText(_translate("MainWindow", "/"))
        self.label_11.setText(_translate("MainWindow", "( yy-mm-dd )"))
        self.clear_btn.setText(_translate("MainWindow", "  Clear"))
        self.submit_btn.setText(_translate("MainWindow", " Submit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
