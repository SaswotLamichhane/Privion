J='play /home/Shaswot/Documents/Privion/co.mp3'
I='covid'
import os,datetime as E,time
while True:
    G=['10:05','11:05','19:44','13:35','14:35'] 
    print("hello")
    H=E.datetime.now();C=H.strftime('%H:%M')
    for A in G:
        if A==C:os.system('notify-send --urgency=critical Online class');os.system(J)
    time.sleep(60)
