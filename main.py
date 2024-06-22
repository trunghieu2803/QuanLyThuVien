from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import ip
from ChucNang import Ui_MainWindow
from PyQt6.QtCore import QDate
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
        self.switch_to_trangchuPage()


        #chuc nang Book
        self.ShowBooks()
        self.tableBook.cellClicked.connect(self.tableBooks_Clicked)
        self.btnUpdateBook.clicked.connect(self.updateBook)
        self.btnDeleteBook.clicked.connect(self.deleteBook)
        self.btnAddBook.clicked.connect(self.AddBook)
        self.btnShowAllBook.clicked.connect(self.ShowBooks)
        self.btnSearchBook.clicked.connect(self.searchBook)
        self.btnXuatFile.clicked.connect(self.PrintBooktoExcel)



        #chức năng nhân viên
        self.ShowALLNhanvien()
        self.btnShowAllNV.clicked.connect(self.ShowALLNhanvien)
        self.tableNV.cellClicked.connect(self.tableNhanVien_Clicked)
        self.btnAddNV.clicked.connect(self.AddNhanVien)
        self.btnDeleteNV.clicked.connect(self.DeleteNhanVien)
        self.btnUpdateNV.clicked.connect(self.UpdateNhanVien)
        self.btnSearchNV.clicked.connect(self.searchNhanVien)
        self.btnXuatFileNV.clicked.connect(self.PrintNhanVientoExcel)

        #chuyển trang
        self.btnTrangChu.clicked.connect(self.switch_to_trangchuPage)
        self.btnSach.clicked.connect(self.switch_to_sachPage)
        self.btnNhanVien.clicked.connect(self.switch_to_NhanVienPage)
        self.btnDocGia.clicked.connect(self.switch_to_DocgiaPage)
        self.btnHoaDon.clicked.connect(self.switch_to_hoaDonPage)
        self.btnCTHoaDon.clicked.connect(self.switch_to_cthoaDonPage)
        self.btnMuonTra.clicked.connect(self.switch_to_muonTraPage)


    def switch_to_trangchuPage(self):
        self.tabWidget.setCurrentIndex(0)
    def switch_to_sachPage(self):
        self.tabWidget.setCurrentIndex(1)
    def switch_to_NhanVienPage(self):
        self.tabWidget.setCurrentIndex(2)
    def switch_to_DocgiaPage(self):
        self.tabWidget.setCurrentIndex(3)    
    def switch_to_hoaDonPage(self):
        self.tabWidget.setCurrentIndex(4)
    def switch_to_cthoaDonPage(self):
        self.tabWidget.setCurrentIndex(5)
    def switch_to_muonTraPage(self):
        self.tabWidget.setCurrentIndex(6)
    
    #Giao dien quan ly sach

#region ###########################  BOOK ##################### 
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


#Thêm Sách
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


    #cập nhật sách
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

#tìm kiếm sách
    def searchBook(self):
        tenSach = self.txtSearchBook.text()
        data = ip.DAL_Sach.SearchBook(tenSach)
        self.tableBook.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableBook.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableBook.setItem(row_number, column_number, ip.QTableWidgetItem(str(data)))

#in sách ra excel
    def PrintBooktoExcel(self):
        ip.DAL_Sach.XuatFileBook()

#endregion ###########################  END BOOK #############  

#region ########################### Nhân Viên ##################
    def ShowALLNhanvien(self):
        self.tableNV.setRowCount(ip.DAL_NhanVien.showALLNhanVien().__len__())
        self.tableNV.setColumnCount(9)
        self.tableNV.setHorizontalHeaderLabels(["Mã nhân viên", "Tên nhân viên", "Giới tính", "Ngày sinh",
                                                     "Địa chỉ", "Số điện thoại", "tên đăng nhập", "Mật khẩu", "Chức Vụ"])
        table_row = 0
        for row in ip.DAL_NhanVien.showALLNhanVien():
            self.tableNV.setItem(table_row, 0, ip.QTableWidgetItem(str(row[0])))
            self.tableNV.setItem(table_row, 1, ip.QTableWidgetItem(str(row[1])))
            self.tableNV.setItem(table_row, 2, ip.QTableWidgetItem(str(row[2])))
            self.tableNV.setItem(table_row, 3, ip.QTableWidgetItem(str(row[3])))
            self.tableNV.setItem(table_row, 4, ip.QTableWidgetItem(str(row[4])))
            self.tableNV.setItem(table_row, 5, ip.QTableWidgetItem(str(row[5])))
            self.tableNV.setItem(table_row, 6, ip.QTableWidgetItem(str(row[6])))
            self.tableNV.setItem(table_row, 7, ip.QTableWidgetItem(str(row[7])))
            self.tableNV.setItem(table_row, 8, ip.QTableWidgetItem(str(row[8])))
            table_row += 1
    
    def tableNhanVien_Clicked(self, row, column):
        dateFirt = ip.QDate.fromString(self.tableNV.item(row, 3).text(), "yyyy-MM-dd")
        self.txtMaNV.setText(self.tableNV.item(row, 0).text())
        self.txtHoTenNV.setText(self.tableNV.item(row, 1).text())

        #Xử lí click vào cell  nào thì combobox hiện lên thông tin đấy
        gioitinh = self.tableNV.item(row, 2).text()
        for i in range(self.cbbgioitinhNV.count()):
            if(gioitinh == self.cbbgioitinhNV.itemText(i)):
                self.cbbgioitinhNV.setCurrentIndex(i)
        #----------------
               
        self.NgaySinhNV.setDate(dateFirt)
        self.txtDiaChiNV.setText(self.tableNV.item(row, 4).text())
        self.txtSDTNV.setText(self.tableNV.item(row, 5).text())
        self.txtTenDangNhap.setText(self.tableNV.item(row, 6).text())
        self.txtMatKhau.setText(self.tableNV.item(row, 7).text())
        chucVu = self.tableNV.item(row, 8).text()
        for i in range(self.cbbChucVuNV.count()):
            if(chucVu == self.cbbChucVuNV.itemText(i)):
                self.cbbChucVuNV.setCurrentIndex(i)

    def SetDefaultNhanVienTxt(self):
        self.txtMaNV.setText("")
        self.txtHoTenNV.setText("")
        self.cbbgioitinhNV.setCurrentIndex(0)
        self.NgaySinhNV.setDate(QDate(2024, 6, 22))
        self.txtDiaChiNV.setText("")
        self.txtSDTNV.setText("")
        self.txtTenDangNhap.setText("")
        self.txtMatKhau.setText("")
        self.cbbChucVuNV.setCurrentIndex(1)
        self.check = True


    def AddNhanVien(self):
        if(self.check == True):
            self.ShowALLNhanvien()
            table_row = ip.DAL_NhanVien.showALLNhanVien()[ip.DAL_NhanVien.showALLNhanVien().__len__() - 1]
            maNV = table_row[0] + 1
            self.txtMaNV.setText(str(maNV))
            self.txtHoTenNV.setText("")
            self.cbbgioitinhNV.setCurrentIndex(0)
            self.NgaySinhNV.setDate(QDate(2024, 6, 22))
            self.txtDiaChiNV.setText("")
            self.txtSDTNV.setText("")
            self.txtTenDangNhap.setText("")
            self.txtMatKhau.setText("")
            self.cbbChucVuNV.setCurrentIndex(1)
            self.check = False
            self.btnAddNV.setText("Lưu")
        else:
            maNV = self.txtMaNV.text()
            tenNV = self.txtHoTenNV.text()
            gioiTinh = self.cbbgioitinhNV.currentText()
            ngaySinh = self.NgaySinhNV.date().toString("yyyy-MM-dd")
            diaChi = self.txtDiaChiNV.text()
            sdt = self.txtSDTNV.text()
            tenDangnhap = self.txtTenDangNhap.text()
            matKhau = self.txtMatKhau.text()
            chucVu = self.cbbChucVuNV.currentText()
            kt = ip.DAL_NhanVien.AddNhanVien(maNV, tenNV, gioiTinh, ngaySinh, diaChi, sdt, tenDangnhap, matKhau, chucVu)
            if kt == 1:
                ip.QMessageBox.information(self, "Thông báo", "Thêm thành công!")
                self.ShowALLNhanvien()
                self.SetDefaultNhanVienTxt()
                self.btnAddNV.setText("Thêm Nhân viên")
            else:
                ip.QMessageBox.information(self, "Thông báo", "Thêm không thành công!")


    def UpdateNhanVien(self):
        maNV = self.txtMaNV.text()
        tenNV = self.txtHoTenNV.text()
        gioiTinh = self.cbbgioitinhNV.currentText()
        ngaySinh = self.NgaySinhNV.date().toString("yyyy-MM-dd")
        diaChi = self.txtDiaChiNV.text()
        sdt = self.txtSDTNV.text()
        tenDangnhap = self.txtTenDangNhap.text()
        matKhau = self.txtMatKhau.text()
        chucVu = self.cbbChucVuNV.currentText()

        kt = ip.DAL_NhanVien.UpdateNhanVien(maNV, tenNV, gioiTinh, ngaySinh, diaChi, sdt, tenDangnhap, matKhau, chucVu)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "update thành công!")
            self.ShowALLNhanvien()
        else:
            ip.QMessageBox.information(self, "Thông báo", "update không thành công!")



    def DeleteNhanVien(self):
        txtMaNV = self.txtMaNV.text()
        kt = ip.DAL_NhanVien.DeleteNhanVien(txtMaNV)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Xóa thành công!")
            self.ShowALLNhanvien()
            self.SetDefaultNhanVienTxt()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Xóa không thành công!")


    def searchNhanVien(self):
        maTenSach = self.txtSearchNV.text()
        data = ip.DAL_NhanVien.SearchNhanVien(maTenSach)
        self.tableNV.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableNV.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableNV.setItem(row_number, column_number, ip.QTableWidgetItem(str(data)))

    #in sách ra excel
    def PrintNhanVientoExcel(self):
        ip.DAL_NhanVien.XuatFileNhanVien()

#endregion   ########################### End Nhân Viên ##################     


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
