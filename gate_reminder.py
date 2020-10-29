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

def left():
    p=date.today()
    q=date(2021,2,5)
    z='GATE EXAM: {} days left'.format((q-p).days )
    notify(z)







schedule.every(10).minutes.do(left)
while True:
    schedule.run_pending() 
    time.sleep(1)
    
