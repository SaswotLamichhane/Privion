import requests
from bs4 import BeautifulSoup
import datetime
import os
import time
i = 0
def covid_return():
    global i
    try:
        current = datetime.datetime.now()
        day = current.strftime("%m-%d")
        URL = 'https://www.worldometers.info/coronavirus/country/nepal'
        page = requests.get(URL)  
        soup = BeautifulSoup(page.content, 'lxml')
        result = soup.find('div', id=f"newsdate2021-{day}")
        sou = result.find('li', class_='news_li')
        p = sou.find_all('strong')
        cases = f"{p[0]}"
        death = f"{p[1]}"
        c_text = cases.replace('<strong>', '')
        c_text = c_text.replace("</strong>", '')
        d_text = death.replace('<strong>', '')
        d_text = d_text.replace("</strong>", '')
        os.system(f'notify-send -i /home/shaswot/Pictures/avatar.jpg --urgency=critical "{c_text}" "{d_text}"')
        os.system('play co.wav')
    except:
        i += 1
        os.system(f'notify-send -i /home/shaswot/Pictures/avatar.jpg --urgency=critical "No Internet Connection" "I will try in 5 minutes for 5 times"')
        time.sleep(300000)
        print(i)
        if i < 5:
            covid_return()
        else:
            pass