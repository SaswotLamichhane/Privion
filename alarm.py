import os,datetime as E,time
from covidon import covid_return as F
J='play /home/Shaswot/Documents/Privion/co.mp3'
I='covid'
G=['19:19','11:05','12:05','13:35','14:35'];B=['18:30','Aarti','17:20',I,'21:00','Dish Wash', '16:00', "Duolingo 'French Time'", '22:00', 'Sleep!'];subjects = {'Sunday': ['C.Math', 'Science', 'S.Studies', 'O.Maths', 'HPE'], 'Monday': ['Computer', 'English', 'Nepali', 'C.Maths', 'Science'], 'Tuesday': ['English', 'Social', 'O.Maths', 'Computer', 'HPE'], 'Wednesday': ['C.Maths', 'Nepali', 'Science', 'Social', 'C.Maths'], 'Thursday': ['O.Maths', 'Computer', 'Nepali', 'English', 'Computer'], 'Friday': ['Science', 'Social', 'English', 'O.maths', 'Computer']};s_c = 0
while True:
	H=E.datetime.now();C=H.strftime('%H:%M')
	day = H.strftime("%A") 
	s = subjects[day]
	if day == "Saturday":
		break
	for A in G:
		if A==C:su=s[s_c];os.system(f'notify-send --urgency=critical "Online class" {su}');os.system(J);s_c +=1
	for A in B:
		if A==C:
			D=B[B.index(A)+1]
			if D==I:F()
			else:os.system(f"notify-send -i /home/Shaswot/Documents/Privion/avatar.jpg --urgency=critical {D}");os.system(J)
	time.sleep(60)
