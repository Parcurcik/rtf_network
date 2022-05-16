import sys
import sqlite3
import time

from sqlite3 import Cursor, Connection

import cv2

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap

from design import *


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = UiRTFNetwork()
        self.main_win.showFullScreen()
        self.ui.setup_ui(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Auntification)
        self.ui.OutorIn.clicked.connect(self.log_in)
        self.ui.toMenuFromFAQ.clicked.connect(self.show_main)
        self.ui.toMenuFromCamera.clicked.connect(self.show_main)
        self.ui.FAQ_btn.clicked.connect(self.show_faq)
        self.ui.Camera_btn.clicked.connect(self.show_camera)
        self.ui.ExitFAQ.clicked.connect(QApplication.instance().quit)
        self.ui.ExitAuntification.clicked.connect(QApplication.instance().quit)
        self.ui.ExitMenu.clicked.connect(QApplication.instance().quit)
        self.ui.ExitCamera.clicked.connect(QApplication.instance().quit)
        self.ui.ExitRegistration.clicked.connect(QApplication.instance().quit)
        self.ui.RegistrationButton.clicked.connect(self.show_registration)
        self.ui.ToAuntificatoinFromReg.clicked.connect(self.show_auntification)
        self.ui.RegBtn.clicked.connect(self.registration)
        self.timer = QTimer()  # Таймер для камеры
        self.timer.timeout.connect(self.camera_on)  # Подключаем камеру
        self.ui.Camera_btn.clicked.connect(self.control_timer)  # Визуализация включение камеры

    def camera_on(self):
        ret, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        img = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.ui.Cam.setPixmap(QPixmap.fromImage(img))
        self.ui.Cam.setScaledContents(True)

    def control_timer(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            self.timer.start(0)

    def network(self):
        #ret, frame = video_capture.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('cascade/haarcascade_russian_plate_number.xml')
        plaques = face_cascade.detectMultiScale(gray, 1.3, 5)
        for i, (x, y, w, h) in enumerate(plaques):
            roi_color = frame[y:y + h, x:x + w]
            r = 400.0 / roi_color.shape[1]
            dim = (400, int(roi_color.shape[0] * r))
            resized = cv2.resize(roi_color, dim, interpolation=cv2.INTER_AREA)
            w_resized = resized.shape[0]
            h_resized = resized.shape[1]
            frame[100:100 + w_resized, 100:100 + h_resized] = resized

    def play(self):
        self.media.play()

    def show_main(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Menu)

    def show(self):
        self.main_win.show()

    def show_faq(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.FAQ)

    def show_camera(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Camera)

    def show_registration(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Registration)

    def show_auntification(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Auntification)

    def registration(self):
        login = self.ui.LoginEnter.text()
        password = self.ui.PasswordEnter.text()
        username = self.ui.UsernameEntrer.text()

        try:
            data_base = sqlite3.connect("database.db")
            cursor = data_base.cursor()

            data_base.create_function("MD5", 1, md5sum)

            cursor.execute("SELECT login FROM users WHERE login = ?", [login])
            if cursor.fetchone() is None:
                values = [login, md5sum(password), username]

                cursor.execute("INSERT INTO users(login, password,username) VALUES(?,?,?)", values)
                data_base.commit()
                time.sleep(1)
                self.ui.stackedWidget.setCurrentWidget(self.ui.Auntification)
            else:
                self.ui.stackedWidget_3.setCurrentWidget(self.ui.WrongReg)
        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            data_base.close()

    def log_in(self):
        global cursor, db
        login = self.ui.Login.text()
        password = self.ui.Password.text()

        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()
            cursor.execute("SELECT login FROM  users WHERE login = ?", [login])
            if cursor.fetchone() is None:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.WrongLogin)
            else:
                cursor.execute("SELECT password FROM users WHERE login = ? AND password = ?", [login, md5sum(password)])
                if cursor.fetchone() is None:
                    self.ui.stackedWidget_2.setCurrentWidget(self.ui.WrongLogin)
                else:
                    cursor.execute("SELECT username FROM users WHERE login = ?", [login])
                    time.sleep(0.2)
                    self.ui.stackedWidget.setCurrentWidget(self.ui.Menu)
                    self.ui.User.setText(f'{cursor.fetchone()[0]}')
        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
