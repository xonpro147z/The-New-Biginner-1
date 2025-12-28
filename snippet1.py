class GhiLog:
    def __init__(self, filename):
        self.filename = filename
    #self là đại diện chính cho đối tượng object giúp lưu trữ và truy cập dữ liệu
    def __enter__(self):
        self.file = open(self.filename, "a", encoding="utf-8")
        self.file.write("📌 Bắt đầu xử lý\n")
        print("🔓 Đã mở file log")
        return self.file  # Trả về file để sử dụng trong khối with

    def __exit__(self, exc_type, exc_value, traceback): #(loại lỗi, giá trị lỗi, nơi lỗi xảy ra)
        self.file.write("✅ Kết thúc xử lý\n")
        self.file.close()
        print("🔒 Đã đóng file log")

# Sử dụng context manager để ghi log vào file
with GhiLog("log.txt") as log_file:
    log_file.write("📥 Đang xử lý dữ liệu học sinh...\n")
    log_file.write("🎓 Đã cập nhật điểm thi.\n")
