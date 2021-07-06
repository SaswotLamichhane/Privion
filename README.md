# Privion

A project I wish to maintain, Works only on ubuntu based system. 

# Required packages
* Unix play
* notify-send
* Python 8.0+
> Tested on [Pop! os](https://pop.system76.com/ "Pop! Os Official Website") 21.04, MacOS Big sur, [Fedora](https://getfedora.org/) 34 Should work on versions closer to it. 

# Main file

The main file which should be run is [alarm.py](https://github.com/SaswotLamichhane/Privion/blob/master/alarm.py "Opens the github link to alarm.py")

# Mechanics
It works by running the main code evey second. While it runs, It receives the current time of the user, It then checks through the list of alarms marked by _G_ and _B_ through `for` loop.
If the current time matches one of the times in the _G_ or _B_ list, It triggers the alarm. Once the alarm is triggered a notificaition is sent and music is played. 

> Other simple functionalities can be easily understood my checking the code. The code is compressed to decrease memory usage. But earlier versions of it contains the un-compressed code which is more read-able.
