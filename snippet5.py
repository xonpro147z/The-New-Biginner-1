import os
import csv
from datetime import datetime

# 🎯 Decorator ghi log và bắt lỗi
def log_and_error_handling(func):
    def wrapper(*args, **kwargs):
        log_file = "activity.log"
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"\n🕒 {datetime.now()} - Gọi hàm: {func.__name__} với args: {args}, kwargs: {kwargs}\n")
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            with open(log_file, "a", encoding="utf-8") as log:
                log.write(f"❌ Lỗi: {e}\n")
            print("⚠️ Lỗi: File không tồn tại!")
        except Exception as e:
            with open(log_file, "a", encoding="utf-8") as log:
                log.write(f"❌ Lỗi không xác định: {e}\n")
            print("⚠️ Đã xảy ra lỗi:", e)
    return wrapper

# 📊 Hàm đọc điểm học sinh từ file CSV
@log_and_error_handling
def read_student_scores(filename):
    scores = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            scores.append((row["ten"], float(row["diem_tb"])))
    return scores

# 🧪 Gọi thử hàm
data = read_student_scores("diem.csv")
if data:
    print("🎓 Học sinh có điểm trung bình:")
    for name, score in data:
        print(f"👉 {name}: {score}")
