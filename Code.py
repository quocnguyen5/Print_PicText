import time as t
from time import sleep
print()
print()

note_1 = "** Hello! My name is NguyenDepTrai\n"
note_2 = "** Hello em tui :DDD.\n*****\n****\n***\n**\n*\n"

for c in note_1 + note_2:
    print(c, end='', flush=True)
    sleep(0.05)  # Chỉnh sửa thông số, tốc độ load của note.
print()

input('>> Nhập họ và tên của người yêu bạn:\n')
input('>> Nhập sai họ tên của người yêu rồi, NHẬP LẠI:\n')
print()

note_1 = "*                       Tuyệt Vời - Tèn tennnnnn"
print()
for c in note_1:
    print(c, end='', flush=True)
    sleep(0.03)  # tốc độ của từ "Tuyệt Vời - Khó Thế Mà Cũng Nhớ Ra Được"
print()

countdown = range(10, 110, +10)
for i in range(len(countdown)):
    print("*                       Đang xử lý: ", countdown[i], end="")
    print("%")
    t.sleep(0.5)  # Tốc độ loading khi bắt đầu xử lý loading 10 -> 100%
print("*                       Hoàn tất....")

# "PicText.txt" là file chứa text-image đã tạo.
with open("PicText.txt", "r") as fh:
    for line in fh:
        print(line.strip())
        t.sleep(0.1)  # Chỉnh sửa thông số thay đổi Tốc độ load của hình ảnh
