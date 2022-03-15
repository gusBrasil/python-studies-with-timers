import datetime
import time
import os
import webbrowser

# variable to check what it is right now
now = datetime.datetime.now()

# this will make the alarm go off at 18h00
alarmTime = datetime.datetime.combine(now.date(), datetime.time(19, 30, 0))

# this will make so that the program isn't constantly running, but actually sleeping until the time set for the alarm to go off
time.sleep((alarmTime - now).total_seconds())

# put any link you'd like, i just put a random study playlist :)
webbrowser.open("https://www.youtube.com/watch?v=eGy-E8-cTjQ")