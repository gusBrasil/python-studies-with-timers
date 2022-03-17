import datetime
import time
import os
import webbrowser
import win32api
import random

# variable to check what it is right now
now = datetime.datetime.now()

hora = int(input('Insira a hora: '))
minuto = int(input('Insira os minutos: '))
segundo = -10

horaDesejada = datetime.time(hora, minuto, segundo)


# this will make the alarm go off at 18h00
alarmTime = datetime.datetime.combine(now.date(), horaDesejada)

# this will make so that the program isn't constantly running, but actually sleeping until the time set for the alarm to go off

def alarme():
    time.sleep((alarmTime - now).total_seconds())
    for i in range(5):
        #time.sleep((alarmTime - now).total_seconds())
        time.sleep(0.1)
    
        # this will alert you
        win32api.Beep(4500, 500)
        
alarme()