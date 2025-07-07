# importing the library to use build-in functions for screenshot
import pyautogui
import time

def screenshot():
  time.sleep(3)
  name=time.time()
  name="C:/Users/prana/PYTHON PROJECTS/screenshots/{}.png".format(name)
  img=pyautogui.screenshot()
  img.save(name)
  img.show()

screenshot()