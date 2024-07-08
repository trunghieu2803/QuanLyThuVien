from . import ConnectDB


def showAllDocGia():
    conn = ConnectDB.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM docgia")
    rows = cursor.fetchall()
    conn.close()
    return rows


def AddDocGia(maDG, tenDocGia, diaChiDG, gioiTinhDG, sdtDG):
    conn = ConnectDB.connect_db()
    cs = conn.cursor()
    qr = "INSERT INTO docgia(maDocGia, tendocgia, DiaChi, GioiTinh, SDT) VALUES(%s, %s, %s, %s, %s)"
    cs.execute(qr, (maDG, tenDocGia, diaChiDG, gioiTinhDG, sdtDG))
    conn.commit()
    conn.close()
    return cs.rowcount


def DeleteDocGia(maDocGia):
    conn = ConnectDB.connect_db()
    cursor = conn.cursor()
    qr = "DELETE FROM docgia WHERE maDocGia = %s"
    cursor.execute(qr, (maDocGia,))
    conn.commit()
    conn.close()
    return cursor.rowcount


def UpdateDocGia(maDocGia, tenDocGia, diaChiDG, gioiTinhDG, sdtDG):
    conn = ConnectDB.connect_db()
    cs = conn.cursor()
    qr = "UPDATE docgia SET tendocgia = %s, DiaChi = %s, GioiTinh = %s, SDT = %s WHERE maDocGia = %s"
    cs.execute(qr, (tenDocGia, diaChiDG, gioiTinhDG, sdtDG, maDocGia))
    conn.commit()
    conn.close()
    return cs.rowcount

def SearchDocGia(maTenDocgia):
    conn = ConnectDB.connect_db()
    qr = "SELECT * FROM Docgia WHERE madocgia LIKE '%"+maTenDocgia+"%' OR tendocgia LIKE '%"+maTenDocgia+"%';"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def SearchMaDocGia(maDocGia):
    conn = ConnectDB.connect_db()
    qr = "SELECT * FROM Docgia WHERE madocgia LIKE '%"+maDocGia+"%'"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

import openpyxl
def XuatFileDocGia():
    conn = ConnectDB.connect_db()
    cs = conn.cursor()
    qr = "SELECT * FROM DocGia"
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(["Mã độc giả", "Tên độc giả", "Địa chỉ", "Giới tính", "Số điện thoại"])
    for row in rs:
        ws.append(row)

    wb.save('DanhSachDocGia.xlsx')