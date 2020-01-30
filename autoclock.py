
from tkinter import *
import time
import pyautogui
import threading


global stop
stop = 0
def auto_click():
  global stop
  while True:
    print("click")
    time.sleep(1)
    if   stop != 1:
      pyautogui.click()
    else:
       exit  

t1=threading.Thread(target=auto_click)

def start_thread():
  t1.start()
def stopClick():
   global stop
   stop=1

window = Tk()               
window.geometry('100x100')  
  
# Create a Button 
btn1 = Button(window, text = 'start', bd = '2',command = start_thread)  #Just keep the mouse over the bottun 
btn2 = Button(window, text = 'stop', bd = '2',command = stopClick)  
    
  
btn1.pack(side = 'top')
btn2.pack(side = 'bottom')
#btn2.pack(side = 'bottom')     
  
window.mainloop()




