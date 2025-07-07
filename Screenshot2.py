#creating GUI application for screenshot using tkinter library
import tkinter as tk
# importing the library to use build-in functions for screenshot
import pyautogui
import time
from unicodedata import name

#main function to taking,naming and saving an screenshot
def screenshot():
  time.sleep(3)
  name=time.time()
  name="C:/Users/prana/PYTHON PROJECTS/screenshots/{}.png".format(name)
  img=pyautogui.screenshot()
  img.save(name)
  img.show()


root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

# creating button
button=tk.Button(frame,text="Take Screenshot",command= screenshot)
button.pack(side=tk.LEFT)

#crating close button
close=tk.Button(frame,text="QUIT",command=quit)
close.pack(side=tk.LEFT)

root.mainloop()

#calling a function
screenshot()