import os, math, time 
f = "--------------------------------------------------------------------"
os.system('clear')
import os 
banner = """
\033[1;95m██████╗ ████████╗██████╗
██╔══██╗╚══██╔══╝██╔══██╗
██║  ██║   ██║   ██████╔╝
██║  ██║   ██║   ██╔══██╗
██████╔╝   ██║   ██████╔╝
╚═════╝    ╚═╝   ╚═════╝"""
print(f)
print('Chào mừng bạn tới tool tính điểm trung bình các môn của bạn.') 
print('Chúc các bạn có 1 học kỳ thật tốt và không bị mẹ chửi :)')
print(f) 
print("[*] Hệ thống sẽ vào sau ít giây nữa...")
time.sleep(5)
os.system('clear')

import os 
banner = """
\033[1;95m██████╗ ████████╗██████╗
██╔══██╗╚══██╔══╝██╔══██╗
██║  ██║   ██║   ██████╔╝
██║  ██║   ██║   ██╔══██╗
██████╔╝   ██║   ██████╔╝
╚═════╝    ╚═╝   ╚═════╝"""
print(f) 
print("""
[√] Cảm ơn bạn đã dùng tool của mình
[•] Bắt đầu tính thôi
""")
print(f) 
a = int(input('nhập điểm môn Toán : '))
b = int(input('nhập điểm môn Văn : '))
c = int(input('nhập điểm môn Anh : '))
d = int(input('nhập điểm môn Hóa : '))
e = int(input('Nhập điểm môn Sinh : '))
f = int(input('Nhập điểm môn Lý : '))
g = int(input('Nhập điểm môn Sử : '))
h = int(input('Nhập điểm môn Địa : '))
re = (a+b+c+d+e+f+g+h)/8
print("[√] Kết quả sẽ có sau 3 giây nữa... ")
time.sleep(3)
print('Điểm Trung Bình của bạn là: %.2f'%re)
print('[√]Cảm ơn bạn đã sử dụng công cụ tính điểm trung bình của mình ạ')
print("Hệ Thống sẽ tự thoát sau 3 giây")
print(f) 
time.sleep(3)
os.system('clear') 