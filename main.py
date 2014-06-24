#!/usr/bin/python

from Tkinter import *
import clock 


CANWIDTH = 500
CANHEIGHT = 500

root = Tk()
root.title("Clock")
root.resizable(0,0)

win = Canvas(root, width = CANWIDTH, height = CANHEIGHT)
win.grid(ipadx = 10, ipady = 10)  #Places canvas on screen

clockFace = clock.clockOuter(win, CANWIDTH/2.0 - 10, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 5.0)

secondHand = clock.hand("second", win, clockFace.radius- (1/3.0)*clockFace.radius, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 5.0, colour = "#FF0000")

win.delete("all")

clockFace.draw()

for times in range(3600):
    secondHand.draw()
    secondHand.tick()

root.mainloop()