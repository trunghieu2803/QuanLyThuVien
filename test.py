from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

import sys
from sideBar import MySideBar

app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec()