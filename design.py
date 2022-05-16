import sys
import sqlite3
import time
import hashlib
from sqlite3 import Cursor, Connection

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow


class UiRTFNetwork(object):

    def setup_ui(self, rtf_network):
        rtf_network.setObjectName("RTFNetwork")
        rtf_network.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(rtf_network)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Auntification = QtWidgets.QWidget()
        self.Auntification.setObjectName("Auntification")
        self.background = QtWidgets.QLabel(self.Auntification)
        self.background.setGeometry(QtCore.QRect(0, 0, 1920, 850))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.background.setFont(font)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/Rectangle 1.svg"))
        self.background.setObjectName("background")
        self.frameOfLogo = QtWidgets.QLabel(self.Auntification)
        self.frameOfLogo.setGeometry(QtCore.QRect(735, 50, 450, 450))
        self.frameOfLogo.setText("")
        self.frameOfLogo.setPixmap(QtGui.QPixmap("images/Rectangle 18.svg"))
        self.frameOfLogo.setObjectName("frameOfLogo")
        self.OutorIn = QtWidgets.QPushButton(self.Auntification)
        self.OutorIn.setGeometry(QtCore.QRect(785, 800, 350, 100))
        self.OutorIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OutorIn.setStyleSheet("QPushButton {\n"
                                   "position: absolute;\n"
                                   "width: 350px;\n"
                                   "height: 100px;\n"
                                   "left: 785px;\n"
                                   "top: 800px;\n"
                                   "\n"
                                   "position: absolute;\n"
                                   "width: 136px;\n"
                                   "height: 55px;\n"
                                   "left: 892px;\n"
                                   "top: 823px;\n"
                                   "\n"
                                   "font-family: \'SF Pro Display\';\n"
                                   "font-style: italic;\n"
                                   "font-weight: 600;\n"
                                   "font-size: 46px;\n"
                                   "line-height: 55px;\n"
                                   "/* identical to box height */\n"
                                   "\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "text-align: center;\n"
                                   "letter-spacing: 0.03em;\n"
                                   "\n"
                                   "color: #FFFFFF;\n"
                                   "\n"
                                   "background:qlineargradient(spread:pad, x1:0.169, y1:0.0180455, x2:0.791, "
                                   "y2:0.836, stop:0 rgba(105, 246, 255, 255), stop:1 rgba(67, 58, 166, 255));\n "
                                   "border: 1px solid #C4C4C4;\n"
                                   "box-sizing: border-box;\n"
                                   "border-radius: 25px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed{\n"
                                   "background-color:qlineargradient(spread:pad, x1:1, y1:0.478, x2:0, y2:0.466, "
                                   "stop:0 rgba(67, 58, 166, 255), stop:1 rgba(67, 58, 166, 255)); \n "
                                   "}")
        self.OutorIn.setObjectName("OutorIn")
        self.Question = QtWidgets.QLabel(self.Auntification)
        self.Question.setGeometry(QtCore.QRect(150, 1001, 246, 29))
        self.Question.setText("")
        self.Question.setPixmap(QtGui.QPixmap("images/У вас ещё нет аккаунта_.svg"))
        self.Question.setObjectName("Question")
        self.Login = QtWidgets.QLineEdit(self.Auntification)
        self.Login.setGeometry(QtCore.QRect(735, 550, 450, 75))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.Login.setFont(font)
        self.Login.setAcceptDrops(True)
        self.Login.setToolTipDuration(3)
        self.Login.setAutoFillBackground(False)
        self.Login.setStyleSheet("QLineEdit {\n"
                                 "position: absolute;\n"
                                 "width: 450px;\n"
                                 "height: 75px;\n"
                                 "left: 735px;\n"
                                 "top: 550px;\n"
                                 "padding-left: 40px;\n"
                                 "padding-right: 80px;\n"
                                 "\n"
                                 "background: #FFFFFF;\n"
                                 "border: 1px solid #C4C4C4;\n"
                                 "box-sizing: border-box;\n"
                                 "border-radius: 10px;\n"
                                 "}")
        self.Login.setText("")
        self.Login.setCursorPosition(0)
        self.Login.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Login.setObjectName("Login")
        self.Lock = QtWidgets.QLabel(self.Auntification)
        self.Lock.setGeometry(QtCore.QRect(1115, 672, 40, 40))
        self.Lock.setStyleSheet("")
        self.Lock.setText("")
        self.Lock.setPixmap(QtGui.QPixmap("images/image 5.png"))
        self.Lock.setObjectName("Lock")
        self.Logo = QtWidgets.QLabel(self.Auntification)
        self.Logo.setGeometry(QtCore.QRect(835, 75, 250, 250))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("images/image 1.png"))
        self.Logo.setObjectName("Logo")
        self.Letter = QtWidgets.QLabel(self.Auntification)
        self.Letter.setGeometry(QtCore.QRect(1115, 567, 40, 40))
        self.Letter.setStyleSheet("")
        self.Letter.setText("")
        self.Letter.setPixmap(QtGui.QPixmap("images/image 7.png"))
        self.Letter.setObjectName("Letter")
        self.Password = QtWidgets.QLineEdit(self.Auntification)
        self.Password.setGeometry(QtCore.QRect(735, 655, 450, 75))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.Password.setFont(font)
        self.Password.setToolTipDuration(3)
        self.Password.setStyleSheet("QLineEdit {\n"
                                    "position: absolute;\n"
                                    "width: 450px;\n"
                                    "height: 75px;\n"
                                    "left: 735px;\n"
                                    "top: 550px;\n"
                                    "padding-left: 40px;\n"
                                    "padding-right: 80px;\n"
                                    "\n"
                                    "\n"
                                    "background: #FFFFFF;\n"
                                    "border: 1px solid #C4C4C4;\n"
                                    "box-sizing: border-box;\n"
                                    "border-radius: 10px;\n"
                                    "}")
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.TextUnderLogo = QtWidgets.QLabel(self.Auntification)
        self.TextUnderLogo.setGeometry(QtCore.QRect(810, 355, 299, 114))
        self.TextUnderLogo.setText("")
        self.TextUnderLogo.setPixmap(QtGui.QPixmap("images/Нейронная сеть.svg"))
        self.TextUnderLogo.setObjectName("TextUnderLogo")
        self.ExitAuntification = QtWidgets.QPushButton(self.Auntification)
        self.ExitAuntification.setGeometry(QtCore.QRect(1860, 20, 40, 40))
        self.ExitAuntification.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitAuntification.setStyleSheet("QPushButton{\n"
                                             "border-radius: 1px\n"
                                             "}")
        self.ExitAuntification.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/cross-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitAuntification.setIcon(icon)
        self.ExitAuntification.setIconSize(QtCore.QSize(40, 40))
        self.ExitAuntification.setFlat(True)
        self.ExitAuntification.setObjectName("ExitAuntification")
        self.RegistrationButton = QtWidgets.QPushButton(self.Auntification)
        self.RegistrationButton.setGeometry(QtCore.QRect(450, 992, 272, 38))
        self.RegistrationButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RegistrationButton.setStyleSheet("QPushButton{\n"
                                              "border-radius: 1px\n"
                                              "}")
        self.RegistrationButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Зарегистрируйтесь.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RegistrationButton.setIcon(icon1)
        self.RegistrationButton.setIconSize(QtCore.QSize(272, 38))
        self.RegistrationButton.setFlat(True)
        self.RegistrationButton.setObjectName("RegistrationButton")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.Auntification)
        self.stackedWidget_2.setGeometry(QtCore.QRect(786, 744, 352, 24))
        self.stackedWidget_2.setAutoFillBackground(False)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.CurrentLogin = QtWidgets.QWidget()
        self.CurrentLogin.setObjectName("CurrentLogin")
        self.stackedWidget_2.addWidget(self.CurrentLogin)
        self.WrongLogin = QtWidgets.QWidget()
        self.WrongLogin.setObjectName("WrongLogin")
        self.WrongLoginText = QtWidgets.QLabel(self.WrongLogin)
        self.WrongLoginText.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.WrongLoginText.setText("")
        self.WrongLoginText.setPixmap(QtGui.QPixmap("images/Wrong.svg"))
        self.WrongLoginText.setObjectName("WrongLoginText")
        self.stackedWidget_2.addWidget(self.WrongLogin)
        self.background.raise_()
        self.frameOfLogo.raise_()
        self.OutorIn.raise_()
        self.Question.raise_()
        self.Login.raise_()
        self.Logo.raise_()
        self.Letter.raise_()
        self.Password.raise_()
        self.TextUnderLogo.raise_()
        self.Lock.raise_()
        self.ExitAuntification.raise_()
        self.RegistrationButton.raise_()
        self.stackedWidget_2.raise_()
        self.stackedWidget.addWidget(self.Auntification)
        self.Menu = QtWidgets.QWidget()
        self.Menu.setObjectName("Menu")
        self.Underline = QtWidgets.QLabel(self.Menu)
        self.Underline.setGeometry(QtCore.QRect(0, 980, 1920, 100))
        self.Underline.setText("")
        self.Underline.setPixmap(QtGui.QPixmap("images/Underline.svg"))
        self.Underline.setObjectName("Underline")
        self.smallLogo = QtWidgets.QLabel(self.Menu)
        self.smallLogo.setGeometry(QtCore.QRect(1570, 100, 150, 150))
        self.smallLogo.setText("")
        self.smallLogo.setPixmap(QtGui.QPixmap("images/smallLogo.png"))
        self.smallLogo.setObjectName("smallLogo")
        self.Clock = QtWidgets.QLabel(self.Menu)
        self.Clock.setGeometry(QtCore.QRect(200, 200, 75, 75))
        self.Clock.setText("")
        self.Clock.setPixmap(QtGui.QPixmap("images/Clock.png"))
        self.Clock.setObjectName("Clock")
        self.TimeOfUsing = QtWidgets.QLabel(self.Menu)
        self.TimeOfUsing.setGeometry(QtCore.QRect(310, 200, 229, 38))
        self.TimeOfUsing.setText("")
        self.TimeOfUsing.setPixmap(QtGui.QPixmap("images/Время работы.svg"))
        self.TimeOfUsing.setObjectName("TimeOfUsing")
        self.Parking_btn = QtWidgets.QPushButton(self.Menu)
        self.Parking_btn.setGeometry(QtCore.QRect(200, 415, 250, 250))
        self.Parking_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Parking_btn.setStyleSheet("QPushButton{\n"
                                       "position: absolute;\n"
                                       "width: 250px;\n"
                                       "height: 250px;\n"
                                       "left: calc(50% - 250px/2 - 635px);\n"
                                       "top: 415px;\n"
                                       "border-radius: 30px;\n"
                                       "background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.721348, y2:0.734, "
                                       "stop:0 rgba(74, 137, 211, 0.9), stop:1 rgba(18, 27, 116, 0.9));\n "
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.721348, y2:0.734, "
                                       "stop:0 rgba(79, 85, 142, 255), stop:1 rgba(67, 58, 166, 255))\n "
                                       "}")
        self.Parking_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/Парковка.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Parking_btn.setIcon(icon2)
        self.Parking_btn.setIconSize(QtCore.QSize(250, 250))
        self.Parking_btn.setObjectName("Parking_btn")
        self.Data_btn = QtWidgets.QPushButton(self.Menu)
        self.Data_btn.setGeometry(QtCore.QRect(1152, 415, 250, 250))
        self.Data_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Data_btn.setStyleSheet("QPushButton{\n"
                                    "position: absolute;\n"
                                    "width: 250px;\n"
                                    "height: 250px;\n"
                                    "left: calc(50% - 250px/2 - 635px);\n"
                                    "top: 415px;\n"
                                    "border-radius: 30px;\n"
                                    "background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.721348, y2:0.734, "
                                    "stop:0 rgba(74, 137, 211, 0.9), stop:1 rgba(18, 27, 116, 0.9));\n "
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.721348, y2:0.734, "
                                    "stop:0 rgba(79, 85, 142, 255), stop:1 rgba(67, 58, 166, 255))\n "
                                    "}")
        self.Data_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Data_btn.setIcon(icon3)
        self.Data_btn.setIconSize(QtCore.QSize(250, 250))
        self.Data_btn.setObjectName("Data_btn")
        self.Number_btn = QtWidgets.QPushButton(self.Menu)
        self.Number_btn.setGeometry(QtCore.QRect(834, 415, 250, 250))
        self.Number_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Number_btn.setStyleSheet("QPushButton{\n"
                                      "position: absolute;\n"
                                      "width: 250px;\n"
                                      "height: 250px;\n"
                                      "left: calc(50% - 250px/2 - 635px);\n"
                                      "top: 415px;\n"
                                      "border-radius: 30px;\n"
                                      "background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.721348, y2:0.734, "
                                      "stop:0 rgba(74, 137, 211, 0.9), stop:1 rgba(18, 27, 116, 0.9));\n "
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.721348, y2:0.734, "
                                      "stop:0 rgba(79, 85, 142, 255), stop:1 rgba(67, 58, 166, 255))\n "
                                      "}\n"
                                      "")
        self.Number_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/Group 8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Number_btn.setIcon(icon4)
        self.Number_btn.setIconSize(QtCore.QSize(250, 250))
        self.Number_btn.setObjectName("Number_btn")
        self.FAQ_btn = QtWidgets.QPushButton(self.Menu)
        self.FAQ_btn.setGeometry(QtCore.QRect(1470, 415, 250, 250))
        self.FAQ_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FAQ_btn.setStyleSheet("QPushButton{\n"
                                   "position: absolute;\n"
                                   "width: 250px;\n"
                                   "height: 250px;\n"
                                   "left: calc(50% - 250px/2 - 635px);\n"
                                   "top: 415px;\n"
                                   "border-radius: 30px;\n"
                                   "background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.721348, y2:0.734, "
                                   "stop:0 rgba(74, 137, 211, 0.9), stop:1 rgba(18, 27, 116, 0.9));\n "
                                   "}\n"
                                   "QPushButton:pressed{\n"
                                   "background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.721348, y2:0.734, "
                                   "stop:0 rgba(79, 85, 142, 255), stop:1 rgba(67, 58, 166, 255))\n "
                                   "}")
        self.FAQ_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/FAQ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FAQ_btn.setIcon(icon5)
        self.FAQ_btn.setIconSize(QtCore.QSize(250, 250))
        self.FAQ_btn.setObjectName("FAQ_btn")
        self.Camera_btn = QtWidgets.QPushButton(self.Menu)
        self.Camera_btn.setGeometry(QtCore.QRect(517, 415, 250, 250))
        self.Camera_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Camera_btn.setStyleSheet("QPushButton{\n"
                                      "position: absolute;\n"
                                      "width: 250px;\n"
                                      "height: 250px;\n"
                                      "left: calc(50% - 250px/2 - 635px);\n"
                                      "top: 415px;\n"
                                      "border-radius: 30px;\n"
                                      "background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.721348, y2:0.734, "
                                      "stop:0 rgba(74, 137, 211, 0.9), stop:1 rgba(18, 27, 116, 0.9));\n "
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.721348, y2:0.734, "
                                      "stop:0 rgba(79, 85, 142, 255), stop:1 rgba(67, 58, 166, 255))\n "
                                      "}")
        self.Camera_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/Group 7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Camera_btn.setIcon(icon6)
        self.Camera_btn.setIconSize(QtCore.QSize(250, 250))
        self.Camera_btn.setObjectName("Camera_btn")
        self.User = QtWidgets.QLineEdit(self.Menu)
        self.User.setGeometry(QtCore.QRect(200, 100, 421, 38))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.User.setFont(font)
        self.User.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.User.setStyleSheet("QLineEdit{\n"
                                "background:rgb(240, 240, 240)\n"
                                "}")
        self.User.setFrame(False)
        self.User.setReadOnly(True)
        self.User.setObjectName("User")
        self.ExitMenu = QtWidgets.QPushButton(self.Menu)
        self.ExitMenu.setGeometry(QtCore.QRect(1860, 20, 40, 40))
        self.ExitMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitMenu.setStyleSheet("QPushButton{\n"
                                    "border-radius: 1px\n"
                                    "}")
        self.ExitMenu.setText("")
        self.ExitMenu.setIcon(icon)
        self.ExitMenu.setIconSize(QtCore.QSize(40, 40))
        self.ExitMenu.setFlat(True)
        self.ExitMenu.setObjectName("ExitMenu")
        self.stackedWidget.addWidget(self.Menu)
        self.FAQ = QtWidgets.QWidget()
        self.FAQ.setObjectName("FAQ")
        self.Background = QtWidgets.QLabel(self.FAQ)
        self.Background.setEnabled(True)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("images/FAQ.svg"))
        self.Background.setScaledContents(False)
        self.Background.setWordWrap(False)
        self.Background.setOpenExternalLinks(False)
        self.Background.setObjectName("Background")
        self.toMenuFromFAQ = QtWidgets.QPushButton(self.FAQ)
        self.toMenuFromFAQ.setEnabled(True)
        self.toMenuFromFAQ.setGeometry(QtCore.QRect(200, 100, 50, 50))
        self.toMenuFromFAQ.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toMenuFromFAQ.setMouseTracking(False)
        self.toMenuFromFAQ.setTabletTracking(False)
        self.toMenuFromFAQ.setAcceptDrops(False)
        self.toMenuFromFAQ.setAutoFillBackground(False)
        self.toMenuFromFAQ.setStyleSheet("QPushButton{\n"
                                         "position: absolute;\n"
                                         "width: 50px;\n"
                                         "height: 50px;\n"
                                         "left: 200px;\n"
                                         "top: 100px;\n"
                                         "border-radius: 15px;\n"
                                         "}")
        self.toMenuFromFAQ.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/arrowToMenu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("images/arrowToMenu.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap("images/arrowToMenu.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("images/arrowToMenu.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap("images/arrowToMenu.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("images/arrowToMenu.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap("images/arrowToMenu.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("images/arrowToMenu.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.toMenuFromFAQ.setIcon(icon7)
        self.toMenuFromFAQ.setIconSize(QtCore.QSize(50, 50))
        self.toMenuFromFAQ.setCheckable(False)
        self.toMenuFromFAQ.setChecked(False)
        self.toMenuFromFAQ.setAutoRepeat(False)
        self.toMenuFromFAQ.setAutoExclusive(False)
        self.toMenuFromFAQ.setAutoDefault(False)
        self.toMenuFromFAQ.setFlat(True)
        self.toMenuFromFAQ.setObjectName("toMenuFromFAQ")
        self.smallLogo_2 = QtWidgets.QLabel(self.FAQ)
        self.smallLogo_2.setGeometry(QtCore.QRect(1570, 100, 150, 150))
        self.smallLogo_2.setText("")
        self.smallLogo_2.setPixmap(QtGui.QPixmap("images/smallLogo.png"))
        self.smallLogo_2.setObjectName("smallLogo_2")
        self.help = QtWidgets.QLabel(self.FAQ)
        self.help.setGeometry(QtCore.QRect(200, 200, 193, 53))
        self.help.setText("")
        self.help.setPixmap(QtGui.QPixmap("images/Справка.png"))
        self.help.setObjectName("help")
        self.whiteBack = QtWidgets.QLabel(self.FAQ)
        self.whiteBack.setGeometry(QtCore.QRect(360, 330, 1200, 600))
        self.whiteBack.setText("")
        self.whiteBack.setPixmap(QtGui.QPixmap("images/TextInFAQ.svg"))
        self.whiteBack.setObjectName("whiteBack")
        self.Text = QtWidgets.QLabel(self.FAQ)
        self.Text.setGeometry(QtCore.QRect(820, 380, 279, 76))
        self.Text.setText("")
        self.Text.setPixmap(QtGui.QPixmap("images/Instruction.svg"))
        self.Text.setObjectName("Text")
        self.ExitFAQ = QtWidgets.QPushButton(self.FAQ)
        self.ExitFAQ.setGeometry(QtCore.QRect(1860, 20, 40, 40))
        self.ExitFAQ.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitFAQ.setStyleSheet("QPushButton{\n"
                                   "border-radius: 1px\n"
                                   "}")
        self.ExitFAQ.setText("")
        self.ExitFAQ.setIcon(icon)
        self.ExitFAQ.setIconSize(QtCore.QSize(40, 40))
        self.ExitFAQ.setFlat(True)
        self.ExitFAQ.setObjectName("ExitFAQ")
        self.stackedWidget.addWidget(self.FAQ)
        self.Camera = QtWidgets.QWidget()
        self.Camera.setObjectName("Camera")
        self.toMenuFromCamera = QtWidgets.QPushButton(self.Camera)
        self.toMenuFromCamera.setGeometry(QtCore.QRect(200, 100, 50, 50))
        self.toMenuFromCamera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toMenuFromCamera.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/ToMenu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toMenuFromCamera.setIcon(icon8)
        self.toMenuFromCamera.setIconSize(QtCore.QSize(50, 50))
        self.toMenuFromCamera.setFlat(True)
        self.toMenuFromCamera.setObjectName("toMenuFromCamera")
        self.TextCamera = QtWidgets.QLabel(self.Camera)
        self.TextCamera.setGeometry(QtCore.QRect(200, 200, 173, 53))
        self.TextCamera.setText("")
        self.TextCamera.setPixmap(QtGui.QPixmap("images/Камера.svg"))
        self.TextCamera.setObjectName("TextCamera")
        self.label_2 = QtWidgets.QLabel(self.Camera)
        self.label_2.setGeometry(QtCore.QRect(1570, 100, 150, 150))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/smallLogo.png"))
        self.label_2.setObjectName("label_2")
        self.Cam = QtWidgets.QLabel(self.Camera)
        self.Cam.setGeometry(QtCore.QRect(360, 330, 1200, 600))
        self.Cam.setObjectName("Cam")
        self.ExitCamera = QtWidgets.QPushButton(self.Camera)
        self.ExitCamera.setGeometry(QtCore.QRect(1860, 20, 40, 40))
        self.ExitCamera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitCamera.setStyleSheet("QPushButton{\n"
                                      "border-radius: 1px\n"
                                      "}")
        self.ExitCamera.setText("")
        self.ExitCamera.setIcon(icon)
        self.ExitCamera.setIconSize(QtCore.QSize(40, 40))
        self.ExitCamera.setFlat(True)
        self.ExitCamera.setObjectName("ExitCamera")
        self.stackedWidget.addWidget(self.Camera)
        self.Registration = QtWidgets.QWidget()
        self.Registration.setObjectName("Registration")
        self.BackOfReg = QtWidgets.QLabel(self.Registration)
        self.BackOfReg.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.BackOfReg.setText("")
        self.BackOfReg.setPixmap(QtGui.QPixmap("images/BackReg.svg"))
        self.BackOfReg.setObjectName("BackOfReg")
        self.ToAuntificatoinFromReg = QtWidgets.QPushButton(self.Registration)
        self.ToAuntificatoinFromReg.setGeometry(QtCore.QRect(200, 100, 50, 50))
        self.ToAuntificatoinFromReg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ToAuntificatoinFromReg.setStyleSheet("QPushButton{\n"
                                                  "border-radius: 1px;\n"
                                                  "}")
        self.ToAuntificatoinFromReg.setText("")
        self.ToAuntificatoinFromReg.setIcon(icon8)
        self.ToAuntificatoinFromReg.setIconSize(QtCore.QSize(75, 75))
        self.ToAuntificatoinFromReg.setFlat(True)
        self.ToAuntificatoinFromReg.setObjectName("ToAuntificatoinFromReg")
        self.BackReg2 = QtWidgets.QLabel(self.Registration)
        self.BackReg2.setGeometry(QtCore.QRect(660, 190, 600, 700))
        self.BackReg2.setStyleSheet("QLabel{\n"
                                    "position: absolute;\n"
                                    "width: 600px;\n"
                                    "height: 700px;\n"
                                    "left: calc(50% - 600px/2);\n"
                                    "top: 190px;\n"
                                    "\n"
                                    "background:qlineargradient(spread:pad, x1:0.09, y1:0.085, x2:1, y2:1, "
                                    "stop:0 rgba(226, 235, 255, 255), stop:1 rgba(123, 119, 166, 255));\n "
                                    "border-radius: 30px;\n"
                                    "}")
        self.BackReg2.setText("")
        self.BackReg2.setScaledContents(False)
        self.BackReg2.setObjectName("BackReg2")
        self.RegistrationRus = QtWidgets.QLabel(self.Registration)
        self.RegistrationRus.setGeometry(QtCore.QRect(820, 234, 279, 56))
        self.RegistrationRus.setText("")
        self.RegistrationRus.setPixmap(QtGui.QPixmap("images/RegistrationRus.svg"))
        self.RegistrationRus.setObjectName("RegistrationRus")
        self.UserIMG = QtWidgets.QLabel(self.Registration)
        self.UserIMG.setGeometry(QtCore.QRect(755, 355, 45, 45))
        self.UserIMG.setText("")
        self.UserIMG.setPixmap(QtGui.QPixmap("images/UserIMG.png"))
        self.UserIMG.setObjectName("UserIMG")
        self.UsernameEntrer = QtWidgets.QLineEdit(self.Registration)
        self.UsernameEntrer.setGeometry(QtCore.QRect(735, 340, 450, 75))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.UsernameEntrer.setFont(font)
        self.UsernameEntrer.setAcceptDrops(True)
        self.UsernameEntrer.setToolTipDuration(3)
        self.UsernameEntrer.setAutoFillBackground(False)
        self.UsernameEntrer.setStyleSheet("QLineEdit {\n"
                                          "position: absolute;\n"
                                          "width: 450px;\n"
                                          "height: 75px;\n"
                                          "left: 735px;\n"
                                          "top: 550px;\n"
                                          "padding-left: 80px;\n"
                                          "padding-right: 20px;\n"
                                          "\n"
                                          "background: #FFFFFF;\n"
                                          "border: 1px solid #C4C4C4;\n"
                                          "box-sizing: border-box;\n"
                                          "border-radius: 10px;\n"
                                          "}")
        self.UsernameEntrer.setText("")
        self.UsernameEntrer.setCursorPosition(0)
        self.UsernameEntrer.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.UsernameEntrer.setObjectName("UsernameEntrer")
        self.LoginEnter = QtWidgets.QLineEdit(self.Registration)
        self.LoginEnter.setGeometry(QtCore.QRect(735, 510, 450, 75))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.LoginEnter.setFont(font)
        self.LoginEnter.setAcceptDrops(True)
        self.LoginEnter.setToolTipDuration(3)
        self.LoginEnter.setAutoFillBackground(False)
        self.LoginEnter.setStyleSheet("QLineEdit {\n"
                                      "position: absolute;\n"
                                      "width: 450px;\n"
                                      "height: 75px;\n"
                                      "left: 735px;\n"
                                      "top: 550px;\n"
                                      "padding-left: 80px;\n"
                                      "padding-right: 20px;\n"
                                      "\n"
                                      "background: #FFFFFF;\n"
                                      "border: 1px solid #C4C4C4;\n"
                                      "box-sizing: border-box;\n"
                                      "border-radius: 10px;\n"
                                      "}")
        self.LoginEnter.setText("")
        self.LoginEnter.setCursorPosition(0)
        self.LoginEnter.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.LoginEnter.setObjectName("LoginEnter")
        self.PasswordEnter = QtWidgets.QLineEdit(self.Registration)
        self.PasswordEnter.setGeometry(QtCore.QRect(735, 680, 450, 75))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.PasswordEnter.setFont(font)
        self.PasswordEnter.setAcceptDrops(True)
        self.PasswordEnter.setToolTipDuration(3)
        self.PasswordEnter.setAutoFillBackground(False)
        self.PasswordEnter.setStyleSheet("QLineEdit {\n"
                                         "position: absolute;\n"
                                         "width: 450px;\n"
                                         "height: 75px;\n"
                                         "left: 735px;\n"
                                         "top: 550px;\n"
                                         "padding-left: 80px;\n"
                                         "padding-right: 20px;\n"
                                         "\n"
                                         "background: #FFFFFF;\n"
                                         "border: 1px solid #C4C4C4;\n"
                                         "box-sizing: border-box;\n"
                                         "border-radius: 10px;\n"
                                         "}")
        self.PasswordEnter.setText("")
        self.PasswordEnter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordEnter.setCursorPosition(0)
        self.PasswordEnter.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.PasswordEnter.setObjectName("PasswordEnter")
        self.Letter_2 = QtWidgets.QLabel(self.Registration)
        self.Letter_2.setGeometry(QtCore.QRect(760, 525, 40, 40))
        self.Letter_2.setStyleSheet("")
        self.Letter_2.setText("")
        self.Letter_2.setPixmap(QtGui.QPixmap("images/image 7.png"))
        self.Letter_2.setObjectName("Letter_2")
        self.Lock_2 = QtWidgets.QLabel(self.Registration)
        self.Lock_2.setGeometry(QtCore.QRect(760, 695, 40, 40))
        self.Lock_2.setStyleSheet("")
        self.Lock_2.setText("")
        self.Lock_2.setPixmap(QtGui.QPixmap("images/image 5.png"))
        self.Lock_2.setObjectName("Lock_2")
        self.Logo_2 = QtWidgets.QLabel(self.Registration)
        self.Logo_2.setGeometry(QtCore.QRect(1570, 50, 250, 250))
        self.Logo_2.setText("")
        self.Logo_2.setPixmap(QtGui.QPixmap("images/Logo.png"))
        self.Logo_2.setObjectName("Logo_2")
        self.RegBtn = QtWidgets.QPushButton(self.Registration)
        self.RegBtn.setGeometry(QtCore.QRect(710, 840, 500, 100))
        self.RegBtn.setStyleSheet("QPushButton {\n"
                                  "position: absolute;\n"
                                  "width: 350px;\n"
                                  "height: 100px;\n"
                                  "left: 785px;\n"
                                  "top: 800px;\n"
                                  "\n"
                                  "position: absolute;\n"
                                  "width: 136px;\n"
                                  "height: 55px;\n"
                                  "left: 892px;\n"
                                  "top: 823px;\n"
                                  "\n"
                                  "font-family: \'SF Pro Display\';\n"
                                  "font-style: italic;\n"
                                  "font-weight: 600;\n"
                                  "font-size: 46px;\n"
                                  "line-height: 55px;\n"
                                  "/* identical to box height */\n"
                                  "\n"
                                  "display: flex;\n"
                                  "align-items: center;\n"
                                  "text-align: center;\n"
                                  "letter-spacing: 0.03em;\n"
                                  "\n"
                                  "color: #FFFFFF;\n"
                                  "\n"
                                  "background:qlineargradient(spread:pad, x1:0.169, y1:0.0180455, x2:0.791, y2:0.836, "
                                  "stop:0 rgba(105, 246, 255, 255), stop:1 rgba(67, 58, 166, 255));\n "
                                  "border: 1px solid #C4C4C4;\n"
                                  "box-sizing: border-box;\n"
                                  "border-radius: 25px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed{\n"
                                  "background-color:qlineargradient(spread:pad, x1:1, y1:0.478, x2:0, y2:0.466, "
                                  "stop:0 rgba(67, 58, 166, 255), stop:1 rgba(67, 58, 166, 255)); \n "
                                  "}")
        self.RegBtn.setFlat(False)
        self.RegBtn.setObjectName("RegBtn")
        self.ExitRegistration = QtWidgets.QPushButton(self.Registration)
        self.ExitRegistration.setGeometry(QtCore.QRect(1860, 20, 40, 40))
        self.ExitRegistration.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitRegistration.setStyleSheet("QPushButton{\n"
                                            "border-radius: 1px\n"
                                            "}")
        self.ExitRegistration.setText("")
        self.ExitRegistration.setIcon(icon)
        self.ExitRegistration.setIconSize(QtCore.QSize(40, 40))
        self.ExitRegistration.setFlat(True)
        self.ExitRegistration.setObjectName("ExitRegistration")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.Registration)
        self.stackedWidget_3.setGeometry(QtCore.QRect(755, 780, 411, 41))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.CurrentReg = QtWidgets.QWidget()
        self.CurrentReg.setObjectName("CurrentReg")
        self.stackedWidget_3.addWidget(self.CurrentReg)
        self.WrongReg = QtWidgets.QWidget()
        self.WrongReg.setObjectName("WrongReg")
        self.ThisUserWrong = QtWidgets.QLineEdit(self.WrongReg)
        self.ThisUserWrong.setGeometry(QtCore.QRect(0, 10, 411, 22))
        self.ThisUserWrong.setStyleSheet("QLineEdit{\n"
                                         "position: absolute;\n"
                                         "width: 352px;\n"
                                         "height: 24px;\n"
                                         "left: 786px;\n"
                                         "top: 744px;\n"
                                         "\n"
                                         "font-family: \'SF Pro Display\';\n"
                                         "font-style: italic;\n"
                                         "font-weight: 300;\n"
                                         "font-size: 20px;\n"
                                         "line-height: 24px;\n"
                                         "/* identical to box height */\n"
                                         "\n"
                                         "display: flex;\n"
                                         "align-items: center;\n"
                                         "padding-left: 15px;\n"
                                         "color: #FF0000;\n"
                                         "background:qradialgradient(spread:pad, cx:0.6, cy:0.829545, radius:0.5, "
                                         "fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 0), stop:0.35 rgba(255, 188, "
                                         "188, 0), stop:0.517413 rgba(252, 128, 128, 0), stop:0.721393 rgba(255, 132, "
                                         "132, 0), stop:0.865672 rgba(255, 162, 162, 0), stop:1 rgba(255, 255, 255, "
                                         "0));\n "
                                         "}")
        self.ThisUserWrong.setFrame(False)
        self.ThisUserWrong.setReadOnly(True)
        self.ThisUserWrong.setObjectName("ThisUserWrong")
        self.stackedWidget_3.addWidget(self.WrongReg)
        self.BackOfReg.raise_()
        self.ToAuntificatoinFromReg.raise_()
        self.BackReg2.raise_()
        self.RegistrationRus.raise_()
        self.UsernameEntrer.raise_()
        self.UserIMG.raise_()
        self.LoginEnter.raise_()
        self.PasswordEnter.raise_()
        self.Letter_2.raise_()
        self.Lock_2.raise_()
        self.Logo_2.raise_()
        self.RegBtn.raise_()
        self.ExitRegistration.raise_()
        self.stackedWidget_3.raise_()
        self.stackedWidget.addWidget(self.Registration)
        rtf_network.setCentralWidget(self.centralwidget)

        self.retranslate_ui(rtf_network)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(rtf_network)

    def retranslate_ui(self, rtf_network):
        _translate = QtCore.QCoreApplication.translate
        rtf_network.setWindowTitle(_translate("RTFNetwork", "RTFNetwork"))
        self.OutorIn.setText(_translate("RTFNetwork", "Войти"))
        self.Login.setPlaceholderText(_translate("RTFNetwork", "Логин"))
        self.Password.setPlaceholderText(_translate("RTFNetwork", "Пароль"))
        self.User.setText(_translate("RTFNetwork", "Довольный пользователь"))
        self.UsernameEntrer.setPlaceholderText(_translate("RTFNetwork", "Имя Фамилия"))
        self.LoginEnter.setPlaceholderText(_translate("RTFNetwork", "Логин"))
        self.PasswordEnter.setPlaceholderText(_translate("RTFNetwork", 'Пароль'))
        self.RegBtn.setText(_translate("RTFNetwork", "Зарегистрироваться"))
        self.Cam.setText(_translate("RTFNetwork", "TextLabel"))
        self.ThisUserWrong.setText(_translate("RTFNetwork", "Такой пользователь уже зарегистрирован!"))


def md5sum(value):
    return hashlib.md5(value.encode()).hexdigest()


