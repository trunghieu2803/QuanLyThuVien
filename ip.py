from DAL import ConnectDB
from DAL import DAL_Sach
from DAL import DAL_NhanVien
from DAL import DAL_DocGia
from DAL import DAL_HoaDonMT
from DAL import DAL_ChiTietHoaDonMT
from PyQt6 import  QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import QDate
import sys
import mysql.connector as db
glchucvu = ""
checkChucVu = True