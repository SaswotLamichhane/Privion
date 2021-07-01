# import os
# import datetime
# import time
# from covidon import covid_return


# oalarm = ['10:00', '11:00', '12:00', '01:30', '02:30']

# palarm = ['18:30','Aarti','12:39', 'covid', '20:30', 'Dish wash']

# while True:
#     now = datetime.datetime.now()
#     target = now.strftime("%H:%M")
#     for i in oalarm:
#         if i == target:
#             os.system('notify-send --urgency=critical Online class')
#             os.system('play ala.mp3')
#     for i in palarm:
#         if i == target:
#             message = palarm[palarm.index(i) + 1]
#             if message == 'covid':
#                 covid_return()
#             else:
#                 os.system(f'notify-send -i /home/shaswot/Pictures/avatar.jpg --urgency=critical {message}')
#                 os.system('play ala.mp3')
#     time.sleep(60)
import datetime
now = datetime.datetime.now()
print(now.strftime("%H:%M"))