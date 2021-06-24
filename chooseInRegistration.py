# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseInRegistration.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from newCourseEnrollment import *


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(1223, 839)
        RegistrationWindow.setStyleSheet("QMainWindow{\n"
                                            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(13, 115, 119, 255), stop:1 rgba(33, 33, 33, 255));\n"
                                            "}\n"
                                            "\n"
                                            "QLabel{\n"
                                            "color: #32e0c4;\n"
                                            "}\n"
                                            "\n"
                                            "")
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.registrationLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.registrationLabel.setFont(font)
        self.registrationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registrationLabel.setObjectName("registrationLabel")
        self.verticalLayout_5.addWidget(self.registrationLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(740, 470))
        self.frame.setMaximumSize(QtCore.QSize(760, 470))
        self.frame.setStyleSheet("QFrame{\n"
                                 "background-color: rgb(33, 33, 33);\n"
                                 "border-radius: 25px;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "color: #eeeeee;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton{\n"
                                 "background-color: rgb(13, 115, 119);\n"
                                 "border-radius: 80px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover{\n"
                                 "background-color: rgb(50, 224, 196);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#cancelButton{\n"
                                 "color: #eeeeee;\n"
                                 "background-color: #212121;\n"
                                 "border: 2px solid #9a0002;\n"
                                 "border-radius: 25px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#cancelButton:hover{\n"
                                 "border: 3px solid rgb(255, 0, 0);\n"
                                 "background-color: #9a0002;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.newRegistrationButton = QtWidgets.QPushButton(self.frame)
        self.newRegistrationButton.setMinimumSize(QtCore.QSize(161, 161))
        self.newRegistrationButton.setMaximumSize(QtCore.QSize(161, 161))
        self.newRegistrationButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.newRegistrationButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/registration/addStudent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newRegistrationButton.setIcon(icon)
        self.newRegistrationButton.setIconSize(QtCore.QSize(80, 80))
        self.newRegistrationButton.setObjectName("newRegistrationButton")
        self.verticalLayout.addWidget(self.newRegistrationButton)
        self.newRegistrationLabel = QtWidgets.QLabel(self.frame)
        self.newRegistrationLabel.setMinimumSize(QtCore.QSize(161, 31))
        self.newRegistrationLabel.setMaximumSize(QtCore.QSize(161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newRegistrationLabel.setFont(font)
        self.newRegistrationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newRegistrationLabel.setObjectName("newRegistrationLabel")
        self.verticalLayout.addWidget(self.newRegistrationLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.newCourseButton = QtWidgets.QPushButton(self.frame)
        self.newCourseButton.setMinimumSize(QtCore.QSize(161, 161))
        self.newCourseButton.setMaximumSize(QtCore.QSize(161, 161))
        self.newCourseButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.newCourseButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/registration/enroll.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newCourseButton.setIcon(icon1)
        self.newCourseButton.setIconSize(QtCore.QSize(80, 80))
        self.newCourseButton.setObjectName("newCourseButton")
        self.verticalLayout_2.addWidget(self.newCourseButton)
        self.newCourseLabel = QtWidgets.QLabel(self.frame)
        self.newCourseLabel.setMinimumSize(QtCore.QSize(161, 31))
        self.newCourseLabel.setMaximumSize(QtCore.QSize(161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newCourseLabel.setFont(font)
        self.newCourseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newCourseLabel.setObjectName("newCourseLabel")
        self.verticalLayout_2.addWidget(self.newCourseLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setMinimumSize(QtCore.QSize(150, 50))
        self.cancelButton.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 0, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.frame)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 1, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 2, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 1, 0, 1, 1)
        RegistrationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegistrationWindow)
        self.statusbar.setObjectName("statusbar")
        RegistrationWindow.setStatusBar(self.statusbar)
        self.newCourseButton.clicked.connect(self.enrollNewCourse)
        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)


        ####### Added Code ########3

        # Database Connector Object
        self.mydb = RegistrationWindow.mydb

    def enrollNewCourse(self):
        self.newCourseEnroll = QtWidgets.QDialog()
        self.ui = Ui_NewCourseEnrollmentWindow()
        self.ui.setupUi(self.newCourseEnroll,self.mydb)
        self.newCourseEnroll.show()
        self.ui.cancelButton.clicked.connect(self.newCourseEnroll.close)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "MainWindow"))
        self.registrationLabel.setText(_translate("RegistrationWindow", "NEW REGISTRATION"))
        self.newRegistrationLabel.setText(_translate("RegistrationWindow", "New Registration"))
        self.newCourseLabel.setText(_translate("RegistrationWindow", "New Course"))
        self.cancelButton.setText(_translate("RegistrationWindow", "Back"))


import registration_rc
