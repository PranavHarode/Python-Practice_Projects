#import required libraries
import tkinter as tk
from time import strftime

root =tk.Tk()
root.title("Digital Clock")

#defining time() fumction 
def time():
    string= strftime("%H:%M:%S %p \n %D ")
    label.config(text=string)
    label.after(1000,time)

# Designing digital clock
label=tk.Label(root,font=('calibri', 70 ,"bold"),background="black",foreground='white')
label.pack(anchor='center')

#Calling time function
time()
#puting program in loop to updating rime continuesly
root.mainloop()
