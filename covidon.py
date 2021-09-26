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
      t_cases = int(new) - int(recovered)
      b = '🔵️'
      a = '📈!'
      if t_cases < 0:
          b = '🔴️ '
          a = '🔻'
      t = b+str(new)+" cases \n"+b+str(recovered)+" recovered \n"+b+ str(deaths)+" deaths \n" +b+str(t_cases)+" total"
      os.system(f'notify-send -i "/home/shal/Documents/code/Privion/c.png" --urgency=critical "{b+date+"    "+a}" "{t}"')
      os.system('play ./co.mp3')
    except:
        i += 1
        os.system(f'notify-send -i "/home/shal/Documents/code/Privion/avatar.jpg" --urgency=critical "No Internet Connection" "I will try in 5 minutes for 5 times"')
        time.sleep(300)
        if i < 5:
            covid_return()
        else:
            pass