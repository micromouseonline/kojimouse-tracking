from PyQt5.QtWidgets import *

import pyqtgraph as pg

palette = ("#101418", "#c00000", "#c000c0", "#c06000", "#00c000", "#0072c3", "#6fdc8c", "#d2a106")

# A widget subclass that holds all the plots together
class PGWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        title_style = {'color': 'cyan', 'size': '12px'}
        label_styles = {'verSpacing': -10, 'labelTextSize': '10px'}
        hline_style = {'border-style': 'solid', 'border-color': 'green', 'bottom_margin': '50px'}
        self.setStyleSheet('background-color:yellow')

        layout = QVBoxLayout()

        self.pw_y = pg.PlotWidget()
        self.pw_y.setTitle("y (mm)", **title_style)
        self.pw_y.setYRange(-25, 25)
        self.vline = pg.InfiniteLine(angle=90, movable=False)
        self.pw_y.addItem(self.vline)
        # self.pw_y.enableAutoRange()

        self.pw_theta = pg.PlotWidget()
        self.pw_theta.setTitle("theta (deg)", **title_style)
        self.pw_theta.setYRange(-10, 10)
        self.pw_theta.setXLink(self.pw_y)

        self.pw_omega = pg.PlotWidget()
        self.pw_omega.setTitle("omega (deg/s)", **title_style)
        self.pw_omega.setYRange(-300, 300)
        self.pw_omega.setXLink(self.pw_y)

        self.pw_alpha = pg.PlotWidget()
        self.pw_alpha.setTitle("&alpha (deg/s/s)", **title_style)
        self.pw_alpha.setYRange(-20000, 20000)
        self.pw_alpha.setXLink(self.pw_y)

        self.pw_speed = pg.PlotWidget()
        self.pw_speed.setTitle("speed (m/s)", **title_style)
        self.pw_speed.setYRange(0, 9)
        self.pw_speed.setXLink(self.pw_y)

        layout.addWidget(self.pw_y)
        layout.addWidget(self.pw_theta)
        layout.addWidget(self.pw_omega)
        layout.addWidget(self.pw_alpha)
        layout.addWidget(self.pw_speed)
        self.setLayout(layout)

        pg.setConfigOption('foreground', 'y')
        pg.setConfigOptions(antialias=True)
        self.axes = [self.pw_y, self.pw_theta, self.pw_omega, self.pw_alpha, self.pw_speed]
        for ax in self.axes:
            ax.showGrid(x=True, y=True)


