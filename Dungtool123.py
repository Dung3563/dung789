import os, sys
key = input('Nhập key tại đây: ')
if key == '':
   print('sai key')
   os.sys.exit()
elif key == 'DGAME':
   print('key đúng')
else:
   print('key sai')
   os.sys.exit()

import os 
banner = """
\033[1;92m██████╗  ██████╗  █████╗ ███╗   ███╗███████╗
██╔══██╗██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ██║██║  ███╗███████║██╔████╔██║█████╗
██║  ██║██║   ██║██╔══██║██║╚██╔╝██║██╔══╝
██████╔╝╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝"""

os.system('clear')
print(banner) 


name = input('Tên bạn là gì: ')
print('Hello bạn'+name+'thanks bạn đã xem tool')

print("update game, done")

print("hello bạn, đây là trò chơi con mực bản lỗi :)")

print("trò chơi 1, đoán số")

print("bạn sai, đưa tôi 2$. bạn thắng, tôi đưa 20$")

#GuessingGame.py
import random # phải “nhập khẩu” chương trình random trước
the_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: ")) # bạn đoán mò 1 số từ 1 đến 10
count = 0
while guess != the_number: # trong khi số bạn cho còn khác với số của máy cho thì cứ tiếp tục vòng lặp while
    if guess > the_number:
        print(guess, "sai r đưa t 2$ :).") # không phải, số m chọn lớn quá,đưa t 2$
        count = count + 2
    if guess < the_number:
        print(guess, "sai rồi đưa t 2$ :).") # không phải, số m chọn thấp quá,đưa t 2$
        count = count + 2
    guess = int(input("lại đê bạn êi :)")) # Đoán lại đi !
print(guess, "đúng rồi :( 20$ nè") # Đúng rồi m thắng 20$ :(((
if count < 20:
  print("But we pay", 20-count, "$")
else:
  print("But you still have to pay", 20-count, "$")
  
print("tiếp theo là trò chơi con mực lỗi p2 :))")
  
print("trò chơi này tên là oẳn tù tì (búa bao kéo)")
  

import random   # “nhập cảng” đúng ra là gọi chương trình random của Python 
choices = ["búa", "lá", "kéo"] # danh sách tên các thứ bạn/computer chọn 
print("búa thắng kéo. kéo thắng lá. lá thắng búa.") # luật lệ của trò chơi
player = input("bạn chọn búa, lá hay kéo (or quit)? ") # bạn ra cái gì? búa, giấy hay kéo hay quit?
while player != "quit":           # Tiếp tục chơi trong khi bạn chưa gõ chữ quit 
    player = player.lower()   # Chuyển cái bạn chọn ra thành chữ thường (lower case)
    computer = random.choice(choices)   # computer chọn ngẫu nhiên một cái trong danh sách choices
    print("You chose " +player+ ", and the computer chose " +computer+ ".") # cho hiện ra cái bạn chọn và cái computer chọn. Dấu + để nối các biến player và computer vào với các string (text) mà thôi
    if player == computer: # nếu giống nhau
        print("hòa rồi!") # giống nhau thì huề
    elif player == "búa":  # nếu bạn chọn búa
        if computer == "kéo": # nếu computer chọn kéo
            print("bạn thắng rồi, chúc mừng <3!")  # bạn thắng
        else:  # nếu không
            print("tôi win rồi, bạn thua!") # computer thắng
    elif player == "lá":  # nếu bạn ra giấy
        if computer == "búa": # và nếu computer ra búa
            print("bạn thắng rồi!") # thì bạn thắng
        else: # nếu không
            print("tôi thắng rồi, bạn thua!") # computer thắng
    elif player == "kéo": # nếu bạn ra kéo
        if computer == "lá": # và nếu computer ra giấy
            print("bạn thắng rồi!") # thì bạn thắng 
        else: # nếu không
            print("tôi thắng rồi, bạn thua!") # computer thắng
    else: 
        print("tôi nghĩ có j đó sai rồi, báo cho chủ nhân tôi với nhé ")
    print()                             
    player = input("bạn muốn chơi với tôi tiếp không (or quit)? ") 
   
  