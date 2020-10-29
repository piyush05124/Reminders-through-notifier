import datetime
import time
from datetime import date
import win10toast
from win10toast import ToastNotifier
import schedule
import re
import os
import datetime



def notify(x):
    toaster = ToastNotifier()
    toaster.show_toast(x)

def remind():
    r=datetime.datetime.now()
    r=r.strftime("%I:%M %p")

    if r=="06:00 PM":
        notify('study C programming ')
    if r=="08:30 PM" :
        notify('study Computer Organization ')
    if r=="11:30 PM":
        notify('study OPERATING SYSTEM ')
        








schedule.every(2).seconds.do(remind)
while True:
    schedule.run_pending() 
    time.sleep(1)
