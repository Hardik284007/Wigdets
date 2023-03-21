from tkinter import*
from tkinter import ttk
import psutil
from psutil._common import BatteryTime
import datetime 
import time

root = Tk()
root.geometry("500x250")
root.config(bg="black")
root.overrideredirect(True)
style = ttk.Style(root)
style.layout('progressBarStyle'
             [('Horizontal.ProgressBar.trough',
               {'children': [('Horizontal.Progresssbar.pbar',
                              {'side':'right','stcky':'ns'})],
               'sticky':'nsew'}),
              ('Horizontal.progressBar.label', {'sticky':''})])
bar = ttk.ProgressBar(root, minimize = 100, style = 'ProgressBarStyle')
bar.place(relx=0.5, rely=0.2, anchor = CENTER)
battery_life = ttk.ProgressBar(root, font = 'arial 15 bold', bg="black", fg="white")
battery_life.place(relx=0.5, rely=0.5, anchor = CENTER)

def convertTime(seconds):
    get_time = time.gmtime(seconds)
    time_remain = time.strftime("%H:&M:%S", get_time)
    return time_remain

def getBatterylife():
    battery = psutil.sensors_battery()
    bar['value']=battery.percent
    style.configure('ProgressBarStyle', text = str(battery.percent) + '%')
    battery_left = convertTime(battery.secsleft)
    if battery.secsleft == BtteryTime.POWER_TIME_UNLIMITED:
        battery_life['text']  = ' Unplugged the Battery! \n And rerun the code again'
    elif battery.secsleft == BtteryTime.POWER_TIME_UNKNOWN:
        battery_life['text']  = ' Battery life did not detected. \n Plese, run the code again'
    else:
        battery_life['text']  = ' Battery life: ' + battery_left
        root.after(1000, getBatterylife)
getBatterylife()
root.mainloop()


