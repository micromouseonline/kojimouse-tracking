# -*- coding: utf-8 -*

from PyQt5 import QtCore, QtGui, QtWidgets
from pgwidget import PGWidget

class QHLine(QtWidgets.QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.pg_widget = PGWidget()
        self.control_widget = self.make_controls()

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.pg_widget)
        hbox.addWidget(self.control_widget)
        self.centralwidget.setLayout(hbox)
        MainWindow.setCentralWidget(self.centralwidget)

    def make_controls(self):
        control_widget = QtWidgets.QWidget()

        self.lbl_kp = QtWidgets.QLabel("Kp")
        self.lbl_kp.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_kp = QtWidgets.QSpinBox()
        self.sb_kp.setFrame(True)
        self.sb_kp.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_kp.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_kp.setMinimum(0)
        self.sb_kp.setMaximum(40000)
        self.sb_kp.setSingleStep(500)
        self.sb_kp.setProperty("value", 12000)

        self.lbl_kd = QtWidgets.QLabel("Kd")
        self.lbl_kd.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_kd = QtWidgets.QSpinBox()
        self.sb_kd.setFrame(True)
        self.sb_kd.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_kd.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_kd.setMinimum(5)
        self.sb_kd.setMaximum(1000)
        self.sb_kd.setProperty("value", 200)

        self.lbl_k1 = QtWidgets.QLabel("K1")
        self.lbl_k1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_k1 = QtWidgets.QDoubleSpinBox()
        self.sb_k1.setFrame(True)
        self.sb_k1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_k1.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_k1.setDecimals(3)
        self.sb_k1.setMinimum(0.0)
        self.sb_k1.setMaximum(5.0)
        self.sb_k1.setSingleStep(0.025)
        self.sb_k1.setProperty("value", 0.2)

        self.lbl_k2 = QtWidgets.QLabel("K2")
        self.lbl_k2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_k2 = QtWidgets.QDoubleSpinBox()
        self.sb_k2.setFrame(True)
        self.sb_k2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_k2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_k2.setDecimals(3)
        self.sb_k2.setMinimum(0.0)
        self.sb_k2.setMaximum(0.5)
        self.sb_k2.setSingleStep(0.001)
        self.sb_k2.setProperty("value", 0.02)


        self.lbl_acc = QtWidgets.QLabel("Acceleration (m/s/s):")
        self.lbl_acc.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_acc = QtWidgets.QDoubleSpinBox()
        self.sb_acc.setFrame(True)
        self.sb_acc.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_acc.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_acc.setMinimum(1.0)
        self.sb_acc.setMaximum(25.0)
        self.sb_acc.setSingleStep(0.2)
        self.sb_acc.setProperty("value", 9.8)

        self.lbl_alpha_max = QtWidgets.QLabel("Alpha Max:")
        self.lbl_alpha_max.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_alpha_max = QtWidgets.QSpinBox()
        self.sb_alpha_max.setFrame(True)
        self.sb_alpha_max.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_alpha_max.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_alpha_max.setMinimum(50)
        self.sb_alpha_max.setMaximum(500)
        self.sb_alpha_max.setProperty("value", 300)


        self.lbl_y_init = QtWidgets.QLabel("y offset (mm):")
        self.lbl_y_init.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_y_init = QtWidgets.QSpinBox()
        self.sb_y_init.setFrame(True)
        self.sb_y_init.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_y_init.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_y_init.setMinimum(0)
        self.sb_y_init.setMaximum(35)
        self.sb_y_init.setSingleStep(1)
        self.sb_y_init.setValue(10)

        self.lbl_omega_init = QtWidgets.QLabel("Omega (deg/s):")
        self.lbl_omega_init.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_omega_init = QtWidgets.QDoubleSpinBox()
        self.sb_omega_init.setFrame(True)
        self.sb_omega_init.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_omega_init.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_omega_init.setMinimum(-200.0)
        self.sb_omega_init.setMaximum(200.0)
        self.sb_omega_init.setSingleStep(10)
        self.sb_omega_init.setProperty("value", 0)

        self.lbl_theta_init = QtWidgets.QLabel("Theta (deg):")
        self.lbl_theta_init.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_theta_init = QtWidgets.QSpinBox()
        self.sb_theta_init.setFrame(True)
        self.sb_theta_init.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_theta_init.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_theta_init.setMinimum(-20)
        self.sb_theta_init.setMaximum(20)
        self.sb_theta_init.setProperty("value", 0)

        self.lbl_speed_init = QtWidgets.QLabel("Speed (m/s):")
        self.lbl_speed_init.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_speed_init = QtWidgets.QDoubleSpinBox()
        self.sb_speed_init.setFrame(True)
        self.sb_speed_init.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_speed_init.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_speed_init.setMinimum(0.0)
        self.sb_speed_init.setMaximum(9.0)
        self.sb_speed_init.setSingleStep(0.1)
        self.sb_speed_init.setProperty("value", 1.0)

        # Constraints
        self.lbl_v_max = QtWidgets.QLabel("Speed Max (m/s):")
        self.lbl_v_max.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_v_max = QtWidgets.QDoubleSpinBox()
        self.sb_v_max.setFrame(True)
        self.sb_v_max.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_v_max.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_v_max.setMinimum(0.5)
        self.sb_v_max.setMaximum(10.0)
        self.sb_v_max.setSingleStep(0.1)
        self.sb_v_max.setProperty("value", 6.0)

        self.lbl_alpha_max = QtWidgets.QLabel("Alpha Max (deg/s/s):")
        self.lbl_alpha_max.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_alpha_max = QtWidgets.QSpinBox()
        self.sb_alpha_max.setFrame(True)
        self.sb_alpha_max.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sb_alpha_max.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.sb_alpha_max.setMinimum(500)
        self.sb_alpha_max.setMaximum(25000)
        self.sb_alpha_max.setSingleStep(500)
        self.sb_alpha_max.setProperty("value", 15000)


        # controller constants
        self.gb_controls = QtWidgets.QGroupBox("Controls:")
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.lbl_kp,       0,0)
        grid.addWidget(self.sb_kp,        0,1)
        grid.addWidget(self.lbl_kd,       1,0)
        grid.addWidget(self.sb_kd,        1,1)
        grid.addWidget(self.lbl_k1,       2,0)
        grid.addWidget(self.sb_k1,        2,1)
        grid.addWidget(self.lbl_k2,       3,0)
        grid.addWidget(self.sb_k2,        3,1)

        self.gb_controls.setLayout(grid)

        self.gb_initial = QtWidgets.QGroupBox("Initial Conditions:")
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.lbl_y_init,      1, 0)
        grid.addWidget(self.sb_y_init,       1, 1)
        grid.addWidget(self.lbl_theta_init,  2, 0)
        grid.addWidget(self.sb_theta_init,   2, 1)
        grid.addWidget(self.lbl_omega_init,  3, 0)
        grid.addWidget(self.sb_omega_init,   3, 1)
        grid.addWidget(self.lbl_speed_init,  4, 0)
        grid.addWidget(self.sb_speed_init,   4, 1)
        grid.addWidget(self.lbl_acc,      5,0)
        grid.addWidget(self.sb_acc,       5,1)
        self.gb_initial.setLayout(grid)

        self.gb_constraints = QtWidgets.QGroupBox("Constraints:")
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.lbl_v_max,      1, 0)
        grid.addWidget(self.sb_v_max,       1, 1)
        grid.addWidget(self.lbl_alpha_max,  2, 0)
        grid.addWidget(self.sb_alpha_max,   2, 1)
        self.gb_constraints.setLayout(grid)

        self.btn_reset = QtWidgets.QPushButton("RESET")
        self.btn_reset.setStyleSheet('QPushButton {background-color: #A3C1DA; border:  none}')
        self.btn_reset.setFixedHeight(32)

        self.controls_layout = QtWidgets.QVBoxLayout()
        self.controls_layout.addWidget(self.gb_controls)
        self.controls_layout.addWidget(QHLine())
        self.controls_layout.addWidget(self.gb_initial)
        self.controls_layout.addWidget(QHLine())
        self.controls_layout.addWidget(self.gb_constraints)
        self.controls_layout.addWidget(QHLine())
        self.controls_layout.addWidget(self.btn_reset)
        self.controls_layout.addWidget(QHLine())


        spacerItem = QtWidgets.QSpacerItem(240, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controls_layout.addSpacerItem(spacerItem)
        control_widget.setLayout(self.controls_layout)
        return control_widget



