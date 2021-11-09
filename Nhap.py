import time, datetime, requests, json, os, re
try:
    import os, sys, time, datetime, random, requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system('pip2 install requests')
    os.system('pip install requests')
    time.sleep(1)
#======color======#
d = '\x1b[1;91m'
xl = '\x1b[1;92m'
v = '\x1b[1;93m'
xb = '\x1b[1;96m'
t = '\x1b[1;97m'
vio = '\x1b[1;95m'
#=====Logo && Banner=====#
banner = """
\033[1;96m██████╗  [•] Thank kha đã giúp  :))
\033[1;92m██╔══██╗ [•] Tool tds token
\033[1;95m██║  ██║ [•] Facebook: Dũng Dũng
\033[1;92m██║  ██║ [•] Phiên bản v1.0
\033[1;96m██████╔╝ [•] Zalo: 0936485851
\033[1;97m╚═════╝  [•] Chúc các bạn dùng tool vui vẻ
"""
f = """\033[1;97m----------------------------------------------------------------"""
def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
#=====Login Tool=====#
def login():
    os.system('clear')
    print(banner)
    print(f)
    write('key test')
    print(xl+'namekey: Dtool')
    print(xl+'passkey: v1.0')
    print(f)
    correctkeyname = 'Dtool'
    CorrectPasswordkey = 'v1.0'
    loop = 'true'
    while loop == 'true':
        username = input('\x1b[1;96m Key Name >> ')
        if username == correctkeyname:
            password = input('\x1b[1;96m Key Password >> ')
            if password == CorrectPasswordkey:
                main_menu()
                loop = 'false'
            else:
                print ('Wrong Key')
        else:
            print ('Wrong Username Key')
#======Menu Tool=====#
def main_menu():
    os.system('clear')
    write(banner)
    print(f)
    write(v+'Chào mừng tới tool tds token v1.0')
    print(f)
    write(t+'[1] Follow')
    write(t+'[2] Like')
    write(t+'[3] Comment')
    write(t+'[4] Share')
    write(t+'[5] Reaction')
    write(t+'Để thoát, Ctrl + Z')
    print(f)
    kali = input(xl+'Chọn chế độ: ')
    if kali == '1' or kali == '01':
        tool_follow_function()
    elif kali == '2' or kali == '02':
        tool_like_function()
    elif kali == '3' or kali == '03':
        tool_comment_function()
    elif kali == '4' or kali == '04':
        tool_share_function()
    else:
        print(d+'[!] Wrong')
        os.sys.exit()
def tool_follow_function():
    os.system('clear')
    print(banner)
    print(f)
    write(xl+'Job bạn chọn: Follow')
    print(f)
    tokentds = input('\033[1;93m Nhập token tds: ')
    print(f)
    tokenfb = input('\033[1;96m Nhập token facebook: ')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f)
        print(xl+"Đăng nhập thành công")
    else:
        print(d+"Token sai! ")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Tên tài khoản: "+user)
    write(xb+"Xu trong tài khoản:  "+xu)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Nhập lỗi!")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token lỗi! ")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Tên tài khoản: "+user)
    write(xb+"Xu trong tài khoản: "+xu)
    print(f)
    job=input(v+"Follow TDS [y/n] ")
    print(f)
    dl=int(input(xb+"Time Delay >> "))
    print(f)
    dem=0
    if job=="y" or job == "Y":
        while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getfolow=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+tokentds)
            idfolow=getfolow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idfolow)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(idfolow)+'&access_token='+tokentds).text)
            id=idfolow[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Follow >\x1b[1;95m {id} >\x1b[1;93m +600 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Đang chạy, xin đợi:   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('Lỗi'+id,end='\r')
    elif job == 'n' or job == 'N':
        os.sys.exit()
    else:
        print(d+'[!] Lỗi!! ')


def tool_like_function():
    os.system('clear')
    print(banner)
    print(f)
    write(xl+'Job bạn chọn: LIKE')
    print(f)
    tokentds = input('\033[1;93m Nhập token tds: ')
    print(f)
    tokenfb = input('\033[1;96m Nhập token fb')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f)
        print(xl+"Đăng nhập thành công")
    else:
        print(d+"Token lỗi")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Tên tài khoản: "+user)
    write(xb+"Xu trong tài khoản: "+xu)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Lỗi")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token lỗi")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Tên tài khoản: "+user)
    write(xb+"Xu trong tài khoản: "+xu)
    print(f)
    job=input(v+"Like TDS [y/n] ")
    print(f)
    dl=int(input(xb+"Time Delay  "))
    print(f)
    dem=0
    if job=="y" or job == "Y":
        while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getfolow=requests.get('https://traodoisub.com/api/?fields=like&access_token='+tokentds)
            idfolow=getfolow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idfolow)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('ttps://traodoisub.com/api/coin/?type=LIKE&id='+str(idfolow)+'&access_token='+tokentds).text)
            id=idfolow[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m LIKE >\x1b[1;95m {id} >\x1b[1;93m +300 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Đang chạy, xin đợi:   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('Lỗi'+id,end='\r')
    elif job == 'n' or job == 'N':
        os.sys.exit()
    else:
        print(d+'[!] Lỗi!!')


def tool_comment_function():
    os.system('clear')
    print(banner)
    print(f)
    write(xl+'Job bạn chọn: COMMENT')
    print(f)
    tokentds = input('\033[1;93m Nhập token tds: ')
    print(f)
    tokenfb = input('\033[1;96m Nhập token fb: ')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f)
        print(xl+"Đăng nhập thành công")
    else:
        print(d+"Token Lỗi")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Tên tài khoản tds:  "+user)
    write(xb+"Xu trong tài khoản: "+xu)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Lỗi!! ")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token lỗi")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Tên tài khoản: "+user)
    write(xb+"Xu trong tài khoản: "+xu)
    print(f)
    job=input(v+"Comment TDS [y/n] ")
    print(f)
    dl=int(input(xb+"Time Delay: "))
    print(f)
    dem=0
    if job=="y" or job == "Y":
        while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getfolow=requests.get('https://traodoisub.com/api/?fields=comment&access_token='+tokentds)
            idfolow=getfolow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idfolow)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=COMMENT&id='+str(idfolow)+'&access_token='+tokentds).text)
            id=idfolow[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Comment >\x1b[1;95m {id} >\x1b[1;93m +600 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Đang chạy, xin đợi:   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('Lỗi'+id,end='\r')
    elif job == 'n' or job == 'N':
        os.sys.exit()
    else:
        print(d+'[!] Nhập sai')
    

def tool_share_function():
    os.system('clear')
    print(banner)
    print(f)
    write(xl+'Job Bạn chọn: SHARE')
    print(f)
    tokentds = input('\033[1;93m Nhập token tds: ')
    print(f)
    tokenfb = input('\033[1;96m Nhập token fb: ')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f)
        print(xl+"Đăng nhập thành công")
    else:
        print(d+"Token lỗi")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Tên tài khoản: "+user)
    write(xb+"Xu trong tài khoản: "+xu)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Lỗi")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token lỗi")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Tên tài khoản: "+user)
    write(xb+"Xu trong tài khoản:  "+xu)
    print(f)
    job=input(v+"Share TDS [y/n] ")
    print(f)
    dl=int(input(xb+"Time Delay >> "))
    print(f)
    dem=0
    if job=="y" or job == "Y":
        while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getfolow=requests.get('https://traodoisub.com/api/?fields=share&access_token='+tokentds)
            idfolow=getfolow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idfolow)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=SHARE&id='+str(idfolow)+'&access_token='+tokentds).text)
            id=idfolow[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Share >\x1b[1;95m {id} >\x1b[1;93m +800 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Đang chạy, xin đợi:   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('Lỗi'+id,end='\r')


def tool_reaction_funtion():
    os.system('clear')
    print(banner)
    print(f)
    write(xl+'Job bạn chọn: COMMENT')
    print(f)
    tokentds = input('\033[1;93m Nhập token tds: ')
    print(f)
    tokenfb = input('\033[1;96m Nhập token fb')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f)
        print(xl+"Đăng nhập thành công")
    else:
        print(d+"Token Lỗi")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Tên tài khoản: "+user)
    write(xb+"Xu trong tài khoản: "+xu)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Lỗi! ")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token Sai")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Tên tài khoản: "+user)
    write(xb+"Xu trong tài khoản: "+xu)
    print(f)
    job=input(v+"Comment TDS [y/n] ")
    print(f)
    dl=int(input(xb+"Time Delay: "))
    print(f)
    dem=0
    if job=="y" or job == "Y":
        while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getfolow=requests.get('https://traodoisub.com/api/?fields=comment&access_token='+tokentds)
            idfolow=getfolow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idfolow)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=COMMENT&id='+str(idfolow)+'&access_token='+tokentds).text)
            id=idfolow[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Comment >\x1b[1;95m {id} >\x1b[1;93m +600 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Đang chạy, xin đợi:   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('Lỗi'+id,end='\r')
    elif job == 'n' or job == 'N':
        os.sys.exit()
    else:
        print(d+'[!] Sai')
#=====Exit=====#
def exit():
    print(banner)
    print(f)
    print(xl+'Cảm ơn bạn đã dùng tool ')
login()