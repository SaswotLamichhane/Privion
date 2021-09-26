import os,datetime as E,time
from covidon import covid_return as F
J='play "/home/shal/Documents/code/Privion/co.mp3"'
I='covid'
G=['10:05',0, '11:05',1,'12:05',2,'13:35',3,'14:35',4];B=['18:30','Job','17:00',I, '16:00', "Duolingo 'French Time'", '22:00', 'Sleep!'];subjects = {'Sunday': ['C.Math', 'Science', 'S.Studies', 'O.Maths', 'HPE'], 'Monday': ['Computer', 'English', 'Nepali', 'C.Maths', 'Science'], 'Tuesday': ['English', 'Social', 'O.Maths', 'Computer', 'HPE'], 'Wednesday': ['C.Maths', 'Nepali', 'Science', 'Social', 'HPE'], 'Thursday': ['O.Maths', 'Computer', 'Nepali', 'English', 'C.Maths'], 'Friday': ['Science', 'Social', 'English', 'O.maths', 'Computer']}
OOSD=E.datetime.now()
day = OOSD.strftime("%A")
if day != "Saturday":
	s = subjects[day]
while True:
	H=E.datetime.now();C=H.strftime('%H:%M')
	if day != "Saturday":
		for A in G:
			if A==C:s_c=G[G.index(A)+1];su=s[s_c];os.system(f'notify-send --urgency=critical "Online class" {su}');os.system(J)
	for A in B:
		if A==C:
			D=B[B.index(A)+1]
			if D==I:F()
			else:os.system(f'notify-send -i "/home/shal/Documents/code/Privion/avatar.jpg" --urgency=critical {D}');os.system(J)
	time.sleep(60)