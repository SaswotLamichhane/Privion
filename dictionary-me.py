from PyDictionary import PyDictionary
import os
dictionary=PyDictionary()
diction = dictionary.meaning("good")
headers = list(diction.keys())
final_header = str()
final_main = str()
for i in range(len(headers)):
    header = headers[i]
    values = diction[header]
    main = ''
    for i in values:
        main = main + ',' + i
    final_header = final_header + "\n" + header + "\n" 
    final_main = final_main + "\n" + main + "\n"

os.system(f'notify-send "{final_header}" "{final_main}"')