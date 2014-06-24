import math

class clockOuter(object):

    def __init__(self, canvas, radius, centre, colour = "#000000", fill = "#FFFFFF", width = 1.0):
        self.coords = (centre[0]-radius, centre[1]-radius, centre[0]+radius, centre[1]+radius)
        self.canvas = canvas
        self.colour = colour
        self.fill = fill
        self.width = width
        self.radius = radius

    def draw(self):
        self.canvas.create_oval(self.coords, outline = self.colour, fill = self.fill, width = self.width)


class hand(object):

    def __init__(self, handType, canvas, length, centre, angle = 0.0, colour = "#000000", fill = "#000000", width = 1.0):
        self.canvas = canvas
        self.colour = colour
        self.width = width
        self.angle = math.radians(angle)
        self.length = float(length)
        self.handType = handType

        self.cx = centre[0]
        self.cy = centre[1]
        self.px = centre[0] + self.length*math.sin(self.angle)
        self.py = centre[0] - self.length*math.cos(self.angle)
        self.coords = (self.cx, self.cy, self.px, self.py)

    def draw(self):
        self.canvas.create_line(self.coords, fill = self.colour, width = self.width)

    def tick(self):
        if self.handType == "second":
            self.angle += 6
            self.angle %= 360
            self.px = self.cx + self.length*math.sin(math.radians(self.angle))
            self.py = self.cy -self.length*math.cos(math.radians(self.angle))
            
            self.coords = (self.cx, self.cy, self.px, self.py)
