from PyQt6.QtCore import Qt
from main import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")

        self.btnTrangChu.clicked.connect(self.switch_to_tranCchuPage)

        self.btnSach.clicked.connect(self.switch_to_sachPage)
    
        self.btnTaiKhoan.clicked.connect(self.switch_to_taiKhoanPage)

        self.btnHoaDon.clicked.connect(self.switch_to_hoaDonPage)

        self.btnMuonTra.clicked.connect(self.switch_to_muonTraPage)


    def switch_to_tranCchuPage(self):
        self.tabWidget.setCurrentIndex(0)
    def switch_to_sachPage(self):
        self.tabWidget.setCurrentIndex(1)
    def switch_to_taiKhoanPage(self):
        self.tabWidget.setCurrentIndex(2)
    def switch_to_hoaDonPage(self):
        self.tabWidget.setCurrentIndex(3)
    def switch_to_muonTraPage(self):
        self.tabWidget.setCurrentIndex(4)
    