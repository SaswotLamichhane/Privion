import os,datetime as E,time
from covidon import covid_return as F
J='play /home/Shaswot/Documents/Privion/co.mp3'
I='covid'
G=['10:05','11:05','12:05','13:35','14:35']
B=['18:30','Aarti','17:20',I,'21:00','Dish Wash', '16:00', "Duolingo 'French Time'", '22:00', 'Sleep!']
while True:
	H=E.datetime.now();C=H.strftime('%H:%M')
	if H.strftime("%A") == "Saturday":
		break
	for A in G:
		if A==C:os.system('notify-send --urgency=critical Online class');os.system(J)
	for A in B:
		if A==C:
			D=B[B.index(A)+1]
			if D==I:F()
			else:os.system(f"notify-send -i /home/Shaswot/Documents/Privion/avatar.jpg --urgency=critical {D}");os.system(J)
	time.sleep(60)
