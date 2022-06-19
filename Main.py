import sys
import sqlite3
import time
import os

from sqlite3 import Cursor, Connection

import cv2
import math

from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

import tensorflow as tf
from matplotlib import pyplot as plt
import itertools
from skimage.color import rgb2gray
from skimage.feature import canny

import numpy as np

from design import *


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_RTFNetwork()
        self.main_win.showFullScreen()
        # Login
        self.ui.setup_ui(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Auntification)
        self.ui.OutorIn.clicked.connect(self.log_in)
        # MainMenu
        self.ui.toMenuFromParking.clicked.connect(self.show_main)
        self.ui.toMenuFromFAQ.clicked.connect(self.show_main)
        self.ui.toMenuFromCamera.clicked.connect(self.show_main)
        self.ui.toMenuFromNumbers.clicked.connect(self.show_main)
        # Buttons to sections
        self.ui.FAQ_btn.clicked.connect(self.show_faq)
        self.ui.Camera_btn.clicked.connect(self.show_camera)
        self.ui.Parking_btn.clicked.connect(self.show_parking)
        self.ui.Number_btn.clicked.connect(self.show_numbers)
        # Buttons to exit
        self.ui.ExitFAQ.clicked.connect(QApplication.instance().quit)
        self.ui.ExitParking.clicked.connect(QApplication.instance().quit)
        self.ui.ExitNumbers.clicked.connect(QApplication.instance().quit)
        self.ui.ExitAuntification.clicked.connect(QApplication.instance().quit)
        self.ui.ExitMenu.clicked.connect(QApplication.instance().quit)
        self.ui.ExitCamera.clicked.connect(QApplication.instance().quit)
        self.ui.ExitRegistration.clicked.connect(QApplication.instance().quit)
        # Registration
        self.ui.ToAuntificatoinFromReg.clicked.connect(self.show_auntification)
        self.ui.RegBtn.clicked.connect(self.registration)
        # Camera settings
        self.PredictNumber = PredictNumber()
        self.PredictNumber.ImageUpdate.connect(self.image_update_slot)
        self.ui.Camera_btn.clicked.connect(self.PredictNumber.start)
        self.ui.Camera_btn.clicked.connect(self.cars_work)
        # Timer
        self.temp = 0
        self.ui.OutorIn.clicked.connect(self.start_timer)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.display_time)
        # Cars
        self.ui.Parking_btn.clicked.connect(self.replace_statistic)

        # Number
        self.ui.Number_btn.clicked.connect(self.clean_number)
        self.ui.searchButton.clicked.connect(self.search_number)

        # Cache

    def clean_number(self):
        self.ui.historyDate_2.setText("")
        self.ui.SWNumberCar.setCurrentWidget(self.ui.NaNpage)

    def start_timer(self):
        self.timer.start()

    def display_time(self):
        f_temp = datetime.utcfromtimestamp(self.temp).strftime("%H:%M:%S")
        self.ui.TimerMenu.setText(f_temp)
        self.temp += 1

    def image_update_slot(self, image):
        self.ui.Cam.setPixmap(QPixmap.fromImage(image))
        self.ui.Cam.setScaledContents(True)

    def play(self):
        self.media.play()

    def search_number(self):
        if self.ui.historyDate_2.text() in Cars.cars_arr:
            self.ui.SWNumberCar.setCurrentWidget(self.ui.CurrentPage)
        else:
            self.ui.SWNumberCar.setCurrentWidget(self.ui.WrongPage)

    def show_main(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Menu)

    def show(self):
        self.main_win.show()

    def show_faq(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.FAQ)

    def show_numbers(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Numbers)

    def show_parking(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Parking)

    def show_camera(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Camera)

    def show_cache(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Cache)

    def show_registration(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Registration)

    def show_auntification(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Auntification)

    def registration(self):
        login = self.ui.LoginEnter.text()
        password = self.ui.PasswordEnter.text()
        username = self.ui.UsernameEntrer.text()

        try:
            data_base = sqlite3.connect("dataBases/database.db")
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
            db = sqlite3.connect("DataBases/database.db")
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

    def replace_statistic(self):
        self.ui.countOfCarsInPark.setText(str(Cars.cars_count_in_park))
        self.ui.countOfFreePark.setText(str(Cars.cars_count_out_park - Cars.cars_count_in_park))

    def cars_work(self, number):
        try:
            db = sqlite3.connect("dataBases/NUM_DB.db")
            cursor = db.cursor()

            cursor.execute("SELECT number FROM num_db WHERE number = ?", [number])
            if cursor.fetchone() is None:
                self.ui.NumberWidget.setCurrentWidget(self.ui.WrongNumber)
            else:
                self.ui.NumberWidget.setCurrentWidget(self.ui.RightNumber)
                if number not in Cars.cars_arr:
                    Cars.cars_arr.insert(Cars.increment, number)
                    Cars.increment += 1
                    Cars.cars_count_in_park += 1
        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            db.close()


class Cars:
    park_count = 100
    cars_arr = [0] * park_count
    cars_count_out_park = park_count
    cars_count_in_park = park_count - cars_count_out_park

    increment = 0


class PredictNumber(QThread):
    ImageUpdate = pyqtSignal(QImage)
    count_iterations = 1

    def run(self):
        number = ""
        self.ThreadActive = True
        capture = cv2.VideoCapture('testVideo/3.mp4')
        a = "Нет номера"
        main_win.ui.NumberText.setText("Нет номера")
        while self.ThreadActive:
            face_cascade = cv2.CascadeClassifier('networks/cascadeToNumberPlates.xml')
            ret, frame = capture.read()
            if ret:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                with_cascade = face_cascade.detectMultiScale(image, 1.3, 7)
                for i, (x, y, w, h) in enumerate(with_cascade):
                    roi_color = image[y:y + h, x:x + w]
                    r = 300.0 / roi_color.shape[1]
                    dim = (400, int(roi_color.shape[0] * r))
                    resized = cv2.resize(roi_color, dim, interpolation=cv2.INTER_AREA)
                    w_resized = resized.shape[0]
                    h_resized = resized.shape[1]
                    image[980:980 + w_resized, 1520:1520 + h_resized] = resized
                    letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'E', 'H', 'K', 'M', 'O',
                               'P', 'T', 'X', 'Y']

                    def decode_batch(out):
                        ret = []
                        for j in range(out.shape[0]):
                            out_best = list(np.argmax(out[j, 2:], 1))
                            out_best = [k for k, g in itertools.groupby(out_best)]
                            outstr = ''
                            for c in out_best:
                                if c < len(letters):
                                    outstr += letters[c]
                            ret.append(outstr)
                        return ret

                    paths = "networks/tesseractNumbers.tflite"
                    interpreter = tf.lite.Interpreter(model_path=paths)
                    interpreter.allocate_tensors()
                    # Get input and output tensors.
                    input_details = interpreter.get_input_details()
                    output_details = interpreter.get_output_details()
                    img = resized
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    img = cv2.resize(img, (128, 64))
                    img = img.astype(np.float32)
                    img /= 255
                    img1 = img.T
                    img1.shape
                    X_data1 = np.float32(img1.reshape(1, 128, 64, 1))
                    interpreter.set_tensor(input_details[0]['index'], X_data1)
                    interpreter.invoke()
                    net_out_value = interpreter.get_tensor(output_details[0]['index'])
                    pred_texts = decode_batch(net_out_value)
                    if a != pred_texts:
                        a = pred_texts
                        a = " ".join(a)
                convert_to_qt_format = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
                self.ImageUpdate.emit(convert_to_qt_format)
                number = str(a)
                PredictNumber.count_iterations += 1
                if PredictNumber.count_iterations % 4 == 0:
                    main_win.ui.NumberText.setText(number)
                    MainWindow.cars_work(main_win, number)
                self.msleep(10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
