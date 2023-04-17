#!/usr/bin/python3

import sys
import os
import numpy as np
from pgwidget import PGWidget
from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.QtCore import (Qt, QObject)
from PyQt5.QtGui import QBrush, QPainter, QIcon, QFont
from PyQt5.QtWidgets import (
    QWidget, QApplication, QMainWindow, QGraphicsScene)
import math
import pyqtgraph as pg
from ui_kojima_steering import Ui_MainWindow
from color_maps import *

# this may or may not help with high DPI screen
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
version = list(map(int, QT_VERSION_STR.split('.')))

if version[1] >= 14:
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
if hasattr(Qt, "AA_EnableHighDpiScaling"):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, "AA_UseHighDpiPixmaps"):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
pg.setConfigOptions(antialias=True)
from color_maps import *
palette = ("#101418", "#c00000", "#c000c0", "#c06000",
           "#00c000", "#0072c3", "#6fdc8c", "#d2a106")

class AppWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Kojima Steering Correction')
        #icon: https://commons.wikimedia.org/wiki/File:Icono_para_transporte_por_carretera.svg
        self.setWindowIcon(QtGui.QIcon('steering-wheel.png'))
        self.resize(1000, 900)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.centre_on_screen()
        # connect all the parameter elements to the same recalculation
        self.ui.sb_kp.valueChanged.connect(self.recalculate)
        self.ui.sb_kd.valueChanged.connect(self.recalculate)
        self.ui.sb_k1.valueChanged.connect(self.recalculate)
        self.ui.sb_k2.valueChanged.connect(self.recalculate)
        self.ui.sb_acc.valueChanged.connect(self.recalculate)
        self.ui.sb_theta_init.valueChanged.connect(self.recalculate)
        self.ui.sb_y_init.valueChanged.connect(self.recalculate)
        self.ui.sb_omega_init.valueChanged.connect(self.recalculate)
        self.ui.sb_speed_init.valueChanged.connect(self.recalculate)
        self.ui.sb_alpha_max.valueChanged.connect(self.recalculate)
        self.ui.sb_v_max.valueChanged.connect(self.recalculate)
        # and connect the parameter reset
        self.ui.btn_reset.clicked.connect(self.reset)

        # create empty plots here so there are references to populate later
        colors = color_map_10a
        self.y_plot = self.ui.pg_widget.pw_y.plot(pen=pg.mkPen(colors[1], width=2))
        self.speed_plot = self.ui.pg_widget.pw_speed.plot(pen=pg.mkPen(colors[2], width=2))
        self.theta_plot = self.ui.pg_widget.pw_theta.plot(pen=pg.mkPen(colors[3], width=2))
        self.omega_plot = self.ui.pg_widget.pw_omega.plot(pen=pg.mkPen(colors[4], width=2))
        self.alpha_plot = self.ui.pg_widget.pw_alpha.plot(pen=pg.mkPen(colors[5], width=2))

        self.time_data = []
        self.speed_data = []
        self.alpha_data = []
        self.omega_data = []
        self.theta_data = []
        self.x_data = []
        self.y_data = []
        self.recalculate()

    def centre_on_screen(self):
        geometry = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        center_point = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        geometry.moveCenter(center_point)
        self.move(geometry.topLeft())

    def reset(self):
        self.ui.sb_kp.setValue(12000)
        self.ui.sb_kd.setValue(200)
        self.ui.sb_k1.setValue(0.200)
        self.ui.sb_k2.setValue(0.020)
        self.ui.sb_y_init.setValue(10)
        self.ui.sb_theta_init.setValue(0)
        self.ui.sb_omega_init.setValue(0.0)
        self.ui.sb_speed_init.setValue(1.0)
        self.ui.sb_acc.setValue(9.8)
        self.ui.sb_v_max.setValue(6.0)
        self.ui.sb_alpha_max.setValue(15000)
        pass



    def recalculate(self):
        dt = 0.001
        time = 0
        acc = self.ui.sb_acc.value()
        alpha_max = math.radians(self.ui.sb_alpha_max.value())
        speed = self.ui.sb_speed_init.value()
        x = 0.0
        alpha = math.radians(0.0)
        omega = math.radians(self.ui.sb_omega_init.value())
        theta = math.radians(self.ui.sb_theta_init.value())
        k1 = self.ui.sb_k1.value()
        k2 = self.ui.sb_k2.value()
        kp = self.ui.sb_kp.value()
        kd = self.ui.sb_kd.value()
        y = self.ui.sb_y_init.value()/1000.0
        S = k1*y+k2*theta
        self.time_data = [time]
        self.speed_data = [speed]
        self.x_data = [x]
        self.y_data = [y]
        self.theta_data = [theta]
        self.omega_data = [omega]
        self.alpha_data = [alpha]
        while x < 1.8:
            time += dt
            speed += dt * acc
            speed = min(speed, self.ui.sb_v_max.value())
            # speed = self.ui.sb_speed_init.value()

            # limit the value of alpha that is used in the calculation
            alpha = max(min(alpha,alpha_max),-alpha_max)
            omega += dt * alpha
            theta += dt * omega
            x += dt * speed * math.cos(theta)
            y += dt * speed * math.sin(theta)
            S = k1 * y + k2 * theta
            self.time_data.append(time)
            self.y_data.append(1000*y)
            self.speed_data.append(speed)
            self.x_data.append(x)
            self.theta_data.append(math.degrees(theta))
            self.omega_data.append(math.degrees(omega))
            self.alpha_data.append(math.degrees(alpha))
            alpha = -((kd+k1/k2) * omega + kp * S / k2)
            # print(time,acc,speed,alpha,omega,theta,x,y,S)
            if time > 10:
                break
        self.update_charts()


    def update_charts(self):
        # pythonistas would throw a kitten at the following method
        # for finding the last value greater than 10% of peak
        y = self.y_data[2:]
        max_y = max(y)
        i = len(y)-1
        while abs(y[i]) < max_y/10:
            i = i -1
        self.ui.pg_widget.vline.setPos(self.x_data[i])
        # skip the first two elements for cleaner plot without
        # the initial conditions.
        # probably, I have a mistake there?
        self.y_plot.setData(self.x_data[2:], self.y_data[2:])
        self.speed_plot.setData(self.x_data[2:], self.speed_data[2:])
        self.theta_plot.setData(self.x_data[2:], self.theta_data[2:])
        self.omega_plot.setData(self.x_data[2:], self.omega_data[2:])
        self.alpha_plot.setData(self.x_data[2:], self.alpha_data[2:])




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('pyTurnProfiler.png'))
    window = AppWindow()
    window.setWindowTitle("Kojima Steering Simulator")
    window.show()
    sys.exit(app.exec_())
