import sys
from PySide6 import QtCore, QtWidgets
from test import Automatic_Instrument_Detection as autoDetection


class Demo_UI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoDetection_Demo_V0.3")
        self.button = QtWidgets.QPushButton("Detection Instrument")
        self.text = QtWidgets.QLabel("Click the button to start detection Instrument", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.detect)

    @QtCore.Slot()
    def detect(self):
        Detection_Info = autoDetection.detection()
        self.text.setText(Detection_Info)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    UI = Demo_UI()
    UI.resize(400, 300)
    UI.show()

    sys.exit(app.exec())
