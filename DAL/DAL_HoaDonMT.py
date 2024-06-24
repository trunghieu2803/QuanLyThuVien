from . import ConnectDB

def ShowAllHDMuonTra():
    conn = ConnectDB.connect_db()
    cs = conn.cursor()
    qr = "SELECT * FROM hdmuontra"
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs

def AddHoaDonMuonTra(maMuonTra, tenHdMuonTra, ngayMuon, maDocGia, maNV):
    conn = ConnectDB.connect_db()
    qr = r"INSERT INTO hdmuontra (mamuontra, tenhdmuontra, ngaymuon, madocgia, manv) VALUES (%s, %s, %s, %s, %s)"
    data = (maMuonTra, tenHdMuonTra, ngayMuon, maDocGia, maNV)
    cs = conn.cursor()
    cs.execute(qr, data)
    conn.commit()
    conn.close()
    return cs.rowcount

def DeleteHoaDonMuonTra(maMuonTra):
    conn = ConnectDB.connect_db()
    qr = r"DELETE FROM hdmuontra WHERE mamuontra = %s"
    data = (maMuonTra,)
    cs = conn.cursor()
    cs.execute(qr, data)
    conn.commit()
    conn.close()
    return cs.rowcount


def UpdateHoaDonMuonTra(maMuonTra, tenHdMuonTra, ngayMuon, maDocGia, maNV):
    conn = ConnectDB.connect_db()
    qr = r"UPDATE hdmuontra SET tenhdmuontra = %s, ngaymuon = %s, madocgia = %s, manv = %s WHERE mamuontra = %s"
    data = (tenHdMuonTra, ngayMuon, maDocGia, maNV, maMuonTra)
    cs = conn.cursor()
    cs.execute(qr, data)
    conn.commit()
    conn.close()
    return cs.rowcount

def SearchHoaDon(maTenMuonTra):
    conn = ConnectDB.connect_db()
    qr = "SELECT * FROM hdmuontra WHERE mamuontra LIKE '%"+maTenMuonTra+"%' OR tenhdmuontra LIKE '%"+maTenMuonTra+"%';"
    cs = conn.cursor()
    cs.execute(qr)
    rs = cs.fetchall()
    conn.close()
    return rs


def ShowAll(maMuonTra):
    conn = ConnectDB.connect_db()
    qr = "SELECT * FROM hdmuontra WHERE mamuontra = %s"
    data = (maMuonTra,)
    cs = conn.cursor()
    cs.execute(qr, data)
    rs = cs.fetchall()
    conn.close()
    return rs

