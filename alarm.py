J='play /home/shaswot/Documents/code/utilities/ala.mp3'
I='covid'
import os,datetime as E,time
from covidon import covid_return as F
G=['10:00','11:00','12:00','13:32','14:32']
B=['18:30','Aarti','18:00',I,'20:30','Dish wash']
while True:
	H=E.datetime.now();C=H.strftime('%H:%M')
	for A in G:
		if A==C:os.system('notify-send --urgency=critical Online class');os.system(J)
	for A in B:
		if A==C:
			D=B[B.index(A)+1]
			if D==I:F()
			else:os.system(f"notify-send -i /home/shaswot/Pictures/avatar.jpg --urgency=critical {D}");os.system(J)
	time.sleep(60)