drop database quanlythuvien;
create database quanlythuvien;
use quanlythuvien;

-- Tạo bảng 'sach'
CREATE TABLE `sach` (
	`masach` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`tensach` VARCHAR(255),
	`tentg` VARCHAR(255),
	`gia` FLOAT,
	`soluong` INT,
	PRIMARY KEY(`masach`)
);

-- Tạo bảng 'docgia'
CREATE TABLE `docgia` (
	`madocgia` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`tendocgia` VARCHAR(255),
	`diachi` VARCHAR(255),
	`gioitinh` VARCHAR(255),
	`sdt` VARCHAR(255),
	PRIMARY KEY(`madocgia`)
);

-- Tạo bảng 'nhanvien'
CREATE TABLE `nhanvien` (
	`manv` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`tennv` VARCHAR(255),
	`gioitinh` VARCHAR(255),
	`ngaysinh` DATE,
	`diachi` VARCHAR(255),
	`sdt` VARCHAR(255),
	`tendangnhap` VARCHAR(255),
	`matkhau` VARCHAR(255),
	`chucvu` VARCHAR(255),
	PRIMARY KEY(`manv`)
);

-- Tạo bảng 'hoadon'
-- Tạo bảng 'hoadon'
CREATE TABLE `hoadon` (
	`sohd` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`manv` INT,
	`madocgia` INT,
	`ngaymuon` DATE,
    `ngaytra` date,
	PRIMARY KEY(`sohd`),
	FOREIGN KEY (`manv`) REFERENCES `nhanvien`(`manv`)
		ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (`madocgia`) REFERENCES `docgia`(`madocgia`)
		ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Tạo bảng 'cthoadon'
CREATE TABLE `cthoadon` (
	`sohd` INT,
	`masach` INT,
	FOREIGN KEY (`sohd`) REFERENCES `hoadon`(`sohd`)
		ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (`masach`) REFERENCES `sach`(`masach`)
		ON UPDATE NO ACTION ON DELETE NO ACTION
);




-- Không cần thêm các ALTER TABLE vì các FOREIGN KEY đã được khai báo ngay khi tạo bảng.

-- Bảng `sach`
INSERT INTO `sach` (`tensach`, `tentg`, `gia`, `soluong`) VALUES 
('Sách Giáo Khoa Toán', 'Nguyễn Văn A', 50.0, 100),
('Sách Lịch Sử Việt Nam', 'Trần Văn B', 70.0, 50),
('Sách Văn Học', 'Lê Thị C', 60.0, 80),
('Sách Khoa Học Tự Nhiên', 'Phạm Văn D', 55.0, 90),
('Sách Địa Lý', 'Nguyễn Thị E', 45.0, 60);

-- Bảng `docgia`
INSERT INTO `docgia` (`tendocgia`, `diachi`, `gioitinh`, `sdt`) VALUES 
('Nguyễn Văn H', '123 Đường A, TP.HCM', 'Nam', '0901234567'),
('Trần Thị M', '456 Đường B, Hà Nội', 'Nữ', '0902345678'),
('Lê Văn K', '789 Đường C, Đà Nẵng', 'Nam', '0903456789'),
('Phạm Thị N', '101 Đường D, Hải Phòng', 'Nữ', '0904567890'),
('Hoàng Văn P', '202 Đường E, Cần Thơ', 'Nam', '0905678901');

-- Bảng `nhanvien`
INSERT INTO `nhanvien` (`tennv`, `gioitinh`, `ngaysinh`, `diachi`, `sdt`, `tendangnhap`, `matkhau`, `chucvu`) VALUES 
('Nguyễn Thị A', 'Nữ', '1990-01-01', '234 Đường F, TP.HCM', '0911234567', 'admin', '123', 'Quản lý'),
('Trần Văn B', 'Nam', '1985-05-05', '567 Đường G, Hà Nội', '0912345678', 'b.tran', 'pass456', 'Thủ thư'),
('Lê Thị C', 'Nữ', '1992-07-07', '890 Đường H, Đà Nẵng', '0913456789', 'c.le', 'pass789', 'Thủ thư'),
('Phạm Văn D', 'Nam', '1988-09-09', '123 Đường I, Hải Phòng', '0914567890', 'd.pham', 'pass101', 'Thủ thư'),
('Hoàng Thị E', 'Nữ', '1995-11-11', '456 Đường J, Cần Thơ', '0915678901', 'e.hoang', 'pass202', 'Thủ thư');

-- Thêm dữ liệu vào bảng 'hoadon'
INSERT INTO `hoadon` (`manv`, `madocgia`, `ngaymuon`, `ngaytra`) VALUES 
(1, 1, '2024-06-01', '2024-06-10'),
(2, 2, '2024-06-05', '2024-06-10'),
(3, 3, '2024-06-10', '2024-06-15'),
(4, 4, '2024-06-15', '2024-06-20'),
(5, 5, '2024-06-20', '2024-06-25');

-- Thêm dữ liệu vào bảng 'cthoadon'
INSERT INTO `cthoadon` (`sohd`, `masach`) VALUES 
(1, 1),
(1, 2),
(2, 2),
(2, 3),
(3, 3),
(3, 4),
(4, 4),
(4, 5),
(5, 5),
(5, 1);