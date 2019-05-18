##### Python Clock for Raspberry Pi 3B+
##### https://github.com/scottslaughter/clock
##### reqires Python3
##### exit the clock by clicking or pressing ESC
##### clock style may be adjusted in the style section
###################################################################
# import modules
from tkinter import *
#import sys

# importing strftime function to get time
from time import strftime 

# creating fullscreen tkinter widget (root) window
root = Tk() 
root.title('Clock') 
root.configure(background='black',cursor="none")
root.attributes('-fullscreen', True)

# function to allow ESC to exit
def exitClock(event):
    root.destroy()
root.bind('<Escape>', exitClock)
root.bind('<Button-1>', exitClock)

# put time into a label (lbl)
def time():
    string = strftime('%I:%M %p') 
    lbl.config(text = string) 
    lbl.after(1000, time)

# style
lbl = Label(root, font = ('DejaVu Sans', 66), 
            background = 'black', 
            foreground = 'darkorange') 
lbl.pack(anchor = 'center', pady=90) 

# execute
time()
mainloop() 
