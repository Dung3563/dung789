import os, math, time, sys, random,datetime
d = '\x1b[1;91m'
xl = '\x1b[1;92m'
v = '\x1b[1;93m'
xb = '\x1b[1;96m'
t = '\x1b[1;97m'
h = '\x1b[1;95m'
def write(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)
def load():
	kha = ['.   ','..  ','... ']
	for o in kha:
		print("\r\033[1;97m[\033[1;96m*\033[1;97m] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
def key():
  key = input('[!]Nhập key của bạn: ')
  if key == '':
    print("[!]Sai key")
    os.system('clear')
  elif key == 'niemphong':
    print("key đúng")
  else:
    print("Key sai")
    os.system.exit()
def key1():
  key = input('[!]Nhập key của bạn: ')
  if key == '':
    print("[!]Sai key")
    os.system('clear')
  elif key == 'axeyed kha' or key == 'Axeyed kha':
    print("key đúng")
  else:
    print("Key sai")
    os.system.exit()
money = 30000
f = "\033[1;97m------------------------------------------------------------"
banner = """
\033[1;96m██████╗  [•] Copyright Axeyed Kha (có của Dũng nữa :))
\033[1;92m██╔══██╗ [•] Tool tính đủ thứ trên đời :v
\033[1;95m██║  ██║ [•] Facebook: Dũng Dũng
\033[1;92m██║  ██║ [•] Phiên bản v1.0
\033[1;96m██████╔╝ [•] Zalo: 0936485851
\033[1;97m╚═════╝  [•] Chúc các bạn dùng tool vui vẻ
"""
banhang = """

 ____________________________________________
|############################################|
|#|                           |##############|
|#|  =====  ..--''`  |~~``|   |##|````````|##|
|#|  |   |  \     |  :    |   |##| Exact  |##|
|#|  |___|   /___ |  | ___|   |##| Change |##|
|#|  /=__\  ./.__\   |/,__\   |##| Only   |##|
|#|  \__//   \__//    \__//   |##|________|##|
|#|===========================|##############|
|#|```````````````````````````|##############|
|#| =.._      +++     //////  |##############|
|#| \/  \     | |     \    \  |#|`````````|##|
|#|  \___\    |_|     /___ /  |#| _______ |##|
|#|   / __\\  /|_|\   // __\   |#| |1|2|3| |##|
|#|  \__//-  \|_//   -\__//   |#| |4|5|6| |##|
|#|===========================|#| |7|8|9| |##|
|#|```````````````````````````|#| ``````` |##|
|#| ..--    ______   .--._.   |#|[=======]|##|
|#| \   \   |    |   |    |   |#|  _   _  |##|
|#|  \___\  : ___:   | ___|   |#| ||| ( ) |##|
|#|  / __\  |/ __\   // __\   |#| |||  `  |##|
|#|  \__//   \__//  /_\__//   |#|  ~      |##|
|#|===========================|#|_________|##|
|#|```````````````````````````|##############|
|############################################|
|#|||||||||||||||||||||||||||||####```````###|
|#||||||||||||PUSH|||||||||||||####\|||||/###|
|############################################|
\\\\\\\\\\\\\\\\\\\\\\///////////////////////
 |________________________________|CR98|___|
"""
def main():
  os.system('clear')
  write(banner)
  write(xl+'Chào mừng bạn đến với hệ thống tính điểm trung bình.')
  write(f)
  load()
  menu()
def yn():
  write(f)
  cnbn = input('Bạn có muốn quay về lại menu không? [y/n] :')
  if cnbn == 'y' or cnbn == 'Y':
    menu()
  elif cnbn == 'n' or cnbn == 'N':
    print('\033[1;96m Cám ơn bạn đã sử dụng công cụ của tôi')
    os.sys.exit()
  else:
    print(d+'[!] Nhập sai')
    os.sys.exit()
def menu():
  os.system('clear')
  write(banner)
  write(f)
  write(t+'['+xl+'1'+t+'] Tính phương trình bậc 2')
  write(t+'['+xl+'2'+t+'] Tính điểm trung bình 2 môn')
  write(t+'['+xl+'3'+t+'] Tính điểm trung bình 3 môn')
  write(t+'['+xl+'4'+t+'] Tính điểm trung bình 4 môn')
  write(t+'['+xl+'5'+t+'] Tính điểm trung bình 5 môn')
  write(t+'['+xl+'6'+t+'] Tính điểm trung bình 6 môn')
  write(t+'['+xl+'7'+t+'] Tính điểm trung bình 7 môn')
  write(t+'['+xl+'8'+t+'] Tính điểm trung bình 8 môn')
  write(t+'['+xl+'9'+t+'] Tính điểm trung bình 9 môn')
  write(t+'['+xl+'10'+t+'] Tính điểm trung bình 10 môn')
  write(t+'['+xl+'11'+t+'] Tính điểm trung bình 11 môn')
  write(t+'['+xl+'12'+t+'] Tính điểm trung bình 12 môn')
  write(t+'['+xl+'13'+t+'] Tính điểm trung bình 13 môn')
  write(t+'['+xl+'14'+t+'] Random đáp án trắc nghiệm')
  write(t+'['+xl+'15'+t+'] Tính xác suất(premium :)))')
  write(t+'['+xl+'16'+t+'] tính điểm trắc nghiệm 30 câu(update)  ')
  print(f) 
  write(t+'['+xl+'20'+t+'] Game oẳn tù tì(búa bao kéo)')
  write(t+'['+xl+'21'+t+'] Game tập tầm vông(đại loại vậy :) vì chưa biết vùng khác tên là gì ')
  print(f)
  write(t+'['+xl+'30'+t+'] Góc tool xịn xò(Đang update) ')
  print(f) 
  write(t+'['+h+'khu shopping'+t+']') 
  write(t+'['+xl+'31'+t+'] sờ nách :))')
  write(t+'['+xl+'32'+t+'] Nước') 
  write(t+'['+xl+'33'+t+'] Bánh') 
  print(f) 
  write(t+'['+xl+'40'+t+'] Góc cho người hệ tâm linh :))) (Niêm phong vì không còn thiêng như nếu muốn thử thì ib Dũng để đc thử) ')
  print(f) 
  q = input(t+'[?] Nhập lựa chọn của bạn: '+xl)
  if q == '1' or q == '01':
    k1()
  elif q == '2' or q == '02':
    k2()
  elif q == '3' or q == '03':
    k3()
  elif q == '4' or q == '04':
    k4()
  elif q == '5' or q == '05':
    k5()
  elif q == '6' or q == '06':
    k6()
  elif q == '7' or q == '07':
    k7()
  elif q == '8' or q == '08':
    k8() 
  elif q == '9' or q == '09':
    k9()
  elif q == '10' or q == '10':
    k10()
  elif q == '11' or q == '11':
    k11()
  elif q == '12' or q == '12':
    k12()
  elif q == '13' or q == '13':
    k13()
  elif q == '14' or q == '14':
    k14()
  elif q == '15' or q == '15':
    k15()
  elif q == '16' or q == '16':
    k16()
  elif q == '20' or q == '20':
    k20()
  elif q == '21' or q == '21':
    k21()
  elif q == '30' or q == '30':
    k30()
  elif q == '31' or q == '31':
    k31()
  elif q == '32' or q == '32':
    k31()
  elif q == '33' or q == '33':
    k31()
  elif q == '40' or q == '40':
    k40()
  else:
        print(d+'[!] Nhập Sai')
        os.sys.exit()
def k1():
  print("\033[1;97mGiải phương trình bậc 2\n")
  print("phương trình bậc  2 có dạng L: aX^2 + bx +c = 0\n")
  print("mời bạn nhập \n")
  time.sleep(1)
  a = float(input("a = "))
  b = float(input("b = "))
  c = float(input("c = "))
  if(a==0):
    a = float(input("bạn đã nhập sai , nhập lại ! .a = "))
  dental = b*b - 4*a*c
  if(dental < 0 ):
    print("phương trình vô nghiệm\n")
  elif(dental > 0):
    x1 = (-b + math.sqrt(dental))/(2*a)
    x2 = (-b - math.sqrt(dental))/(2*a)
    print("phương trình có 2 nghiệm x1 ="+ str(x1) + " và "+" x2 = " +str(x2))
  else:
    x = -b/(2*a)
    print("phương trình có 2 nghiệm x1 = x2 = " + str(x))
  yn()
def k2():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  write(f)
  re = (k+kk)/2
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k3():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  re = (k+kk+kkk)/3
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k4():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  re = (k+kk+kkk+kkkk)/4
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k5():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk)/5
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k6():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk)/6
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k7():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk)/7
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k8():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk)/8
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k9():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nhập điểm môn thứ 9 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk)/9
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k10():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nhập điểm môn thứ 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nhập điểm môn thứ 10 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk)/10
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k11():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nhập điểm môn thứ 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nhập điểm môn thứ 10 :'))
  write(f)
  kkkkkkkkkkk = float(input('Nhập điểm môn thứ 11 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk+kkkkkkkkkkk)/11
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k12():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nhập điểm môn thứ 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nhập điểm môn thứ 10 :'))
  write(f)
  kkkkkkkkkkk = float(input('Nhập điểm môn thứ 11 :'))
  write(f)
  kkkkkkkkkkkk = float(input('Nhập điểm môn thứ 12 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk+kkkkkkkkkkk+kkkkkkkkkkkk)/12
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k13():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nhập điểm môn thứ 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nhập điểm môn thứ 10 :'))
  write(f)
  kkkkkkkkkkk = float(input('Nhập điểm môn thứ 11 :'))
  write(f)
  kkkkkkkkkkkk = float(input('Nhập điểm môn thứ 12 :'))
  write(f)
  kkkkkkkkkkkkk = float(input('Nhập điểm môn thứ 13 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk+kkkkkkkkkkk+kkkkkkkkkkkk+kkkkkkkkkkkkk)/13
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k14():
  os.system('clear')
  write(banner)
  print("tool random đáp án trắc nghiệm")
  write('\033[1;91m[!]Lưu ý: tool chỉ mang tính chất giải trí, không phục vụ mục đích học tập')
  write('\033[1;97m[•]Mong các bạn đạt điểm cao trong bài ktra nhaaa :3')
  write(f) 
  suits = ["A", "B", "C", "D"]
  dem=0
  keep_going = True 
  while keep_going:  
       j=datetime.datetime.now().strftime("%X")
       dem=dem+1
       my_suit = random.choice(suits)
       load()
       time.sleep(0.5)
       write(f'\x1b[1;93m[{dem}] >\x1b[1;92m{j} >\x1b[1;96m"Đáp án là" >\x1b[1;94m'+ my_suit)
       answer = input("[•]Muốn tiếp tục random thì bấm Enter, nếu không thì bấm quit: ") 
       keep_going = (answer == "")
       if answer == "quit" or answer == "Quit":
          os.system('clear')
          os.sys.exit()
def k15():
  os.system('clear')
  print(banner) 
  print(f) 
  write('[!]Tool sẽ tính số cách xảy ra với trường hợp bạn đưa ra')
  a = float(input('[•]Nhập số đơn vị có trong bài(vd: người, quả...): '))
  if a == '3':
    print('tool chưa xong đâu :(( thông cảm nha ')
def k16():
  os.system('clear')
  print(banner) 
  
def k20():
  os.system('clear') 
  write(banner)
  print(f) 
  write('trò chơi này tên là oẳn tù tì (búa bao kéo)')

  choices = ["búa", "lá", "kéo"] 
  write('búa thắng kéo. kéo thắng lá. lá thắng búa.')
  player = input("bạn chọn búa, lá hay kéo (or quit)? ") 
  while player != "quit":           
    player = player.lower()   
    computer = random.choice(choices)   
    print("Bạn chọn " +player+ ", và tôi chọn " +computer+ ".") 
    if player == computer: 
        print("hòa rồi!") 
    elif player == "búa":  
        if computer == "kéo":
            print("bạn thắng rồi, chúc mừng <3!")  
        else:  
            print("tôi win rồi, bạn thua!")
    elif player == "lá":  
        if computer == "búa":
            print("bạn thắng rồi!") 
        else: 
            print("tôi thắng rồi, bạn thua!") 
    elif player == "kéo": 
        if computer == "lá": 
            print("bạn thắng rồi!") 
        else: 
            print("tôi thắng rồi, bạn thua!") 
    else: 
        print("tôi nghĩ có j đó sai rồi, báo cho chủ nhân tôi với nhé ")
    print()                             
    player = input("bạn muốn chơi với tôi tiếp không (or quit)? ") 
def k21():
  os.system('clear')
  print(banner)
  write(f)
  write('LUẬT: có 2 ô(ô 1 và ô 2) và phải chọn đúng ô với máy chọn')
  o = ['1 ',' 2']
  keep_going = True 
  while keep_going:  
    my_o = random.choice(o)
    write('tập tầm vông....')
    a = int(input('[?]Chọn ô đúng?: '))
    time.sleep(3)
    if a == my_o:
      write('[√]Bạn thắng rồi')
    else:
      write('[!]Thua r :(((')
      q = input('Bạn muốn chơi lại không?: ')
      if q == 'n' or q == 'N':
        os.system.exit()
        yn()
def k30():
  key1()
  os.system('clear')
  print(banner) 
  write('Happy Birthday: ')
  write('[√]Mình không có gì nhiều...chỉ có cái tool này để chúc sinh nhật bạn ')
  yn()
def k31():
  os.system('clear')
  print(banner) 
  print(f)
  write(banhang) 
  write('Đồ của bạn đây, chúc ngon miệng :))')
  a = input('bạn muốn ăn nhẹ hay ăn kiểu chết đói(nhẹ/đói): ')
  if a == 'nhẹ' or a == 'Nhẹ':
    write('nhăm nhăm :)))')
  elif a == 'Đói' or a == 'đói':
    write('nhoàm nhoàm, ăn lòi l')
  else:
      print(d+"[!]Nhập sai")
      os.system.exit()
  yn()
def k32():
  os.system('clear')
  print(banner) 
  print(f)
  write(banhang) 
  write('Đồ của bạn đây, chúc ngon miệng :))')
  yn()
def k33():
  os.system('clear')
  print(banner) 
  print(f)
  write(banhang) 
  write('Đồ của bạn đây, chúc ngon miệng :))')
  a = input('bạn muốn ăn nhẹ hay ăn kiểu chết đói(nhẹ/đói) :)')
  if a == 'nhẹ' or a == 'Nhẹ':
    write('nhăm nhăm :)))')
  elif a == 'Đói' or a == 'đói':
    write('nhoàm nhoàm, ăn lòi l')
  else:
      print(d+"[!]Nhập sai")
      os.system.exit()
  yn()
def k40():
  key()
  os.system('clear')
  write('[!]Lưu ý: tool chỉ mang tính chất giải trí và không có mục đích xúc phải 1 cá nhân hay 1 tổ chức nào đó.')
  phat = """
                       \033[1;93m      _`			
                          _ooOoo_				
                         o8888888o				
                         88" . "88				
                         (| -_- |)				
                         O\  =  /O				
                      ____/`---'\____				
                    .'  \\|     |//  `.			
                   /  \\|||  :  |||//  \			
                  / _||||| -:- |||||_  \			
                  |   | \\\  -  /'| |   |			
                  | \_|  `\`---'//  |_/ |			
                  \  .-\__ `-. -'__/-.  /			
                ___`. .'  /--.--\  `. .'___			
             ."" '<  `.___\_<|>_/___.' _> \"".			
            | | :  `- \`. ;`. _/; .'/ /  .' ; |		
            \  \ `-.   \_\_`. _.'_/_/  -' _.' /		
=============`-.`___`-.__\ \___  /__.-'_.'_.-'=================
                           `=--=-'                    



          _.-/`)
         // / / )
      .=// / / / )
     //`/ / / / /
    // /     ` /
   ||         /
    \\       /
     ))    .'
    //    /
         /"""
  write(phat) 
  uoc = input("\033[1;97mHãy ước điều bạn muốn: ")
  write('mong bạn 1 ngày tốt lành <3')
  write('Và điều ước sẽ tới với bạn')
  yn()

#################################################################
#                             _`				#
#                          _ooOoo_				#
#                         o8888888o				#
#                         88" . "88				#
#                         (| -_- |)				#
#                         O\  =  /O				#
#                      ____/`---'\____				#
#                    .'  \\|     |//  `.			#
#                   /  \\|||  :  |||//  \			#
#                  /  _||||| -:- |||||_  \			#
#                  |   | \\\  -  /'| |   |			#
#                  | \_|  `\`---'//  |_/ |			#
#                  \  .-\__ `-. -'__/-.  /			#
#                ___`. .'  /--.--\  `. .'___			#
#             ."" '<  `.___\_<|>_/___.' _> \"".			#
#            | | :  `- \`. ;`. _/; .'/ /  .' ; |		#
#            \  \ `-.   \_\_`. _.'_/_/  -' _.' /		#
#=============`-.`___`-.__\ \___  /__.-'_.'_.-'=================#
    #                       `=--=-'                    
   
#Làm ơn đấy, sửa lần 34 rồi :))
#Tâm linh vaicut, ghép cái này vào chạy phát ok luôn :))
  #        _.-/`)
   #      // / / )
  #    .=// / / / )
  #   //`/ / / / /
 #   // /     ` /
 #  ||         /
  #  \\       /
   #  ))    .'
   # //    /
    #     /
main()
