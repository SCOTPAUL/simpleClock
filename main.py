#!/usr/bin/python

from Tkinter import *
import clock
from config import *


root = Tk()
root.title("Clock")

#Prevent root window from being resized
root.resizable(0,0)

#Create a canvas widget, to draw clock on
win = Canvas(root, width = CANWIDTH, height = CANHEIGHT)
win.grid()  #Places canvas on screen

#Create objects for each part of the clock
clockFace = clock.clockOuter(win, CANWIDTH/2.0 - 10, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 5.0)
secondHand = clock.hand(root, "second", win, clockFace.radius- (1/4.0)*clockFace.radius, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 5.0, colour = "#FF0000")
minuteHand = clock.hand(root, "minute", win, clockFace.radius- (1/3.0)*clockFace.radius, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 8.0, colour = "#000000")
hourHand = clock.hand(root, "hour", win, clockFace.radius- (1/2.0)*clockFace.radius, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 10.0, colour = "#000000")
centreRing = clock.clockCentre(win, 8, (CANWIDTH/2.0, CANHEIGHT/2.0))

#Draw the outer circle and hour divisions of the clock
clockFace.drawOuterRing()
clockFace.drawHourLines()

#Set hands to current time
secondHand.update()
minuteHand.update()
hourHand.update()

#Draw each hand
secondHand.draw()
minuteHand.draw()
hourHand.draw()

#Draw the centrepiece of the clock
centreRing.draw()


root.mainloop()

