from PyQt5.QtWidgets import *

import pyqtgraph as pg
import numpy as np

palette = ("#101418", "#c00000", "#c000c0", "#c06000", "#00c000", "#0072c3", "#6fdc8c", "#d2a106")

# A widget subclass that holds all the plots together
class PGWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        title_style = {'color': 'cyan', 'size': '12px'}
        label_styles = {'verSpacing': -10, 'labelTextSize': '10px', 'color':'cyan'}
        hline_style = {'border-style': 'solid', 'border-color': 'green', 'bottom_margin': '50px'}
        self.setStyleSheet('background-color:yellow')

        layout = QVBoxLayout()

        self.pw_y = pg.PlotWidget()
        self.pw_y.setTitle("distance error", **title_style)
        self.pw_y.setYRange(-25, 25)
        self.pw_y.setLabel('bottom','distance',units='m', **label_styles)
        self.pw_y.setLabel('left','y',units='mm', **label_styles)

        self.vline = pg.InfiniteLine(angle=90, movable=False)
        self.pw_y.addItem(self.vline)
        # self.pw_y.enableAutoRange()

        self.pw_theta = pg.PlotWidget()
        self.pw_theta.setTitle("angle error", **title_style)
        self.pw_theta.setYRange(-12, 12)
        self.pw_theta.setXLink(self.pw_y)
        self.pw_theta.setLabel('bottom','distance',units='m', **label_styles)
        self.pw_theta.setLabel('left','theta',units='deg', **label_styles)

        self.pw_omega = pg.PlotWidget()
        self.pw_omega.setTitle("angular velocity", **title_style)
        self.pw_omega.setYRange(-300, 300)
        self.pw_omega.setXLink(self.pw_y)
        self.pw_omega.setLabel('bottom','distance',units='m', **label_styles)
        self.pw_omega.setLabel('left','omega',units='deg/s', **label_styles)

        self.pw_alpha = pg.PlotWidget()
        self.pw_alpha.setTitle("controller output (angular acceleration)", **title_style)
        self.pw_alpha.setYRange(-20000, 20000)
        self.pw_alpha.setXLink(self.pw_y)
        self.pw_alpha.setLabel('bottom','distance',units='m', **label_styles)
        self.pw_alpha.setLabel('left','alpha',units='deg/s/s', **label_styles)

        self.pw_speed = pg.PlotWidget()
        self.pw_speed.setTitle("robot speed", **title_style)
        self.pw_speed.setYRange(0, 9)
        self.pw_speed.setXLink(self.pw_y)
        self.pw_speed.setLabel('bottom','distance',units='m', **label_styles)
        self.pw_speed.setLabel('left','v',units='m/s', **label_styles)

        layout.addWidget(self.pw_y)
        layout.addWidget(self.pw_theta)
        layout.addWidget(self.pw_omega)
        layout.addWidget(self.pw_alpha)
        layout.addWidget(self.pw_speed)
        self.setLayout(layout)

        pg.setConfigOption('foreground', 'y')
        pg.setConfigOptions(antialias=True)
        self.axes = [self.pw_y, self.pw_theta, self.pw_omega, self.pw_alpha, self.pw_speed]
        dx = [(v,f'{v:.3f}') for v in list(np.arange(0,1.9,0.18))]
        print(dx)
        for ax in self.axes:
            ax.showGrid(x=True, y=True)
            ax.getAxis('bottom').setTicks([dx])



