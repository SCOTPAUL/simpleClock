import math
from time import strftime

def getTime(timeType):
    if timeType == "second":
        return int(strftime("%S"))
    elif timeType == "minute":
        return int(strftime("%M"))
    elif timeType == "hour":
        return int(strftime("%H"))%12


class clockOuter(object):

    def __init__(self, canvas, radius, centre, colour = "#000000", fill = "#FFFFFF", width = 1.0):
        self.coords = (centre[0]-radius, centre[1]-radius, centre[0]+radius, centre[1]+radius)
        self.canvas = canvas
        self.colour = colour
        self.fill = fill
        self.width = width
        self.radius = radius
        self.centre = centre


    def drawOuterRing(self):
        self.outer = self.canvas.create_oval(self.coords, outline = self.colour, fill = self.fill, width = self.width)
        self.canvas.tag_lower(self.outer)

    def drawHourLines(self, num = 12, length = 20, width = 5.0):
        angle = 0.0
        angleStep = math.radians(360.0/num)

        for lines in range(num):
            startX = self.centre[0] + self.radius*math.sin(angle)
            startY = self.centre[1] - self.radius*math.cos(angle)
            endX = startX - length*math.sin(angle)
            endY = startY + length*math.cos(angle)
            lineCoords = (startX, startY, endX, endY)
            print lineCoords
            self.canvas.create_line(lineCoords, fill = self.colour, width = width)
            angle += angleStep





class clockCentre(object):

    def __init__(self, canvas, radius, centre, colour = "#000000", fill = "#000000", width = 0.0):
        self.coords = (centre[0]-radius, centre[1]-radius, centre[0]+radius, centre[1]+radius)
        self.canvas = canvas
        self.colour = colour
        self.fill = fill
        self.width = width
        self.radius = radius

    def draw(self):
        self.shape = self.canvas.create_oval(self.coords, outline = self.colour, fill = self.fill, width = self.width)
        self.canvas.tag_raise(self.shape)


class hand(object):

    def __init__(self, root, handType, canvas, length, centre, handTime = 0, colour = "#000000", fill = "#000000", width = 1.0):
        self.root = root
        self.canvas = canvas
        self.colour = colour
        self.width = width
        self.angle = 0.0
        self.length = float(length)
        self.handType = handType
        self.handTime = 0

        self.cx = centre[0]
        self.cy = centre[1]
        self.px = centre[0] + self.length*math.sin(self.angle)
        self.py = centre[1] - self.length*math.cos(self.angle)
        self.coords = (self.cx, self.cy, self.px, self.py)
        self.shape = self.canvas.create_line(self.coords, fill = self.colour, width = self.width)

    def draw(self):
        self.canvas.coords(self.shape, self.coords)
        self.root.after(1000, self.draw)
        

    def getTime(self):
        self.handTime = getTime(self.handType)
        print self.handType, self.handTime


    def setTime(self):
        if self.handType == "second" or self.handType == "minute":
            self.angle = 6*self.handTime
        elif self.handType == "hour":
            self.angle = 30*self.handTime

        self.angle %= 360
        self.px = self.cx + self.length*math.sin(math.radians(self.angle))
        self.py = self.cy -self.length*math.cos(math.radians(self.angle))
        self.coords = (self.cx, self.cy, self.px, self.py)


    def update(self):
        self.getTime()
        self.setTime()
        self.root.after(1000, self.update)


