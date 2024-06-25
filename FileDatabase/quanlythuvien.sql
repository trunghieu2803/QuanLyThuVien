drop database quanlythuvien;
create database quanlythuvien;
use quanlythuvien;

CREATE TABLE `sach` (
	`masach` INT NOT NULL AUTO_INCREMENT,
	`tensach` VARCHAR(255) NOT NULL,
	`tentg` VARCHAR(255) NOT NULL,
	`gia` FLOAT NOT NULL,
	`soluong` INT NOT NULL,
	PRIMARY KEY(`masach`)
);

-- Tạo bảng 'docgia'
CREATE TABLE `docgia` (
	`madocgia` INT NOT NULL AUTO_INCREMENT,
	`tendocgia` VARCHAR(255) NOT NULL,
	`diachi` VARCHAR(255) NOT NULL,
	`gioitinh` ENUM('Nam', 'Nữ', 'Khác') NOT NULL,
	`sdt` VARCHAR(15) NOT NULL,
	PRIMARY KEY(`madocgia`)
);

-- Tạo bảng 'nhanvien'
CREATE TABLE `nhanvien` (
	`manv` INT NOT NULL AUTO_INCREMENT,
	`tennv` VARCHAR(255) NOT NULL,
	`gioitinh` ENUM('Nam', 'Nữ', 'Khác') NOT NULL,
	`ngaysinh` DATE NOT NULL,
	`diachi` VARCHAR(255) NOT NULL,
	`sdt` VARCHAR(15) NOT NULL,
	`tendangnhap` VARCHAR(255) NOT NULL,
	`matkhau` VARCHAR(255) NOT NULL,
	`chucvu` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`manv`)
);

CREATE TABLE `hdmuontra` (
	`mamuontra` INT NOT NULL AUTO_INCREMENT,
	`tenhdmuontra` VARCHAR(255),
	`ngaymuon` DATE,
	`madocgia` INT,
	`manv` INT,
	PRIMARY KEY(`mamuontra`),
	FOREIGN KEY (`madocgia`) REFERENCES `docgia`(`madocgia`) ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (`manv`) REFERENCES `nhanvien`(`manv`) ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE `ctmuontra` (
	`mamuontra` INT NOT NULL,
	`masach` INT NOT NULL,
	`ngaymuon` DATE NOT NULL,
	`ngaytradukien` DATE,
	`ngaytrathucte` DATE,
	`trangthai` VARCHAR(255),
	PRIMARY KEY(`mamuontra`, `masach`),
	FOREIGN KEY (`mamuontra`) REFERENCES `hdmuontra`(`mamuontra`) ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (`masach`) REFERENCES `sach`(`masach`) ON UPDATE NO ACTION ON DELETE NO ACTION
);


CREATE TABLE `ctmuontra` (
	`mamuontra` INT NOT NULL,
	`masach` INT NOT NULL,
	`tensach` VARCHAR(255) NOT NULL,
	`tentg` VARCHAR(255) NOT NULL,
	`gia` FLOAT NOT NULL,
	`soluong` INT NOT NULL,
	`ngaymuon` DATE NOT NULL,
	`ngaytradukien` DATE,
	`ngaytrathucte` DATE,
	`trangthai` VARCHAR(255),
	PRIMARY KEY(`mamuontra`, `masach`),
	FOREIGN KEY (`mamuontra`) REFERENCES `hdmuontra`(`mamuontra`) ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (`masach`) REFERENCES `sach`(`masach`) ON UPDATE NO ACTION ON DELETE NO ACTION
);



-- Chèn dữ liệu vào bảng `sach`
INSERT INTO `sach` (`tensach`, `tentg`, `gia`, `soluong`) VALUES 
('Sách Giáo Khoa Toán', 'Nguyễn Văn A', 50.0, 100),
('Sách Lịch Sử Việt Nam', 'Trần Văn B', 70.0, 50),
('Sách Văn Học', 'Lê Thị C', 60.0, 80),
('Sách Khoa Học Tự Nhiên', 'Phạm Văn D', 55.0, 90),
('Sách Địa Lý', 'Nguyễn Thị E', 45.0, 60);

-- Chèn dữ liệu vào bảng `docgia`
INSERT INTO `docgia` (`tendocgia`, `diachi`, `gioitinh`, `sdt`) VALUES 
('Nguyễn Văn H', '123 Đường A, TP.HCM', 'Nam', '0901234567'),
('Trần Thị M', '456 Đường B, Hà Nội', 'Nữ', '0902345678'),
('Lê Văn K', '789 Đường C, Đà Nẵng', 'Nam', '0903456789'),
('Phạm Thị N', '101 Đường D, Hải Phòng', 'Nữ', '0904567890'),
('Hoàng Văn P', '202 Đường E, Cần Thơ', 'Nam', '0905678901');

-- Chèn dữ liệu vào bảng `nhanvien`
INSERT INTO `nhanvien` (`tennv`, `gioitinh`, `ngaysinh`, `diachi`, `sdt`, `tendangnhap`, `matkhau`, `chucvu`) VALUES 
('Nguyễn Thị A', 'Nữ', '1990-01-01', '234 Đường F, TP.HCM', '0911234567', 'admin', '123', 'Quản lý'),
('Trần Văn B', 'Nam', '1985-05-05', '567 Đường G, Hà Nội', '0912345678', 'b.tran', 'pass456', 'Thủ thư'),
('Lê Thị C', 'Nữ', '1992-07-07', '890 Đường H, Đà Nẵng', '0913456789', 'c.le', 'pass789', 'Thủ thư'),
('Phạm Văn D', 'Nam', '1988-09-09', '123 Đường I, Hải Phòng', '0914567890', 'd.pham', 'pass101', 'Thủ thư'),
('Hoàng Thị E', 'Nữ', '1995-11-11', '456 Đường J, Cần Thơ', '0915678901', 'e.hoang', 'pass202', 'Thủ thư');

-- Chèn dữ liệu vào bảng `hdmuontra`
INSERT INTO `hdmuontra` (`tenhdmuontra`, `ngaymuon`, `madocgia`, `manv`) VALUES 
('HD01', '2024-06-01', 1, 1),
('HD02', '2024-06-02', 2, 2),
('HD03', '2024-06-03', 3, 3),
('HD04', '2024-06-04', 4, 4),
('HD05', '2024-06-05', 5, 5);

-- Chèn dữ liệu vào bảng `ctmuontra`
INSERT INTO `ctmuontra` (`mamuontra`, `masach`, `tensach`, `tentg`, `gia`, `soluong`, `ngaymuon`, `ngaytradukien`, `ngaytrathucte`, `trangthai`) VALUES 
(1, 1, 'Sách Giáo Khoa Toán', 'Nguyễn Văn A', 50.0, 1, '2024-06-01', '2024-06-15', NULL, 'Đang mượn'),
(1, 2, 'Sách Lịch Sử Việt Nam', 'Trần Văn B', 70.0, 1, '2024-06-01', '2024-06-15', NULL, 'Đang mượn'),
(2, 3, 'Sách Văn Học', 'Lê Thị C', 60.0, 1, '2024-06-02', '2024-06-16', NULL, 'Đang mượn'),
(2, 4, 'Sách Khoa Học Tự Nhiên', 'Phạm Văn D', 55.0, 1, '2024-06-02', '2024-06-16', NULL, 'Đang mượn'),
(3, 5, 'Sách Địa Lý', 'Nguyễn Thị E', 45.0, 1, '2024-06-03', '2024-06-17', NULL, 'Đang mượn'),
(4, 1, 'Sách Giáo Khoa Toán', 'Nguyễn Văn A', 50.0, 1, '2024-06-04', '2024-06-18', NULL, 'Đang mượn'),
(5, 2, 'Sách Lịch Sử Việt Nam', 'Trần Văn B', 70.0, 1, '2024-06-05', '2024-06-19', NULL, 'Đang mượn'),
(5, 3, 'Sách Văn Học', 'Lê Thị C', 60.0, 1, '2024-06-05', '2024-06-19', NULL, 'Đang mượn');


DELIMITER //

CREATE TRIGGER `after_insert_ctmuontra`
AFTER INSERT ON `ctmuontra`
FOR EACH ROW
BEGIN
    DECLARE available_qty INT;

    -- Kiểm tra số lượng sách có đủ để mượn không
    SELECT `soluong` INTO available_qty FROM `sach` WHERE `masach` = NEW.masach;
    
    IF available_qty >= NEW.soluong THEN
        UPDATE `sach` 
        SET `soluong` = `soluong` - NEW.soluong
        WHERE `masach` = NEW.masach;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Không đủ số lượng sách để mượn';
    END IF;
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER `after_delete_ctmuontra`
AFTER DELETE ON `ctmuontra`
FOR EACH ROW
BEGIN
    -- Cập nhật lại số lượng sách trong bảng sach khi xóa bản ghi trong bảng ctmuontra
    UPDATE `sach` 
    SET `soluong` = `soluong` + OLD.soluong
    WHERE `masach` = OLD.masach;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER `before_update_ctmuontra`
BEFORE UPDATE ON `ctmuontra`
FOR EACH ROW
BEGIN
    DECLARE change_amount INT;

    -- Tính toán sự thay đổi số lượng sách
    SET change_amount = NEW.soluong - OLD.soluong;

    -- Nếu số lượng sách tăng lên (NEW.soluong > OLD.soluong), cần giảm số lượng sách trong bảng sach
    IF change_amount > 0 THEN
        IF (SELECT `soluong` FROM `sach` WHERE `masach` = NEW.masach) >= change_amount THEN
            UPDATE `sach`
            SET `soluong` = `soluong` - change_amount
            WHERE `masach` = NEW.masach;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Không đủ số lượng sách để mượn';
        END IF;
    
    -- Nếu số lượng sách giảm đi (NEW.soluong < OLD.soluong), cần tăng số lượng sách trong bảng sach
    ELSEIF change_amount < 0 THEN
        UPDATE `sach`
        SET `soluong` = `soluong` - change_amount -- Trừ đi số âm để cộng thêm số dương
        WHERE `masach` = NEW.masach;
    END IF;
END //

DELIMITER ;
