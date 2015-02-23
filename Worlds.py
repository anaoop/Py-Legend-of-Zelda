from tkinter import *
import random
#=================== The World Generation =====================    
class squaregrid:
    def __init__ (self,canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.stones = []
        self.stoneimage = PhotoImage(file = 'Graphics\Stone.png')
        self.grass = []
        self.grassimage1 = PhotoImage(file = 'Graphics\Grass1.png')
        self.grassimage2 = PhotoImage(file = 'Graphics\Grass2.png')
        self.water = []
        self.waterimage1 = PhotoImage(file = 'Graphics\Water1.png')
        self.waterimage2 = PhotoImage(file = 'Graphics\Water2.png')


        
        self.TrafficLightList = []
        self.RobotList = []

    def drawgrid(self):
        for y in range(self.height+1):
            for x in range(self.width+1):
                TType = self.draw_tile((x,y))
                self.drawtile((x,y),TType)

    def drawtile(self,gridid,TType):
        x,y = gridid
        
        x = x*16
        y = y*16

        if TType == 'Stone Tile': self.canvas.create_image(x,y,anchor="nw",image=self.stoneimage)
        
        if TType == 'Grass Tile':
            rand = random.randint(1, 100)
            if rand <95:
                self.canvas.create_image(x,y,anchor="nw",image=self.grassimage1)
            elif rand >=95:
                self.canvas.create_image(x,y,anchor="nw",image=self.grassimage2)
 
 
        if TType == 'Water Tile':
            rand = random.randint(1, 100)
            if rand <80:
                self.canvas.create_image(x,y,anchor="nw",image=self.waterimage1)
            elif rand  >=80:
                self.canvas.create_image(x,y,anchor="nw",image=self.waterimage2)

        

        #print ((x,y), TType)

    def draw_tile(self,gridid):

        r = ''
    
        if gridid in self.grass: r = 'Grass Tile'
        if gridid in self.water: r = 'Water Tile'
        if gridid in self.stones: r = 'Stone Tile'
        
    
        return r

    def neighbors(self,gridid):
        (x,y) = gridid
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.passable,results)
        results = filter(self.in_bounds,results)
        return results

    def passable(self, gridid):
       return gridid not in self.water and gridid not in self.stones

    def in_bounds(self, gridid):
        (x, y) = gridid
        return 0 <= x < self.width and 0 <= y < self.height

