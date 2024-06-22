from . import ConnectDB

def showALLNhanVien():
    conn = ConnectDB.connect_db()
    qr = r"SELECT * FROM nhanvien"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def AddNhanVien(maNV, tenNV, gioiTinh, ngaySinh, diaChi, soDT, tenDangNhap, matKhau, chucVu):
    conn = ConnectDB.connect_db()
    qr = r"INSERT INTO nhanvien (maNV, tenNV, gioiTinh, ngaySinh, diaChi, sdt, tenDangNhap, matKhau, chucVu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cs = conn.cursor()
    cs.execute(qr, (maNV, tenNV, gioiTinh, ngaySinh, diaChi, soDT, tenDangNhap, matKhau, chucVu))
    conn.commit()
    conn.close()
    return cs.rowcount


def DeleteNhanVien(maNV):
    conn = ConnectDB.connect_db()
    qr = r"DELETE FROM nhanvien WHERE maNV = %s"
    cs = conn.cursor()
    cs.execute(qr, (maNV,))
    conn.commit()
    conn.close()
    return cs.rowcount


def UpdateNhanVien(maNV, tenNV, gioiTinh, ngaySinh, diaChi, soDT, tenDangNhap, matKhau, chucVu):
    conn = ConnectDB.connect_db()
    qr = r"UPDATE nhanvien SET tenNV = %s, gioiTinh = %s, ngaySinh = %s, diaChi = %s, sdt = %s, tenDangNhap = %s, matKhau = %s, chucVu = %s WHERE maNV = %s"
    cs = conn.cursor()
    cs.execute(qr, (tenNV, gioiTinh, ngaySinh, diaChi, soDT, tenDangNhap, matKhau, chucVu, maNV))
    conn.commit()
    conn.close()
    return cs.rowcount

def SearchNhanVien(maTenNhanvien):
    conn = ConnectDB.connect_db()
    qr = "SELECT * FROM nhanvien WHERE maNV LIKE '%"+maTenNhanvien+"%' OR tenNV LIKE '%"+maTenNhanvien+"%';"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

import openpyxl
def XuatFileNhanVien():
    conn = ConnectDB.connect_db()
    cs = conn.cursor()
    qr = "SELECT * FROM nhanvien"
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(["Mã nhân viên", "Tên nhân viên", "Giới tính", "Ngày sinh",
                        "Địa chỉ", "Số điện thoại", "tên đăng nhập", "Mật khẩu", "Chức Vụ"])
    for row in rs:
        ws.append(row)

    wb.save('DanhSachNhanVien.xlsx')