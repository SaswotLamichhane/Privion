import requests, json, time, os
i = 0
def covid_return():
    global i
    try:
      URL = 'https://covid19.mohp.gov.np/covid/api/confirmedcases'
      text = requests.get(URL).text
      data = json.loads(text)['nepal']
      new = data['today_newcase']
      date = data['date']
      recovered = data['today_recovered']
      deaths = data['today_death']
      t = str(new)+" cases \n"+str(recovered)+" recovered \n"+ str(deaths)+" deaths "
      os.system(f'notify-send -i "/media/shal/Hard disk/apps/Privion-master/co.mp3" --urgency=critical "{date}" "{t}"')
      os.system('play ./co.mp3')
    except:
        i += 1
        os.system(f'notify-send -i "/media/shal/Hard disk/apps/Privion-master/avatar.jpg" --urgency=critical "No Internet Connection" "I will try in 5 minutes for 5 times"')
        time.sleep(300)
        if i < 5:
            covid_return()
        else:
            pass