import sys
import time
import random
import numpy as np
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
# noinspection PyUnresolvedReferences
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class Animator_View(QtWidgets.QWidget):

    def __init__(self, debug=False):
        super(Animator_View, self).__init__()

        self.setWindowTitle("Live Data Plot V0.0.1")
        layout = QtWidgets.QGridLayout(self)

        # define widget
        Real_Time_Info = QtWidgets.QLabel("T = Unknown\n"
                                          "I = Unknown\n"
                                          "U = Unknown\n"
                                          "R = Unknown\n"
                                          )
        Real_Time_Info.setFont(QFont("Consolas", 16, QFont.Bold))
        Real_Time_Info.setMargin(100)
        Current_Canvas = FigureCanvas(Figure(figsize=(5, 3)))
        Voltage_Canvas = FigureCanvas(Figure(figsize=(5, 3)))
        Resistance_Canvas = FigureCanvas(Figure(figsize=(5, 3)))

        layout.addWidget(Real_Time_Info, 1, 1)
        layout.addWidget(Current_Canvas, 1, 2)
        layout.addWidget(Voltage_Canvas, 1, 3)
        layout.addWidget(Resistance_Canvas, 2, 1, 1, -1)
        layout.addWidget(NavigationToolbar(Resistance_Canvas, self), 3, 1, 1, -1)

        Current_Canvas_Fig = Current_Canvas.figure.subplots()
        Voltage_Canvas_Fig = Voltage_Canvas.figure.subplots()
        Resistance_Canvas_Fig = Resistance_Canvas.figure.subplots()

        # debug ON
        if debug:
            self.debug()
        else:
            pass

    def debug(self, I=10):
        weight = 0.5
        ibas = random.random()
        I = 10 + random.random()
        V = weight * I + ibas
        R = V / I


if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = Animator_View()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec()
