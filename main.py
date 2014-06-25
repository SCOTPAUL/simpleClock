#!/usr/bin/python

from Tkinter import *
import clock
from config import *


root = Tk()
root.title("Clock")
root.resizable(0,0)

win = Canvas(root, width = CANWIDTH, height = CANHEIGHT)
win.grid()  #Places canvas on screen

clockFace = clock.clockOuter(win, CANWIDTH/2.0 - 10, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 5.0)
secondHand = clock.hand(root, "second", win, clockFace.radius- (1/4.0)*clockFace.radius, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 5.0, colour = "#FF0000")
minuteHand = clock.hand(root, "minute", win, clockFace.radius- (1/3.0)*clockFace.radius, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 8.0, colour = "#000000")
hourHand = clock.hand(root, "hour", win, clockFace.radius- (1/2.0)*clockFace.radius, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 10.0, colour = "#000000")
centreRing = clock.clockCentre(win, 8, (CANWIDTH/2.0, CANHEIGHT/2.0))

clockFace.drawOuterRing()
clockFace.drawHourLines()

secondHand.update()
minuteHand.update()
hourHand.update()

secondHand.draw()
minuteHand.draw()
hourHand.draw()

centreRing.draw()


root.mainloop()

