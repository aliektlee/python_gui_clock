#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from tkinter import *
import threading
from datetime import datetime
import time
import sys 

window = Tk()
 
window.title("CLOCK")
 
lbl = Label(window,bg="black", text="Hello", font=("Arial Bold", 50,),fg="white")
 
lbl.grid(column=0, row=0)

window.geometry('620x60')
window.resizable(0, 0)

def loop_clock(tlbl):
    print('loop_clock')
    while keep_run:
        time.sleep(0.1)
        # print(datetime.now().ctime())
        tlbl['text']= datetime.now().ctime()

keep_run = True
x = threading.Thread(target=loop_clock, args=(lbl,), daemon=True)
x.start()


window.lift()
window.attributes('-topmost', True)
window.update()
 
window.mainloop()

keep_run = False

print('close')
sys.exit()
