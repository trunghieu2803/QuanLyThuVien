from . import ConnectDB

def showBookAll():
    conn = ConnectDB.connect_db()
    qr = r"SELECT * FROM quanlythuvien.sach WHERE masach LIKE '%%'"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def UpdateBook(maSach, tenSach, tenTG, gia, soLuong):
    try:
        conn = ConnectDB.connect_db()
        cs = conn.cursor()
        new_GV = (tenSach, tenTG, gia, soLuong, maSach)
        qr = "UPDATE sach SET tensach = %s, tenTG = %s, gia = %s, soluong = %s WHERE masach = %s"
        cs.execute(qr, new_GV)
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0
    
def AddBook(masach, tensach, tentacgia, gia, soluong):
    try:
        conn = ConnectDB.connect_db()
        cs = conn.cursor()
        new_GV = (masach, tensach, tentacgia, gia, soluong)
        qr = "INSERT INTO sach (masach, tensach, tenTG, gia, soluong) values ( %s, %s, %s, %s, %s)"
        cs.execute(qr, new_GV)
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0
    
def DeleteBook(masach):
    try:
        conn = ConnectDB.connect_db()
        cs = conn.cursor()
        qr = "DELETE FROM sach WHERE masach = %s"
        cs.execute(qr, (masach,))
        kt = conn.commit()
        conn.close()
        return cs.rowcount
    except:
        return 0

def SearchBook(matenSach):
    conn = ConnectDB.connect_db()
    qr = "SELECT * FROM sach WHERE masach LIKE '%"+matenSach+"%' OR tensach LIKE '%"+matenSach+"%';"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def SearchBookByMaSach(masach):
    conn = ConnectDB.connect_db()
    qr = "SELECT * FROM sach WHERE masach = %s"
    cs = conn.cursor()
    cs.execute(qr, (masach,))
    rs = cs.fetchall()
    conn.close()
    return rs

import openpyxl
def XuatFileBook():
    conn = ConnectDB.connect_db()
    cs = conn.cursor()
    qr = "SELECT * FROM sach"
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(['Mã sách', 'Tên sách', 'Tên tác giả', 'Giá', 'Số lượng'])
    for row in rs:
        ws.append(row)

    wb.save('DanhSachSach.xlsx')