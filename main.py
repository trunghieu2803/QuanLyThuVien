from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import ip
from ChucNang import Ui_MainWindow
class login(QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        ip.uic.loadUi('dangnhap.ui', self) 
        self.btnDangNhap.clicked.connect(self.CheckLogin)

    #kiểm tra tài khoản    
    def CheckLogin(self):
        result = ip.ConnectDB.CheckLogin(self.txbtaikhoan.text(), self.txbmatkhau.text())
        if result:
            widget.setFixedHeight(722)
            widget.setFixedWidth(1007)
            widget.move(250, 50)
            widget.setCurrentIndex(1)
        else:
            ip.QMessageBox.information(self, "Thông báo", "Tài khoản hoặc mật khẩu không đúng")
            return False



class MySideBar(QMainWindow, Ui_MainWindow):
   
    def __init__(self):
        self.check = True
        super(MySideBar, self).__init__()
        ip.uic.loadUi('ChucNang.ui', self)
        self.setWindowTitle("SideBar Menu")
        self.switch_to_tranCchuPage()


        self.ShowBooks()
        self.tableBook.cellClicked.connect(self.tableBooks_Clicked)
        self.btnUpdateBook.clicked.connect(self.updateBook)
        self.btnDeleteBook.clicked.connect(self.deleteBook)
        self.btnAddBook.clicked.connect(self.AddBook)
        self.btnShowAllBook.clicked.connect(self.ShowBooks)
        self.btnSearchBook.clicked.connect(self.searchBook)



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
    
    #Giao dien quan ly sach


    #hien thi toan bo sach
    def ShowBooks(self):
        self.tableBook.setRowCount(ip.DAL_Sach.showBookAll().__len__())
        self.tableBook.setColumnCount(5)
        self.tableBook.setHorizontalHeaderLabels(["Mã sách", "Tên sách", "Tên Tác Giả", "Giá", "Số lượng"])
        table_row = 0
        for row in ip.DAL_Sach.showBookAll():
            self.tableBook.setItem(table_row, 0, ip.QTableWidgetItem(str(row[0])))
            self.tableBook.setItem(table_row, 1, ip.QTableWidgetItem(str(row[1])))
            self.tableBook.setItem(table_row, 2, ip.QTableWidgetItem(str(row[2])))
            self.tableBook.setItem(table_row, 3, ip.QTableWidgetItem(str(row[3])))
            self.tableBook.setItem(table_row, 4, ip.QTableWidgetItem(str(row[4])))
            table_row += 1

    #clicked tablebook 
    def tableBooks_Clicked(self, row, column):
        self.txtMaSach.setText(self.tableBook.item(row, 0).text())
        self.txtTensach.setText(self.tableBook.item(row, 1).text())
        self.txtTacGia.setText(self.tableBook.item(row, 2).text())
        self.txtGiaTien.setText(self.tableBook.item(row, 3).text())
        self.txtSoLuong.setText(self.tableBook.item(row, 4).text())



    def AddBook(self):
        if(self.check == True):
            self.ShowBooks()
            table_row = ip.DAL_Sach.showBookAll()[ip.DAL_Sach.showBookAll().__len__() - 1]
            maSach = table_row[0] + 1
            self.txtMaSach.setText(str(maSach))
            self.txtTensach.setText("")
            self.txtTacGia.setText("")
            self.txtGiaTien.setText("")
            self.txtSoLuong.setText("")
            self.check = False
            self.btnAddBook.setText("Lưu")
        else:
            maSach = self.txtMaSach.text()
            tenSach = self.txtTensach.text()
            tenTG = self.txtTacGia.text()
            giaTien = self.txtGiaTien.text()
            soLuong = self.txtSoLuong.text()
            kt = ip.DAL_Sach.AddBook(maSach, tenSach, tenTG, giaTien, soLuong)
            if kt == 1:
                ip.QMessageBox.information(self, "Thông báo", "Thêm thành công!")
                self.ShowBooks()
                self.check = True
                self.txtMaSach.setText("")
                self.txtTensach.setText("")
                self.txtTacGia.setText("")
                self.txtGiaTien.setText("")
                self.txtSoLuong.setText("")
                self.btnAddBook.setText("Thêm Sách")
            else:
                ip.QMessageBox.information(self, "Thông báo", "Thêm không thành công!")
        
    def updateBook(self):
        maSach = self.txtMaSach.text()
        tenSach = self.txtTensach.text()
        tenTG = self.txtTacGia.text()
        giaTien = self.txtGiaTien.text()
        soLuong = self.txtSoLuong.text()
        kt = ip.DAL_Sach.UpdateBook(maSach, tenSach, tenTG, giaTien, soLuong)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "update thành công!")
            self.ShowBooks()
        else:
            ip.QMessageBox.information(self, "Thông báo", "update không thành công!")

    def deleteBook(self):
        maSach = self.txtMaSach.text()
        kt = ip.DAL_Sach.DeleteBook(maSach)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Xóa thành công!")
            self.txtMaSach.setText("")
            self.txtTensach.setText("")
            self.txtTacGia.setText("")
            self.txtGiaTien.setText("")
            self.txtSoLuong.setText("")
            self.ShowBooks()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Xóa không thành công!")

    def searchBook(self):
        tenSach = self.txtSearchBook.text()
        data = ip.DAL_Sach.SearchBook(tenSach)
        self.tableBook.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableBook.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableBook.setItem(row_number, column_number, ip.QTableWidgetItem(str(data)))


app = QApplication(ip.sys.argv)
widget = ip.QtWidgets.QStackedWidget()
login_f = login()
mainGui_f = MySideBar()
widget.addWidget(login_f)
widget.addWidget(mainGui_f)
widget.setCurrentIndex(0)
widget.setFixedHeight(436)
widget.setFixedWidth(877)
widget.show()
app.exec()
