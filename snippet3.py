class LoggerContext:
    def __init__(self, log_filename):
        self.log_filename = log_filename
    
    def context_generator(self):
        self.file = open(self.log_filename, "a", encoding="utf-8")
        self.file.write("📌 Bắt đầu xử lý dữ liệu học sinh\n")
        print("🔓 Mở file log")
        try:
            yield self.file  # Trả file để sử dụng trong with
        finally:
            self.file.write("✅ Kết thúc xử lý\n")
            self.file.close()
            print("🔒 Đóng file log")

    def __enter__(self):
        self.context = self.context_generator()
        return next(self.context)

    def __exit__(self, exc_type, exc_value, traceback):
        next(self.context, None)

# 🧪 Sử dụng context manager để ghi log khi xử lý dữ liệu
with LoggerContext("log.txt") as log_file:
    log_file.write("📥 Đang đọc dữ liệu học sinh...\n")
    log_file.write("🎓 Phân tích xong danh sách học sinh giỏi.\n")
