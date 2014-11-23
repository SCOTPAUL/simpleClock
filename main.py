#!/usr/bin/python

from Tkinter import *
import clock
from config import *
from math import sqrt


class ResizingCanvas(Canvas):
    def __init__(self,parent, width, height, **kwargs):
        Canvas.__init__(self,parent, width=width, height=height, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = height
        self.width = width

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        #This -=2 is a temporary hack to stop window scaling forever
        #TODO: Find out why event.width and event.height are always 2 greater than the canvas size
        event.width -=2
        event.height -=2

        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "static" tag
        self.scale("static",0,0,wscale,hscale)

        for hand in hands:
            hand.rescale((self.width/2.0, self.height/2.0), wscale)



root = Tk()
root.title("Clock")
root.aspect(1,1,1,1)
frame = Frame(root)
frame.pack(fill=BOTH, expand=YES)

#Create a canvas widget, to draw clock on
win = ResizingCanvas(frame, width = CANWIDTH, height = CANHEIGHT)
win.pack(fill=BOTH, expand=YES)  #Places canvas on screen

#Create objects for each part of the clock
clockFace = clock.clockOuter(win, CANWIDTH/2.0 - 10, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 5.0)
secondHand = clock.hand(frame, "second", win, clockFace.radius- (1/4.0)*clockFace.radius, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 5.0, colour = "#FF0000")
minuteHand = clock.hand(frame, "minute", win, clockFace.radius- (1/3.0)*clockFace.radius, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 8.0, colour = "#000000")
hourHand = clock.hand(frame, "hour", win, clockFace.radius- (1/2.0)*clockFace.radius, (CANWIDTH/2.0, CANHEIGHT/2.0), width = 10.0, colour = "#000000")
centreRing = clock.clockCentre(win, 8, (CANWIDTH/2.0, CANHEIGHT/2.0))

staticWidgetList = [clockFace, centreRing]
hands = [secondHand, minuteHand, hourHand]



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

