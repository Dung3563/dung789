import os, math, time, sys
d = '\033[1;91m'
xl = '\033[1;92m'
v = '\033[1;93m'
xb = '\033[1;96m'
t = '\033[1;97m'
def write(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)
def load():
  kha = ['.   ','..  ','... ']
  for o in kha:
    print("\r\033[1;97m[\033[1;96m*\033[1;97m] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
f = "\033[1;95------------------------------------------------------------"
banner = """
\033[1;95艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ砛033[1;92  [艗鈮ぢ勨€毭劽碷 tool t艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m tb v1.0
\033[1;92艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ掆墹卢茂卢锚艗鈮ぢ掆墹卢帽卢脿艗鈮ぢ甭犈掆墹卢茂卢贸\033[1;96  [艗鈮ぢ勨€毭劽碷B艗卤艗盲卢拢n quy艗卤卢陋卢脜n c艗卤卢陋卢脽a D艗茂卢漏ng  
\033[1;96艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ�  艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ玕033[1;93  [艗鈮ぢ勨€毭劽碷Gmail:trongdung406@gmail.com
\033[1;93艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ�  艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ玕033[1;94  [艗鈮ぢ勨€毭劽碷Zalo/TSR:0936485851
\033[1;94艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ甭犈掆墹卢帽卢脿艗鈮ぢ掆墹卢茂卢霉\033[1;95  [艗鈮ぢ勨€毭劽碷Facebook: D艗茂卢漏ng D艗茂卢漏ng
\033[1;97艗鈮ぢ杜掆墹卢茂卢锚艗鈮ぢ掆墹卢茂卢锚艗鈮ぢ掆墹卢茂卢锚艗鈮ぢ�
"""
def main():
  os.system('clear')
  write(banner)
  write(xl+'Ch艗矛卢鈥爋 m艗卤卢陋卢麓ng b艗卤艗盲鈥毭劽瞡 艗卯卢毛艗卤艗盲艗猫n v艗卤卢陋卢玫i h艗卤卢陋卢谩 th艗卤卢陋卢毛ng t艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh.')
  write(xb+'C艗卤艗盲卢拢m 艗帽鈥毭劽瞡 b艗卤艗盲鈥毭劽瞡 艗卯卢毛艗矛卢拢 s艗卤卢陋卢鈮� d艗卤卢陋鈥毭嚸榥g')
  write(f)
  load()
  menu()
def yn():
  write(f)
  cnbn = input('B艗卤艗盲鈥毭劽瞡 c艗矛卢鈮� mu艗卤卢陋卢毛n quay v艗卤卢陋卢脜 l艗卤艗盲鈥毭劽瞚 menu kh艗矛艗脩ng? [y/n] :')
  if cnbn == 'y' or cnbn == 'Y':
    menu()
  elif cnbn == 'n' or cnbn == 'N':
    print('\033[1;96m C艗矛鈥毭劽瞞 艗帽鈥毭劽瞡 b艗卤艗盲鈥毭劽瞡 艗卯卢毛艗矛卢拢 s艗卤卢陋卢鈮� d艗卤卢陋鈥毭嚸榥g c艗矛艗脩ng c艗卤卢陋鈥毭嚸� c艗卤卢陋卢脽a t艗矛艗脩i')
    os.sys.exit()
  else:
    print(d+'[!] Nh艗卤艗盲卢鈮爌 sai')
    os.sys.exit()
def menu():
  os.system('clear')
  write(banner)
  write(f)
  write(t+'['+xl+'1'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 2 m艗矛艗脩n')
  write(t+'['+xl+'2'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 3 m艗矛艗脩n')
  write(t+'['+xl+'3'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 4 m艗矛艗脩n')
  write(t+'['+xl+'4'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 5 m艗矛艗脩n')
  write(t+'['+xl+'5'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 6 m艗矛艗脩n')
  write(t+'['+xl+'6'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 7 m艗矛艗脩n')
  write(t+'['+xl+'7'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 8 m艗矛艗脩n')
  write(t+'['+xl+'8'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 9 m艗矛艗脩n')
  write(t+'['+xl+'9'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 10 m艗矛艗脩n')
  write(t+'['+xl+'10'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 11 m艗矛艗脩n')
  write(t+'['+xl+'11'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 12 m艗矛艗脩n')
  write(t+'['+xl+'12'+t+'] T艗矛卢鈮爊h 艗卯卢毛i艗卤卢陋卢脡m trung b艗矛卢篓nh 13 m艗矛艗脩n')
  write(f)
  q = input(t+'[?] Nh艗卤艗盲卢鈮爌 l艗卤卢陋卢卤a ch艗卤卢陋卢莽n c艗卤卢陋卢脽a b艗卤艗盲鈥毭劽瞡: '+xl)
  if q == '1' or q == '01':
    k2()
  elif q == '2' or q == '02':
    k3()
  elif q == '3' or q == '03':
    k4()
  elif q == '4' or q == '04':
    k5()
  elif q == '5' or q == '05':
    k6()
  elif q == '6' or q == '06':
    k7()
  elif q == '7' or q == '07':
    k8()
  elif q == '8' or q == '08':
    k9() 
  elif q == '9' or q == '09':
    k10()
  elif q == '10' or q == '10':
    k11()
  elif q == '11' or q == '11':
    k12()
  elif q == '12' or q == '12':
    k13()
  else:
        print(d+'[!] Nh艗卤艗盲卢鈮爌 Sai')
        os.sys.exit()
def k2():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  write(f)
  re = (k+kk)/2
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k3():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  re = (k+kk+kkk)/3
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k4():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  kkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 4 :'))
  write(f)
  re = (k+kk+kkk+kkkk)/4
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k5():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  kkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 4 :'))
  write(f)
  kkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 5 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk)/5
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k6():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  kkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 4 :'))
  write(f)
  kkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 5 :'))
  write(f)
  kkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 6 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk)/6
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k7():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  kkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 4 :'))
  write(f)
  kkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 5 :'))
  write(f)
  kkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 6 :'))
  write(f)
  kkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 7 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk)/7
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k8():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  kkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 4 :'))
  write(f)
  kkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 5 :'))
  write(f)
  kkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 6 :'))
  write(f)
  kkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 7 :'))
  write(f)
  kkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 8 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk)/8
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k9():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  kkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 4 :'))
  write(f)
  kkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 5 :'))
  write(f)
  kkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 6 :'))
  write(f)
  kkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 7 :'))
  write(f)
  kkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 9 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk)/9
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k10():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  kkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 4 :'))
  write(f)
  kkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 5 :'))
  write(f)
  kkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 6 :'))
  write(f)
  kkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 7 :'))
  write(f)
  kkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 10 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk)/10
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k11():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  kkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 4 :'))
  write(f)
  kkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 5 :'))
  write(f)
  kkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 6 :'))
  write(f)
  kkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 7 :'))
  write(f)
  kkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 10 :'))
  write(f)
  kkkkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 11 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk+kkkkkkkkkkk)/11
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k12():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  kkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 4 :'))
  write(f)
  kkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 5 :'))
  write(f)
  kkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 6 :'))
  write(f)
  kkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 7 :'))
  write(f)
  kkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 10 :'))
  write(f)
  kkkkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 11 :'))
  write(f)
  kkkkkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 12 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk+kkkkkkkkkkk+kkkkkkkkkkkk)/12
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
def k13():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢锚i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 1 : '))
  write(f)
  kk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 2 : '))
  write(f)
  kkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 3 :'))
  write(f)
  kkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 4 :'))
  write(f)
  kkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 5 :'))
  write(f)
  kkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 6 :'))
  write(f)
  kkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 7 :'))
  write(f)
  kkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 10 :'))
  write(f)
  kkkkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 11 :'))
  write(f)
  kkkkkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 12 :'))
  write(f)
  kkkkkkkkkkkkk = float(input('Nh艗卤艗盲卢鈮爌 艗卯卢毛i艗卤卢陋卢脡m m艗矛艗脩n th艗卤卢陋卢漏 13 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk+kkkkkkkkkkk+kkkkkkkkkkkk+kkkkkkkkkkkkk)/13
  load()
  write('艗卯卢锚i艗卤卢陋卢脡m trung b艗矛卢篓nh l艗矛卢鈥� %.2f:'%re)
  write(f)
  if (re < 5):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c y艗卤艗盲艗猫u")
  elif(re >=5 and re < 7):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c trung b艗矛卢篓nh")
  elif(re >=7 and re < 9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c kh艗矛鈥毭劽�")
  elif(re >=9):
        print("H艗卤卢陋卢莽c l艗卤卢陋卢卤c gi艗卤卢陋卢猫i")
  yn()
#=====RUN TOOL=====#
main()