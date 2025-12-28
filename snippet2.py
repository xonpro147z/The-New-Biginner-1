import csv

class GhiLog:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "a", encoding="utf-8")
        self.file.write("📌 Bắt đầu xử lý\n")
        print("🔓 Đã mở file log")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.write("✅ Kết thúc xử lý\n")
        self.file.close()
        print("🔒 Đã đóng file log")

# Đọc và phân tích học sinh có điểm trung bình > 8.0
with GhiLog("log.txt") as log_file:
    try:
        with open("diem.csv", "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            log_file.write("📊 Đang phân tích dữ liệu điểm trung bình học sinh...\n")
            print("🎓 Học sinh có điểm trung bình > 8.0:")

            for row in reader:
                try:
                    diem = float(row["diem_tb"])
                    if diem >= 8.0:
                        print(f"👉 {row['ten']} ({diem})")
                        log_file.write(f"✅ {row['ten']} có điểm {diem} > 8.0\n")
                except ValueError:
                    log_file.write(f"⚠️ Lỗi chuyển đổi điểm: {row}\n")

    except FileNotFoundError:
        print("❌ Không tìm thấy file 'diem.csv'")
        log_file.write("❌ Không tìm thấy file 'diem.csv'\n")
