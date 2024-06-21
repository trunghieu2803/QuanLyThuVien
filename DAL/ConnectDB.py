import pymysql

def connect_db():
    try:
        db = pymysql.connect(host="localhost", user="root", password="123456", database="quanlythuvien")
        return db
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def CheckLogin(tk, mk):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM taikhoan WHERE username = %s AND password = %s", (tk, mk))
    result = cursor.fetchone()
    return result

