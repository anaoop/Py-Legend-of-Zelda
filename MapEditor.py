from tkinter import *
import random


import tkinter.filedialog as tkfd

class surface():
    def __init__(self):
        self.window = Tk()
        self.canvas = ''
        self.canvas_Tiles = ''
        self.TType = '1'
        self.TNum = '1'
        self.x = 0
        self.y = 0
        self.TileWindow = {}
        self.MapData = {}
        self.MapExport = []
        self.MapName = ''
        self.rotation = 0
        self.screenlocation = (0,0)
        
        self.grassimage1 = PhotoImage(file = 'Graphics\Grass1.png')
        self.grassimage2 = PhotoImage(file = 'Graphics\Grass2.png')
        self.waterimage1 = PhotoImage(file = 'Graphics\Water1.png')
        self.waterimage2 = PhotoImage(file = 'Graphics\Water2.png')
        self.stoneimage = PhotoImage(file = 'Graphics\Stone.png')
        self.flowerimage = PhotoImage(file = 'Graphics\Flower.png')
        self.stumpimage = [[PhotoImage(file = 'Graphics\TLStump.png'),
                           PhotoImage(file = 'Graphics\BLStump.png')],
                           [PhotoImage(file = 'Graphics\TRStump.png'),
                           PhotoImage(file = 'Graphics\BRStump.png')]]

        self.I1 = PhotoImage(file = 'Graphics\GrassCliffN.png')
        self.i1 = PhotoImage(file = 'Graphics\TopCliffN.png')
        self.I2 = PhotoImage(file = 'Graphics\TopCliffN.png')
        self.I3 = PhotoImage(file = 'Graphics\WaterCliffN.png')
        self.I4 = PhotoImage(file = 'Graphics\WaterN.png')
        
        self.I5 = PhotoImage(file = 'Graphics\GrassCliffNE.png')
        self.I6 = PhotoImage(file = 'Graphics\TopCliffNE.png')
        self.I7 = PhotoImage(file = 'Graphics\MiddleCliffNE.png')
        self.I8= PhotoImage(file = 'Graphics\WaterCliffNE.png')
        self.I9 = PhotoImage(file = 'Graphics\WaterCLiffNtoNE.png')
        self.I10 = PhotoImage(file = 'Graphics\WaterNE.png')
        self.I11 = PhotoImage(file = 'Graphics\WaterOuterNE.png')
        self.I12 = PhotoImage(file = 'Graphics\WaterOuterNE2.png')

        self.I13 = PhotoImage(file = 'Graphics\TopCliffE.png')
        self.I14 = PhotoImage(file = 'Graphics\BottomCliffE.png')
        self.I15 = PhotoImage(file = 'Graphics\WaterCliffE.png')

        self.I16 = PhotoImage(file = 'Graphics\TopCliffNW.png') #p
        self.I17 = PhotoImage(file = 'Graphics\CliffMiddleNW.png') #q
        self.I18 = PhotoImage(file = 'Graphics\CliffBottomNW.png') #r

        self.I19 = PhotoImage(file = 'Graphics\CliffGrassNW.png') #s
        self.I20 = PhotoImage(file = 'Graphics\WaterCliffNW.png') #t
        
        self.I21 = PhotoImage(file = 'Graphics\CliffTopW.png') #u
        self.I22 = PhotoImage(file = 'Graphics\MiddleCliffW.png') #v
        self.I23 = PhotoImage(file = 'Graphics\WaterW.png') #w
        self.I24= PhotoImage(file = 'Graphics\GrassCliffSW.png') #x

        self.I25 = PhotoImage(file = 'Graphics\TopCliffSW.png') #y 
        self.I26 = PhotoImage(file = 'Graphics\GrassSW.png') #z
        
        self.I27 = PhotoImage(file = 'Graphics\BottomCliffSW.png') #A 
        self.I28 = PhotoImage(file = 'Graphics\WaterSW.png') #B
        self.I29 = PhotoImage(file = 'Graphics\WaterCornerSW.png') #C 
        self.I30 = PhotoImage(file = 'Graphics\GrassCliffS.png') #D
        self.I31 = PhotoImage(file = 'Graphics\TopCliffS.png') #E 
        self.I32 = PhotoImage(file = 'Graphics\MiddleCliffS.png')# F
        self.I33 = PhotoImage(file = 'Graphics\BottomCliffS.png')# G
        self.I34 = PhotoImage(file = 'Graphics\WaterS.png')# H
        self.I35 = PhotoImage(file = 'Graphics\GrassSE.png')# I
        self.I36 = PhotoImage(file = 'Graphics\GrassCliffSE.png')# J
        self.I37 = PhotoImage(file = 'Graphics\TopCliffSE.png')# K
        self.I38 = PhotoImage(file = 'Graphics\BottomCliffSE.png')# L
        self.I39 = PhotoImage(file = 'Graphics\WaterCliffSE.png')# M
        self.I40 = PhotoImage(file = 'Graphics\CornerWaterSE.png')# N
        #self.I41 = PhotoImage(file = 'Graphics\.png')# O
        #self.I42 = PhotoImage(file = 'Graphics\.png')# P
        #self.I43 = PhotoImage(file = 'Graphics\.png')# Q
        #self.I44 = PhotoImage(file = 'Graphics\.png')# R
        #self.I45 = PhotoImage(file = 'Graphics\.png')# S
        #self.I46 = PhotoImage(file = 'Graphics\.png')# T
        #self.I47 = PhotoImage(file = 'Graphics\.png')# U
        #self.I48 = PhotoImage(file = 'Graphics\.png')# V
        #self.I49 = PhotoImage(file = 'Graphics\.png')# W
        #self.I50 = PhotoImage(file = 'Graphics\.png')# X
        #self.I51 = PhotoImage(file = 'Graphics\.png')# Y
        #self.I52 = PhotoImage(file = 'Graphics\.png')# Z
        
                      
        

    def openfile(self):
        
        filename = tkfd.askopenfilename()

        self.create(40,25)
         
        y=-1
        
        with open(filename,'r') as f:
            for line in f:
                y+=1
                x=-1
                for char in line:
                    x+=1
                    self.TType = char
                    self.draw(self.canvas,self.TType,x*16,y*16)
                    

    
        
        
    def movecamera(self,direction):
        self.canvas.delete(ALL)
    
        if direction == 'right':            
            self.screenlocation = (self.screenlocation[0]+35,self.screenlocation[1])
            print(self.MapData[(2,2)])
            p = self.screenlocation[0] 
            r = self.screenlocation[1] 

            for s in range (0,35):
                for q in range (0,20):
                    if ( r+q,p+s) in self.MapData: (self.draw(self.canvas,self.MapData[( r+q,p+s)],s*16,q*16))

        if direction == 'left':
            
            self.screenlocation = (self.screenlocation[0]-35,self.screenlocation[1])

            p = self.screenlocation[0] 
            r = self.screenlocation[1]

            for s in range (0,35):
                for q in range (0,20):
                    
                    if ( r+q,p+s) in self.MapData:
                        self.draw(self.canvas,self.MapData[( r+q,p+s)],s*16,q*16)
                        
                    

        if direction == 'up':
            
            self.screenlocation = (self.screenlocation[0],self.screenlocation[1]-20)

            p = self.screenlocation[0] 
            r = self.screenlocation[1] 

            for s in range (0,35):
                for q in range (0,20):
                    if ( r+q,p+s) in self.MapData: self.draw(self.canvas,self.MapData[( r+q,p+s)],s*16,q*16)

        if direction == 'down':
            
            self.screenlocation = (self.screenlocation[0],self.screenlocation[1]+20)

            p = self.screenlocation[0] 
            r = self.screenlocation[1] 

            for s in range (0,35):
                for q in range (0,20):
                    if ( r+q,p+s) in self.MapData: self.draw(self.canvas,self.MapData[( r+q,p+s)],s*16,q*16)
                    
        print(self.screenlocation)
                

    def reset(self):
        for x in range (0,self.x):
            for y in range(0,self.y):
                self.draw(self.canvas,'1',x*16,y*16)

    def savemap(self):
        self.MapExport.clear()
        for x in range (0,self.y):
            for y in range (0,self.x):
                self.MapExport.append(self.MapData[(x,y)])

        self.MapName = tkfd.asksaveasfile(mode = 'w', defaultextension=".txt")
        
        if self.MapName is None:
            return #stops trying to save the map if user presses cancel
        
        p = 0
        for item in self.MapExport:
            p+=1
            if p == self.x:
                self.MapName.write(str(item) + '\n')
                p = 0
            else:
               self.MapName.write(str(item))
               
        
    def draw(self,canvas,TType,x,y):
                
        if TType == '1':
            rand = random.randint(1, 100)
            if rand <95:
                canvas.create_image(x,y,anchor="nw",image=self.grassimage1)
            elif rand >=95:
                canvas.create_image(x,y,anchor="nw",image=self.grassimage2)
 
        if TType == '2':
            rand = random.randint(1, 100)
            if rand <80:
                canvas.create_image(x,y,anchor="nw",image=self.waterimage1)
            elif rand  >=80:
                canvas.create_image(x,y,anchor="nw",image=self.waterimage2)

        if TType == '3': canvas.create_image(x,y,anchor="nw",image=self.stoneimage)
        if TType == '4': canvas.create_image(x,y,anchor="nw",image=self.stumpimage[0][self.rotation])
        if TType == '5': canvas.create_image(x,y,anchor="nw",image=self.stumpimage[1][self.rotation])
        if TType == '6': canvas.create_image(x,y,anchor="nw",image=self.flowerimage)
        
        if TType == 'a': canvas.create_image(x,y,anchor="nw",image=self.I1)
        if TType == 'b': canvas.create_image(x,y,anchor="nw",image=self.I2)
        if TType == 'c': canvas.create_image(x,y,anchor="nw",image=self.I3)
        if TType == 'd': canvas.create_image(x,y,anchor="nw",image=self.I4)
        if TType == 'e': canvas.create_image(x,y,anchor="nw",image=self.I5)
        if TType == 'f': canvas.create_image(x,y,anchor="nw",image=self.I6)
        if TType == 'g': canvas.create_image(x,y,anchor="nw",image=self.I7)
        if TType == 'h': canvas.create_image(x,y,anchor="nw",image=self.I8)
        if TType == 'i': canvas.create_image(x,y,anchor="nw",image=self.I9)
        if TType == 'j': canvas.create_image(x,y,anchor="nw",image=self.I10)
        if TType == 'k': canvas.create_image(x,y,anchor="nw",image=self.I11)
        if TType == 'l': canvas.create_image(x,y,anchor="nw",image=self.I12)
        if TType == 'm': canvas.create_image(x,y,anchor="nw",image=self.I13)
        if TType == 'n': canvas.create_image(x,y,anchor="nw",image=self.I14)
        if TType == 'o': canvas.create_image(x,y,anchor="nw",image=self.I15)
        if TType == 'p': canvas.create_image(x,y,anchor="nw",image=self.I16)
        if TType == 'q': canvas.create_image(x,y,anchor="nw",image=self.I17)
        if TType == 'r': canvas.create_image(x,y,anchor="nw",image=self.I18)
        if TType == 's': canvas.create_image(x,y,anchor="nw",image=self.I19)
        if TType == 't': canvas.create_image(x,y,anchor="nw",image=self.I20)
        if TType == 'u': canvas.create_image(x,y,anchor="nw",image=self.I21)
        if TType == 'v': canvas.create_image(x,y,anchor="nw",image=self.I22)
        if TType == 'w': canvas.create_image(x,y,anchor="nw",image=self.I23)
        if TType == 'x': canvas.create_image(x,y,anchor="nw",image=self.I24)
        if TType == 'y': canvas.create_image(x,y,anchor="nw",image=self.I25)
        if TType == 'z': canvas.create_image(x,y,anchor="nw",image=self.I26)

        if TType == 'A': canvas.create_image(x,y,anchor="nw",image=self.I27)
        if TType == 'B': canvas.create_image(x,y,anchor="nw",image=self.I28)
        if TType == 'C': canvas.create_image(x,y,anchor="nw",image=self.I29)
        if TType == 'D': canvas.create_image(x,y,anchor="nw",image=self.I30)
        if TType == 'E': canvas.create_image(x,y,anchor="nw",image=self.I31)
        if TType == 'F': canvas.create_image(x,y,anchor="nw",image=self.I32)
        if TType == 'G': canvas.create_image(x,y,anchor="nw",image=self.I33)
        if TType == 'H': canvas.create_image(x,y,anchor="nw",image=self.I34)
        if TType == 'I': canvas.create_image(x,y,anchor="nw",image=self.I35)
        if TType == 'J': canvas.create_image(x,y,anchor="nw",image=self.I36)
        if TType == 'K': canvas.create_image(x,y,anchor="nw",image=self.I37)
        if TType == 'L': canvas.create_image(x,y,anchor="nw",image=self.I38)
        if TType == 'M': canvas.create_image(x,y,anchor="nw",image=self.I39)
        if TType == 'N': canvas.create_image(x,y,anchor="nw",image=self.I40)
        #if TType == 'O': canvas.create_image(x,y,anchor="nw",image=self.I41)
        #if TType == 'P': canvas.create_image(x,y,anchor="nw",image=self.I42)
        #if TType == 'Q': canvas.create_image(x,y,anchor="nw",image=self.I43)
        #if TType == 'R': canvas.create_image(x,y,anchor="nw",image=self.I44)
        #if TType == 'S': canvas.create_image(x,y,anchor="nw",image=self.I45)
        #if TType == 'T': canvas.create_image(x,y,anchor="nw",image=self.I46)
        #if TType == 'U': canvas.create_image(x,y,anchor="nw",image=self.I47)
        #if TType == 'V': canvas.create_image(x,y,anchor="nw",image=self.I48)
        #if TType == 'W': canvas.create_image(x,y,anchor="nw",image=self.I49)
        #if TType == 'X': canvas.create_image(x,y,anchor="nw",image=self.I50)
        #if TType == 'Y': canvas.create_image(x,y,anchor="nw",image=self.I51)
        #if TType == 'Z': canvas.create_image(x,y,anchor="nw",image=self.I52)

        
        self.MapData[(y//16,x//16)] = self.TType
        
          

    def Click(self,event):
        x=round_down(event.x,16)
        y=round_down(event.y,16)
        self.draw(self.canvas,self.TType,x,y)
        
    def TClick(self,event):

        x=(round_down(event.x,16))//16
        y=(round_down(event.y,16))//16
        
        Tile = self.TileWindow[(x,y)]

        if not Tile:
            return
       
        self.TType = Tile
        
    def Key(self,event):
        
        if event.char.isdigit() == True:            
            self.TType = event.char
        else:
                
            if event.char == 'p':
                print(self.MapData)
                
            if event.char == 's':
                self.savemap()

            if event.char =='i':
                self.movecamera('up')

            if event.char =='j':
                self.movecamera('left')

            if event.char =='k':
                self.movecamera('down')

            if event.char =='l':
                self.movecamera('right')

            if event.char == 'r':
                self.rotation +=1
                if self.rotation ==2: self.rotation = 0

            
                    

    def create(self,x,y):

        self.x = x
        self.y = y
    
        height = y*16
        width = x*16

        
        self.canvas = Canvas(self.window,width=width-2, height=height-2, bg='black')
        self.canvas_Tiles = Canvas(self.window,width=320, height=height, bg='white')

        self.canvas.grid(row = 0,column = 0)
        self.canvas_Tiles.grid(row = 0,column =1,rowspan=2)

        
        
        q=-1
        with open('TilesforUse.txt','r') as f:
            for line in f:
                q+=1
                x=-1
                for char in line:
                    if char =='\n': continue
                    x+=1
                    self.TType = char
                    self.draw(self.canvas_Tiles,self.TType,x*16,q*16)
                    self.TileWindow[(x,q)] = char
   
        self.TType = '1'

        for x in range (0,self.x):
            for y in range(0,self.y):
                self.draw(self.canvas,self.TType,x*16,y*16)


        self.canvas.bind('<Button-1>',self.Click)
        self.canvas.bind('<B1-Motion>',self.Click)
        self.canvas_Tiles.bind('<Button-1>',self.TClick)
        self.window.bind_all('<Key>',self.Key)
        #self.window.bind('<Right>',self.movecamera('right'))
        #self.window.bind('<Left>',self.movecamera('left'))
        #self.window.bind('<Up>',self.movecamera('up'))                         
        #self.window.bind('<Down>',self.movecamera('down'))
        

        

        #self.canvas_Tiles.create_rectangle(2,2,25,height-1)
               
def round_down(num, divisor):
    return num - (num%divisor)
def addcords(cord1,cord2):
    x1,y1 = cord1
    x2,y2 = cord2

    x3,y3 = (x1+x2,y1+y2)

    return (x3,y3)


def something():
    surface1 = surface()
    #surface1.create(40,25)
    surface1.openfile()
    print (surface1.MapData[(2,2)])
    surface1.window.mainloop()
    
something()

