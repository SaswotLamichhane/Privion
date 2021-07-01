import requests
from bs4 import BeautifulSoup
import datetime
import os
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
def covid_return():
    os.system(f'notify-send -i /home/shaswot/Pictures/avatar.jpg --urgency=critical "{c_text}" "{d_text}"')
    os.system('play co.wav')
