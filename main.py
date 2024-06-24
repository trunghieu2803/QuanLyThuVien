from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import ip
from ChucNang import Ui_MainWindow
from PyQt6.QtCore import QDate
class Login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Login, self).__init__()
        ip.uic.loadUi('dangnhap.ui', self) 

        self.btnDangNhap.clicked.connect(self.CheckLogin)

    #kiểm tra tài khoản    
    def CheckLogin(self):
        try:
            result = ip.ConnectDB.CheckLogin(self.txbtaikhoan.text(), self.txbmatkhau.text())
            if result:
                self.txbtaikhoan.setText("")
                self.txbmatkhau.setText("")
                ip.glchucvu = result
                if ip.glchucvu == "Thủ thư":
                    ip.checkChucVu = False
                else:
                    ip.checkChucVu = True
                widget.setFixedHeight(722)
                widget.setFixedWidth(1007)
                widget.move(250, 50)
                mainGui_f = MySideBar()
                widget.addWidget(mainGui_f)
                widget.setCurrentIndex(1)
        except:
            ip.QMessageBox.information(self, "Thông báo", "Tài khoản hoặc mật khẩu không đúng")


class MySideBar(QMainWindow, Ui_MainWindow):
   
    def __init__(self):
        self.check = True
        self.is_handling_event = False
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
        self.txtSearchBook.textChanged.connect(self.searchBook)




        #chức năng nhân viên
        self.ShowALLNhanvien()
        self.btnShowAllNV.clicked.connect(self.ShowALLNhanvien)
        self.tableNV.cellClicked.connect(self.tableNhanVien_Clicked)
        self.btnAddNV.clicked.connect(self.AddNhanVien)
        self.btnDeleteNV.clicked.connect(self.DeleteNhanVien)
        self.btnUpdateNV.clicked.connect(self.UpdateNhanVien)
        self.btnSearchNV.clicked.connect(self.searchNhanVien)
        self.btnXuatFileNV.clicked.connect(self.PrintNhanVientoExcel)
        self.txtSearchNV.textChanged.connect(self.searchNhanVien)




        #Chức năng độc giả
        self.ShowALLDocGia()
        self.btnShowAllDG.clicked.connect(self.ShowALLDocGia)
        self.tableDocGia.cellClicked.connect(self.tableDocGia_Clicked)
        self.btnAddDG.clicked.connect(self.AddDocGia)
        self.btnDeleteDG.clicked.connect(self.DeleteDocGia)
        self.btnUpdateDG.clicked.connect(self.UpdateDocGia)
        self.btnSearchDG.clicked.connect(self.SearchDocGia)
        self.btnXuatFileDG.clicked.connect(self.PrintDocGiatoExcel)
        self.txtSearchDG.textChanged.connect(self.SearchDocGia)



        #chức năng hóa đơn
        self.ShowALLHoaDonMT()
        self.btnShowAllHD.clicked.connect(self.ShowALLHoaDonMT)
        self.tableHoaDon.cellClicked.connect(self.tableHoaDonMT_Clicked)
        self.btnAddHD.clicked.connect(self.AddHoaDon)
        self.cbbDGHD.currentIndexChanged.connect(self.on_cbbDGHD_changed)
        self.cbbMNVHD.currentIndexChanged.connect(self.on_cbbMNVHD_changed)
        self.btnDeleteHD.clicked.connect(self.DeleteHoaDon)
        self.btnUpdateHD.clicked.connect(self.UpdateHoaDon)
        self.btnSearchHD.clicked.connect(self.SearchHoaDon)
        # self.btnXuatFileDG.clicked.connect(self.PrintDocGiatoExcel)
        self.txtSearchHD.textChanged.connect(self.SearchHoaDon)


        #Chức năng Chi tiết hóa đơn
        self.ShowALLCTHoaDonMT()
        self.btnShowAllCTHD.clicked.connect(self.ShowALLCTHoaDonMT)
        self.tableCTHD.cellClicked.connect(self.tableCTHoaDonMT_Clicked)
        self.btnAddCTHD.clicked.connect(self.AddCTHoaDonMuontra)
        self.cbbMHDCTHD.currentIndexChanged.connect(self.ShowALLCTHoaDonByMaMuonTraMT)
        self.cbbMaSachCTHD.currentIndexChanged.connect(self.ShowSachBYMaSach)
        self.btnDeleteCTHD.clicked.connect(self.DeleteCTHDByMaMuonTraMaSach)
        self.btnUpdateCTHD.clicked.connect(self.UpdateCTHoaDonMuonTra)
        self.btnSearchCTHD.clicked.connect(self.SearchCTHoaDonMuonTra)
        self.txtSearchCTHD.textChanged.connect(self.SearchCTHoaDonMuonTra)
        self.btnXuatFileCTHD.clicked.connect(self.PrintCTMuonTratoExcel)



        #chuyển trang
        self.btnTrangChu.clicked.connect(self.switch_to_trangchuPage)
        self.btnSach.clicked.connect(self.switch_to_sachPage)
        self.btnNhanVien.clicked.connect(self.switch_to_NhanVienPage)
        self.btnDocGia.clicked.connect(self.switch_to_DocgiaPage)
        self.btnHoaDonMuonTra.clicked.connect(self.switch_to_HoaDonMuonTraPage)
        self.btnMuonTra.clicked.connect(self.switch_to_muonTraPage)
        self.btnDangXuat.clicked.connect(self.switch_to_DangXuatPage)

    def switch_to_trangchuPage(self):
        print(ip.checkChucVu)
        self.btnNhanVien.setEnabled(ip.checkChucVu)
        self.tabWidget.setCurrentIndex(0)
    def switch_to_sachPage(self):
        self.ShowBooks()
        self.tabWidget.setCurrentIndex(1)
    def switch_to_NhanVienPage(self):
        self.tabWidget.setCurrentIndex(2)
    def switch_to_DocgiaPage(self):
        self.tabWidget.setCurrentIndex(3) 
    def switch_to_HoaDonMuonTraPage(self):
        self.tabWidget.setCurrentIndex(4)   
    def switch_to_muonTraPage(self):
        self.ShowALLCTHoaDonMT()
        self.tabWidget.setCurrentIndex(5)
    def switch_to_DangXuatPage(self):
        reply = ip.QMessageBox.question(self, 'Xác nhận', 
                                     "Bạn có muốn đăng xuất không?", 
                                     ip.QMessageBox.StandardButton.Yes | ip.QMessageBox.StandardButton.No, 
                                     ip.QMessageBox.StandardButton.No)

        if reply == ip.QMessageBox.StandardButton.Yes:
            print("dang xuat " + str(ip.checkChucVu))
            self.switch_to_trangchuPage()
            ip.glchucvu = ""
            widget.move(300, 200)
            widget.setFixedHeight(436)
            widget.setFixedWidth(877)
            widget.setCurrentIndex(0)
            print("Đăng xuất ngay!")
        else:
            print("Hủy đăng xuất")

    def on_combobox_changed(self, index):
        self.cbbgioitinhDG.clear()
        selected_text = self.cbbgioitinhDG.currentText()
        print(f"Bạn đã chọn: {selected_text}")    
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

#region ###################### ĐỘC GIẢ ################################

    def ShowALLDocGia(self):
            self.tableDocGia.setRowCount(ip.DAL_DocGia.showAllDocGia().__len__())
            self.tableDocGia.setColumnCount(5)
            self.tableDocGia.setHorizontalHeaderLabels(["Mã độc giả", "Tên độc giả", "Địa chỉ",
                                                        "Giới tính", "Số điện thoại"])
            table_row = 0
            for row in ip.DAL_DocGia.showAllDocGia():
                self.tableDocGia.setItem(table_row, 0, ip.QTableWidgetItem(str(row[0])))
                self.tableDocGia.setItem(table_row, 1, ip.QTableWidgetItem(str(row[1])))
                self.tableDocGia.setItem(table_row, 2, ip.QTableWidgetItem(str(row[2])))
                self.tableDocGia.setItem(table_row, 3, ip.QTableWidgetItem(str(row[3])))
                self.tableDocGia.setItem(table_row, 4, ip.QTableWidgetItem(str(row[4])))
                table_row += 1


    def tableDocGia_Clicked(self, row, column):
        self.txtMaDG.setText(self.tableDocGia.item(row, 0).text())
        self.txtHoTenDG.setText(self.tableDocGia.item(row, 1).text())
        self.txtDiaChiDG.setText(self.tableDocGia.item(row, 2).text())
        #Xử lí click vào cell  nào thì combobox hiện lên thông tin đấy
        gioitinh = self.tableDocGia.item(row, 3).text()
        for i in range(self.cbbgioitinhDG.count()):
            if(gioitinh == self.cbbgioitinhDG.itemText(i)):
                self.cbbgioitinhDG.setCurrentIndex(i)
        #----------------
        self.txtSDTDG.setText(self.tableDocGia.item(row, 4).text())

    
    def SetDefaultDocgiaTxt(self):
        self.txtMaDG.setText("")
        self.txtHoTenDG.setText("")
        self.txtDiaChiDG.setText("")
        self.cbbgioitinhDG.setCurrentIndex(0)
        self.txtSDTDG.setText("")
        self.check = True


    def AddDocGia(self):
        if(self.check == True):
            self.ShowALLDocGia()
            table_row = ip.DAL_DocGia.showAllDocGia()[ip.DAL_DocGia.showAllDocGia().__len__() - 1]
            maDG = table_row[0] + 1
            self.txtMaDG.setText(str(maDG))
            self.txtHoTenDG.setText("")
            self.txtDiaChiDG.setText("")
            self.cbbgioitinhDG.setCurrentIndex(0)
            self.txtSDTDG.setText("")
            self.check = False
            self.btnAddDG.setText("Lưu")
        else:
            ma = self.txtMaDG.text()
            ten = self.txtHoTenDG.text()
            diaChi = self.txtDiaChiDG.text()
            gioiTinh = self.cbbgioitinhDG.currentText()
            sdt = self.txtSDTDG.text()
            kt = ip.DAL_DocGia.AddDocGia(ma, ten, diaChi, gioiTinh, sdt)
            if kt == 1:
                ip.QMessageBox.information(self, "Thông báo", "Thêm thành công!")
                self.ShowALLDocGia()
                self.SetDefaultDocgiaTxt()
                self.btnAddDG.setText("Thêm độc giả")
            else:
                ip.QMessageBox.information(self, "Thông báo", "Thêm không thành công!")


    def DeleteDocGia(self):
        txtMaDG = self.txtMaDG.text()
        kt = ip.DAL_DocGia.DeleteDocGia(txtMaDG)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Xóa thành công!")
            self.ShowALLDocGia()
            self.SetDefaultDocgiaTxt()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Xóa không thành công!")

    def UpdateDocGia(self):
        ma = self.txtMaDG.text()
        ten = self.txtHoTenDG.text()
        diaChi = self.txtDiaChiDG.text()
        gioiTinh = self.cbbgioitinhDG.currentText()
        sdt = self.txtSDTDG.text()

        kt = ip.DAL_DocGia.UpdateDocGia(ma, ten, diaChi, gioiTinh, sdt)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "update thành công!")
            self.ShowALLDocGia()
        else:
            ip.QMessageBox.information(self, "Thông báo", "update không thành công!")


    def SearchDocGia(self):
        maTenDocGia = self.txtSearchDG.text()
        data = ip.DAL_DocGia.SearchDocGia(maTenDocGia)
        self.tableDocGia.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableDocGia.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableDocGia.setItem(row_number, column_number, ip.QTableWidgetItem(str(data)))

    #in sách ra excel
    def PrintDocGiatoExcel(self):
        ip.DAL_DocGia.XuatFileDocGia()
#endregion ######################## END ĐỘC GIẢ ########################

#region ##################### Hóa Đơn ###################################
    
    def ShowALLHoaDonMT(self):
        self.cbbDGHD.clear()
        self.cbbMNVHD.clear()
        for i in range(ip.DAL_DocGia.showAllDocGia().__len__()):
            self.cbbDGHD.addItem(str(i + 1))

        for i in range(ip.DAL_NhanVien.showALLNhanVien().__len__()):
            self.cbbMNVHD.addItem(str(i + 1))

        self.tableHoaDon.setRowCount(ip.DAL_HoaDonMT.ShowAllHDMuonTra().__len__())
        self.tableHoaDon.setColumnCount(5)
        self.tableHoaDon.setHorizontalHeaderLabels(["mã hóa đơn", "Tên hóa đơn", "Ngày mượn",
                                                    "Mã độc giả", "Mã nhân viên"])
        table_row = 0
        for row in ip.DAL_HoaDonMT.ShowAllHDMuonTra():
            self.tableHoaDon.setItem(table_row, 0, ip.QTableWidgetItem(str(row[0])))
            self.tableHoaDon.setItem(table_row, 1, ip.QTableWidgetItem(str(row[1])))
            self.tableHoaDon.setItem(table_row, 2, ip.QTableWidgetItem(str(row[2])))
            self.tableHoaDon.setItem(table_row, 3, ip.QTableWidgetItem(str(row[3])))
            self.tableHoaDon.setItem(table_row, 4, ip.QTableWidgetItem(str(row[4])))
            table_row += 1

    def tableHoaDonMT_Clicked(self, row, column):
        dateFirt = ip.QDate.fromString(self.tableHoaDon.item(row, 2).text(), "yyyy-MM-dd")
        self.txtMaHD.setText(self.tableHoaDon.item(row, 0).text())
        self.txtTenHD.setText(self.tableHoaDon.item(row, 1).text())
        self.dateNgayMuonHD.setDate(dateFirt)
        #Xử lí click vào cell  nào thì combobox hiện lên thông tin đấy
        maDocGia = self.tableHoaDon.item(row, 3).text()
        for i in range(self.cbbDGHD.count()):
            if(maDocGia == self.cbbDGHD.itemText(i)):
                self.cbbDGHD.setCurrentIndex(i)
                self.txtTenDocGiaHD.setText(ip.DAL_DocGia.SearchMaDocGia(str(i+1))[0][1])
        #----------------
        
        maNhanVien = self.tableHoaDon.item(row, 4).text()
        for i in range(self.cbbMNVHD.count()):
            if(maNhanVien == self.cbbMNVHD.itemText(i)):
                self.cbbMNVHD.setCurrentIndex(i)
                self.txtNhanVienLapHoaDon.setText(ip.DAL_NhanVien.SearchMaNhanVien(str(i+1))[0][1])


    def SetDefaultHoaDonTxt(self):
        self.txtMaHD.setText("")
        self.txtTenHD.setText("")
        self.dateNgayMuonHD.setDate(QDate(2024, 6, 22))
        self.cbbDGHD.setCurrentIndex(0)
        self.cbbMNVHD.setCurrentIndex(0)
        self.txtTenDocGiaHD.setText("")
        self.txtNhanVienLapHoaDon.setText("")
        self.check = True


    def AddHoaDon(self):
        if(self.check == True):
            self.ShowALLHoaDonMT()
            table_row = ip.DAL_HoaDonMT.ShowAllHDMuonTra()[ip.DAL_HoaDonMT.ShowAllHDMuonTra().__len__() - 1]
            maHD = table_row[0] + 1
            self.txtMaHD.setText(str(maHD))
            self.txtTenHD.setText("")
            self.dateNgayMuonHD.setDate(QDate(2024, 6, 22))
            self.cbbDGHD.setCurrentIndex(0)
            self.cbbMNVHD.setCurrentIndex(0)
            self.txtNhanVienLapHoaDon.setText("")
            self.txtTenDocGiaHD.setText("")
            self.check = False
            self.btnAddHD.setText("Lưu")
        else:
            ma = self.txtMaHD.text()
            ten = self.txtTenHD.text()
            ngaymuon = self.dateNgayMuonHD.date().toString("yyyy-MM-dd")
            maDG = self.cbbDGHD.currentText()
            maNV = self.cbbMNVHD.currentText()
            kt = ip.DAL_HoaDonMT.AddHoaDonMuonTra(ma, ten, ngaymuon, maDG, maNV)
            print()
            if kt == 1:
                ip.QMessageBox.information(self, "Thông báo", "Thêm thành công!")
                self.ShowALLHoaDonMT()
                self.SetDefaultHoaDonTxt()
                self.btnAddHD.setText("Thêm")
            else:
                ip.QMessageBox.information(self, "Thông báo", "Thêm không thành công!")


    def on_cbbDGHD_changed(self, index):
        selected_text = self.cbbDGHD.currentText()
        self.txtTenDocGiaHD.setText(ip.DAL_DocGia.SearchMaDocGia(str(selected_text))[0][1]) 
    def on_cbbMNVHD_changed(self, index):
        selected_text = self.cbbMNVHD.currentText()
        self.txtNhanVienLapHoaDon.setText(ip.DAL_NhanVien.SearchMaNhanVien(str(selected_text))[0][1]) 


    def DeleteHoaDon(self):
        txtMaHD = self.txtMaHD.text()
        kt = ip.DAL_HoaDonMT.DeleteHoaDonMuonTra(txtMaHD)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Xóa thành công!")
            self.ShowALLHoaDonMT()
            self.SetDefaultHoaDonTxt()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Xóa không thành công!")


    def UpdateHoaDon(self):
        ma = self.txtMaHD.text()
        ten = self.txtTenHD.text()
        ngaymuon = self.dateNgayMuonHD.date().toString("yyyy-MM-dd")
        maDG = self.cbbDGHD.currentText()
        maNV = self.cbbMNVHD.currentText()

        kt = ip.DAL_HoaDonMT.UpdateHoaDonMuonTra(ma, ten, ngaymuon, maDG, maNV)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "update thành công!")
            self.SetDefaultHoaDonTxt()
            self.ShowALLHoaDonMT()
        else:
            ip.QMessageBox.information(self, "Thông báo", "update không thành công!")

    def SearchHoaDon(self):
        maTenHoadon = self.txtSearchHD.text()
        data = ip.DAL_HoaDonMT.SearchHoaDon(maTenHoadon)
        self.tableHoaDon.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableHoaDon.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableHoaDon.setItem(row_number, column_number, ip.QTableWidgetItem(str(data)))
#endregion ######################### End Hóa Đơn #############################################

#region ##################### Chi tiết hóa đơn ##############################
    def ShowALLCTHoaDonMT(self):
        sum = 0
        self.cbbMHDCTHD.clear()
        self.cbbMaSachCTHD.clear()

        for i in range(ip.DAL_HoaDonMT.ShowAllHDMuonTra().__len__()):
            self.cbbMHDCTHD.addItem(str(ip.DAL_HoaDonMT.ShowAllHDMuonTra()[i][0]))
        
        for i in range(ip.DAL_Sach.showBookAll().__len__()):
            self.cbbMaSachCTHD.addItem(str(ip.DAL_Sach.showBookAll()[i][0]))

        self.tableCTHD.setRowCount(ip.DAL_ChiTietHoaDonMT.ShowAllCTHDMuonTra().__len__())
        self.tableCTHD.setColumnCount(12)
        self.tableCTHD.setHorizontalHeaderLabels(["mã hóa đơn", "Mã độc giả", "Mã nhân viên", "Mã sách",
                                                    "Tên sách", "Tên tác giả", "Giá", "Số lương",
                                                    "Ngày mượn, Ngày trả dự kiến, Ngày trả thực tế", "Trạng thái"])
        table_row = 0
        for row in ip.DAL_ChiTietHoaDonMT.ShowAllCTHDMuonTra():
            self.tableCTHD.setItem(table_row, 0, ip.QTableWidgetItem(str(row[0])))
            for i in ip.DAL_HoaDonMT.ShowAll(str(row[0])):
                self.tableCTHD.setItem(table_row, 1, ip.QTableWidgetItem(str(ip.DAL_HoaDonMT.ShowAll(str(row[0]))[0][3])))
                self.tableCTHD.setItem(table_row, 2, ip.QTableWidgetItem(str(ip.DAL_HoaDonMT.ShowAll(str(row[0]))[0][4])))               
            self.tableCTHD.setItem(table_row, 3, ip.QTableWidgetItem(str(row[1])))
            self.tableCTHD.setItem(table_row, 4, ip.QTableWidgetItem(str(row[2])))
            self.tableCTHD.setItem(table_row, 5, ip.QTableWidgetItem(str(row[3])))
            self.tableCTHD.setItem(table_row, 6, ip.QTableWidgetItem(str(row[4])))
            self.tableCTHD.setItem(table_row, 7, ip.QTableWidgetItem(str(row[5])))
            self.tableCTHD.setItem(table_row, 8, ip.QTableWidgetItem(str(row[6])))
            self.tableCTHD.setItem(table_row, 9, ip.QTableWidgetItem(str(row[7])))
            self.tableCTHD.setItem(table_row, 10, ip.QTableWidgetItem(str(row[8])))
            self.tableCTHD.setItem(table_row, 11, ip.QTableWidgetItem(str(row[9])))
            sum += (row[4] * row[5])
            table_row += 1
        self.txtTongTienCTHD.setText(str(sum))
    def ShowALLCTHoaDonByMaMuonTraMT(self):
        sum = 0
        if self.is_handling_event:
            return

        self.is_handling_event = True

        try:
            selected_text = self.cbbMHDCTHD.currentText()
            for i in ip.DAL_HoaDonMT.ShowAll(str(selected_text)):
                self.txtMADGCTHD.setText(str(i[3]))
                self.txtMNVCTHD.setText(str(i[4]))

            self.tableCTHD.setRowCount(ip.DAL_ChiTietHoaDonMT.SearchAllCTHDByMaMuonTra(str(selected_text)).__len__())
            self.tableCTHD.setColumnCount(12)
            self.tableCTHD.setHorizontalHeaderLabels(["mã hóa đơn", "Mã độc giả", "Mã nhân viên", "Mã sách",
                                                        "Tên sách", "Tên tác giả", "Giá", "Số lương",
                                                        "Ngày mượn, Ngày trả dự kiến, Ngày trả thực tế", "Trạng thái"])
            table_row = 0
            for row in ip.DAL_ChiTietHoaDonMT.SearchAllCTHDByMaMuonTra(str(selected_text)):
                self.tableCTHD.setItem(table_row, 0, ip.QTableWidgetItem(str(row[0])))
                for i in ip.DAL_HoaDonMT.ShowAll(str(row[0])):
                    self.tableCTHD.setItem(table_row, 1, ip.QTableWidgetItem(str(ip.DAL_HoaDonMT.ShowAll(str(row[0]))[0][3])))
                    self.tableCTHD.setItem(table_row, 2, ip.QTableWidgetItem(str(ip.DAL_HoaDonMT.ShowAll(str(row[0]))[0][4])))               
                self.tableCTHD.setItem(table_row, 3, ip.QTableWidgetItem(str(row[1])))
                self.tableCTHD.setItem(table_row, 4, ip.QTableWidgetItem(str(row[2])))
                self.tableCTHD.setItem(table_row, 5, ip.QTableWidgetItem(str(row[3])))
                self.tableCTHD.setItem(table_row, 6, ip.QTableWidgetItem(str(row[4])))
                self.tableCTHD.setItem(table_row, 7, ip.QTableWidgetItem(str(row[5])))
                self.tableCTHD.setItem(table_row, 8, ip.QTableWidgetItem(str(row[6])))
                self.tableCTHD.setItem(table_row, 9, ip.QTableWidgetItem(str(row[7])))
                self.tableCTHD.setItem(table_row, 10, ip.QTableWidgetItem(str(row[8])))
                self.tableCTHD.setItem(table_row, 11, ip.QTableWidgetItem(str(row[9])))
                sum += (row[4] * row[5])
                table_row += 1
        finally:
            self.is_handling_event = False
        
        self.txtTongTienCTHD.setText(str(sum))

    def ShowSachBYMaSach(self):
        if self.is_handling_event:
            return

        self.is_handling_event = True

        try:
            selected_text = self.cbbMaSachCTHD.currentText()
            for i in ip.DAL_Sach.SearchBookByMaSach(str(selected_text)):
                self.txtTenSachCTHD.setText(str(i[1]))
                self.txtTenTGCTHD.setText(str(i[2]))
                self.txtGiaCTHD.setText(str(i[3]))
        finally:
            self.is_handling_event = False


    def tableCTHoaDonMT_Clicked(self, row, column):
        if self.is_handling_event:
            return

        self.is_handling_event = True

        try:
            ngayMuon = ip.QDate.fromString(self.tableCTHD.item(row, 8).text(), "yyyy-MM-dd")
            ngayTra = ip.QDate.fromString(self.tableCTHD.item(row, 10).text(), "yyyy-MM-dd")
            ngayDuKien = ip.QDate.fromString(self.tableCTHD.item(row, 9).text(), "yyyy-MM-dd")

            maHoaDon = self.tableCTHD.item(row, 0).text()
            for i in range(self.cbbMHDCTHD.count()):
                if(maHoaDon == self.cbbMHDCTHD.itemText(i)):
                    self.cbbMHDCTHD.setCurrentIndex(i)

            self.txtMADGCTHD.setText(self.tableCTHD.item(row, 1).text())
            self.txtMNVCTHD.setText(self.tableCTHD.item(row, 2).text())

            maSach = self.tableCTHD.item(row, 3).text()
            for i in range(self.cbbMaSachCTHD.count()):
                if(maSach == self.cbbMaSachCTHD.itemText(i)):
                    self.cbbMaSachCTHD.setCurrentIndex(i)

            self.txtTenSachCTHD.setText(self.tableCTHD.item(row, 4).text())
            self.txtTenTGCTHD.setText(self.tableCTHD.item(row, 5).text())
            self.txtGiaCTHD.setText(self.tableCTHD.item(row, 6).text())
            self.txtSoLuongCTHD.setText(self.tableCTHD.item(row, 7).text())
            self.dateNgayMuonCTHD.setDate(ngayMuon)
            self.dateNgayTraDuKienCTHD.setDate(ngayDuKien)
            if ngayTra.isValid():
                self.dateNgayTraThucTeCTHD.setDate(ngayTra)
            else:
                self.dateNgayTraThucTeCTHD.setDate(QDate(2000, 1, 1))


            trangThai = self.tableCTHD.item(row, 11).text()
            for i in range(self.cbbTrangThaiCTHD.count()):
                if(trangThai == self.cbbTrangThaiCTHD.itemText(i)):
                    self.cbbTrangThaiCTHD.setCurrentIndex(i)
        finally:
            self.is_handling_event = False


    #Thêm sách vào chi tiết hóa đơn
    def AddCTHoaDonMuontra(self):
        if(self.check == True):
            self.ShowALLCTHoaDonByMaMuonTraMT()
            self.txtSoLuongCTHD.setText("")
            self.dateNgayMuonCTHD.setDate(QDate(2024, 6, 22))
            self.dateNgayTraDuKienCTHD.setDate(QDate(2024, 6, 22))
            self.dateNgayTraThucTeCTHD.setDate(QDate(2024, 6, 22))
            self.cbbTrangThaiCTHD.setCurrentIndex(0)
            self.check = False
            self.btnAddHD.setText("Lưu")
        else:
            maHD = self.cbbMHDCTHD.currentText()
            maSach = self.cbbMaSachCTHD.currentText()
            tenSach = self.txtTenSachCTHD.text()
            tenTG = self.txtTenTGCTHD.text()
            Gia = self.txtGiaCTHD.text()
            soLuong = self.txtSoLuongCTHD.text()
            ngayMuon = self.dateNgayMuonCTHD.date().toString("yyyy-MM-dd")
            ngayTraDuKien = self.dateNgayTraDuKienCTHD.date().toString("yyyy-MM-dd")
            ngayTraThucTe = self.dateNgayTraThucTeCTHD.date().toString("yyyy-MM-dd")
            trangThai = self.cbbTrangThaiCTHD.currentText()
            kt = ip.DAL_ChiTietHoaDonMT.AddCTHoaDonMuonTra(maHD, maSach, tenSach, tenTG, Gia, soLuong,
                                                        ngayMuon, ngayTraDuKien, ngayTraThucTe, trangThai)
            if kt == 1:
                ip.QMessageBox.information(self, "Thông báo", "Thêm thành công!")
                self.ShowALLCTHoaDonByMaMuonTraMT()
                self.btnAddHD.setText("Thêm")
            else:
                ip.QMessageBox.information(self, "Thông báo", "Thêm không thành công!")


    def SetDefaultCTHoaDonTxt(self):
        self.txtMADGCTHD.setText("")
        self.txtMNVCTHD.setText("")
        self.txtTenSachCTHD.setText("")
        self.txtTenTGCTHD.setText("")
        self.txtGiaCTHD.setText("")
        self.txtSoLuongCTHD.setText("")
        self.dateNgayMuonCTHD.setDate(QDate(2024, 6, 22))
        self.dateNgayTraDuKienCTHD.setDate(QDate(2024, 6, 22))
        self.dateNgayTraThucTeCTHD.setDate(QDate(2024, 6, 22))
        self.cbbTrangThaiCTHD.setCurrentIndex(0)
        self.check = True

    def DeleteCTHDByMaMuonTraMaSach(self):
        txtMaHoaDon = self.cbbMHDCTHD.currentText()
        txtMaSach = self.cbbMaSachCTHD.currentText()
        kt = ip.DAL_ChiTietHoaDonMT.DeleteCTHDByMaMuontraMaSach(txtMaHoaDon, txtMaSach)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "Xóa thành công!")
            self.ShowALLCTHoaDonByMaMuonTraMT()
            self.SetDefaultCTHoaDonTxt()
        else:
            ip.QMessageBox.information(self, "Thông báo", "Xóa không thành công!")


    #update sản phẩm trong chi tiết hóa đơn
    def UpdateCTHoaDonMuonTra(self):
        maHD = self.cbbMHDCTHD.currentText()
        maSach = self.cbbMaSachCTHD.currentText()
        tenSach = self.txtTenSachCTHD.text()
        tenTG = self.txtTenTGCTHD.text()
        Gia = self.txtGiaCTHD.text()
        soLuong = self.txtSoLuongCTHD.text()
        ngayMuon = self.dateNgayMuonCTHD.date().toString("yyyy-MM-dd")
        ngayTraDuKien = self.dateNgayTraDuKienCTHD.date().toString("yyyy-MM-dd")
        ngayTraThucTe = self.dateNgayTraThucTeCTHD.date().toString("yyyy-MM-dd")
        trangThai = self.cbbTrangThaiCTHD.currentText()
        kt = ip.DAL_ChiTietHoaDonMT.UpdateCTHoaDonMuonTra(maHD, maSach, tenSach, tenTG, Gia, soLuong,
                                                        ngayMuon, ngayTraDuKien, ngayTraThucTe, trangThai)
        if kt == 1:
            ip.QMessageBox.information(self, "Thông báo", "update thành công!")
            self.SetDefaultCTHoaDonTxt()
            self.ShowALLCTHoaDonByMaMuonTraMT()
        else:
            ip.QMessageBox.information(self, "Thông báo", "update không thành công!")
        self.check = True
    
    def SearchCTHoaDonMuonTra(self):
        maTenSach_Muontra = self.txtSearchCTHD.text()
        self.tableCTHD.setRowCount(ip.DAL_ChiTietHoaDonMT.SearchCTHoaDonMuonTra(maTenSach_Muontra).__len__())
        self.tableCTHD.setColumnCount(12)
        self.tableCTHD.setHorizontalHeaderLabels(["mã hóa đơn", "Mã độc giả", "Mã nhân viên", "Mã sách",
                                                    "Tên sách", "Tên tác giả", "Giá", "Số lương",
                                                    "Ngày mượn, Ngày trả dự kiến, Ngày trả thực tế", "Trạng thái"])
        table_row = 0
        for row in ip.DAL_ChiTietHoaDonMT.SearchCTHoaDonMuonTra(str(maTenSach_Muontra)):
            self.tableCTHD.setItem(table_row, 0, ip.QTableWidgetItem(str(row[0])))
            for i in ip.DAL_HoaDonMT.ShowAll(str(row[0])):
                self.tableCTHD.setItem(table_row, 1, ip.QTableWidgetItem(str(ip.DAL_HoaDonMT.ShowAll(str(row[0]))[0][3])))
                self.tableCTHD.setItem(table_row, 2, ip.QTableWidgetItem(str(ip.DAL_HoaDonMT.ShowAll(str(row[0]))[0][4])))               
            self.tableCTHD.setItem(table_row, 3, ip.QTableWidgetItem(str(row[1])))
            self.tableCTHD.setItem(table_row, 4, ip.QTableWidgetItem(str(row[2])))
            self.tableCTHD.setItem(table_row, 5, ip.QTableWidgetItem(str(row[3])))
            self.tableCTHD.setItem(table_row, 6, ip.QTableWidgetItem(str(row[4])))
            self.tableCTHD.setItem(table_row, 7, ip.QTableWidgetItem(str(row[5])))
            self.tableCTHD.setItem(table_row, 8, ip.QTableWidgetItem(str(row[6])))
            self.tableCTHD.setItem(table_row, 9, ip.QTableWidgetItem(str(row[7])))
            self.tableCTHD.setItem(table_row, 10, ip.QTableWidgetItem(str(row[8])))
            self.tableCTHD.setItem(table_row, 11, ip.QTableWidgetItem(str(row[9])))
            table_row += 1

    def PrintCTMuonTratoExcel(self):
        maMuontra = self.cbbMHDCTHD.currentText()
        ip.DAL_ChiTietHoaDonMT.XuatFileCTDHMuonTra(maMuontra)
#endregion ################## Chi tiết hóa đơn ################################



app = QApplication(ip.sys.argv)
widget = ip.QtWidgets.QStackedWidget()
login_f = Login()
widget.addWidget(login_f)
widget.setCurrentIndex(0)
widget.setFixedHeight(436)
widget.setFixedWidth(877)
widget.show()
app.exec()
