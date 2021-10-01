import os 
banner = """
\033[1;95m██████╗ ██╗   ██╗███╗   ██╗ ██████╗████████╗ ██████╗  ██████╗ ██╗
██╔══██╗██║   ██║████╗  ██║██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║  ██║██║   ██║██╔██╗ ██║██║  ███╗  ██║   ██║   ██║██║   ██║██║
██║  ██║██║   ██║██║╚██╗██║██║   ██║  ██║   ██║   ██║██║   ██║██║     ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝  ██║   ╚██████╔╝╚██████╔╝███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═════"""

os.system('clear')
print(banner) 

print("Hello, cảm ơn bạn đã sử dụng <3")
name = input ("bạn tên là gì:")
print(f"Hello {name}")

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