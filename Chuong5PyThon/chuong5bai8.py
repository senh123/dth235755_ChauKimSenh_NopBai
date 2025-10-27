import os

def LayTenFile(duongdan):
    return os.path.basename(duongdan)

def LayTenBaiHat(duongdan):
    return os.path.splitext(os.path.basename(duongdan))[0]

path = input("Nhập đường dẫn file nhạc: ")
print("Tên file:", LayTenFile(path))
print("Tên bài hát:", LayTenBaiHat(path))
