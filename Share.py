import os, sys, requests, time, datetime, json
d = '\033[1;91m'
xl = '\033[1;92m'
v = '\033[1;93m'
xb = '\033[1;96m'
t = '\033[1;97m'
vio = '\033[1;95m'
def write(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)
f = "\033[1;97m------------------------------------------------------------"
banner = """
\033[1;96m██████╗  [•] Copyright Axeyed Kha (có của Dũng nữa :))
\033[1;92m██╔══██╗ [•] Tool tính đủ thứ trên đời :v
\033[1;95m██║  ██║ [•] Facebook: Dũng Dũng
\033[1;92m██║  ██║ [•] Phiên bản v1.0
\033[1;96m██████╔╝ [•] Zalo: 0936485851
\033[1;97m╚═════╝  [•] Chúc các bạn dùng tool vui vẻ
"""
def menu():
  os.system('clear')
  print(banner) 
  print(f) 
  write(xl+"[•]tool like ảo fb tokeb")
  print(f)
  write(xb+"[1]Share 1 token")
  nhap = input("[√]Nhập chế độ muốn chạy: ")
  if nhap == '1' or nhap == '01':
    share_token1_function()
  else: 
    print(d+"Nhập sai")
    time.sleep(3)
    os.system('clear')
#1tokenshare
def share_token1_function():
  os.system('clear')
  print(banner) 
  print(f) 
  tokenfb = input(vio+"Nhập token fb của bạn: ")
  idshare = input(vio+"Nhập id cần share: ")
  dl = input(vio+"Nhập delay: ")
  check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
  if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        if "success" in run:
            print(f)
            print(xl+'Đang cấu hình id: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Nhập lỗi!")
            time.sleep(3)
            os.sys.exit()
  else:
        print(d+"Token lỗi! ")
        time.sleep(3)
        os.sys.exit()
  print(f)
  dem=0
  t=datetime.datetime.now().strftime("%X")
  dem=dem+1 
  while True:
      getshare=requests.get('https://graph.facebook.com/'+idshare+'?access_token='+tokenfb)
      idshare=getshare.json()[0]['id']
      urlshare='https://graph.facebook.com/'+str(idlike)+'/share'
      datashare="access_token="+tokenfb
      share=requests.post(urlshare, data=datashare)
      id=idshare[0:15]
      if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Share >\x1b[1;95m {id} >\x1b[1;93m Hoàn Thành ')
                for demtg in range(dl, -1, -1):
                    print(xb+'Làm job tiếp sau -->   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
      else:
        print(d+'Lỗi '+id,end='\r')
menu()