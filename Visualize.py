import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
        
class DataVisualize:
    '''
    measured data dot and median value line
    '''
    def __init__(self,fig,data,die):
        self.data = data
        self.coordinate = die
        self.ax = fig.add_subplot(111)
        fig.subplots_adjust(left=0.12, right=0.98, top=0.93, bottom=0.18)   
        self.visualize()

    def visualize(self):     
        self.ax.axhline(np.median(self.data), color='g', label="Median")
        self.ax.plot(self.data,'ro')        
        self.style()
        
    def style(self):
        self.ax.legend(frameon=False,loc ='upper right')
        self.ax.set_xticks(np.arange(len(self.coordinate)))
        self.ax.set_xticklabels(self.coordinate,rotation=30)
        
        
class DieVisualize:
    '''
    draw a circle signify a wafer
    square means independent die
    die's color means the difference between data and median value
    '''
    def __init__(self,fig,data,die,radius):
        self.data = data
        self.coordinate = die
        self.radius = radius
        self.ax = fig.add_subplot(111,aspect='equal')
        self.ax.clear()
        self.visualize()
        
    def visualize(self):
        maxDie = self.radius
        # draw a circle
        self.addCircle(0,0,maxDie,'none','black')
        # draw squares
        for die in [(x,y) for x in range(-maxDie+1,maxDie) for y in range(-maxDie+1,maxDie)]:
            x,y = die[0],die[1]
            if die in self.coordinate:
                self.addRectangle(x,y,self.dieColor(die),'white')
            else:
                if (abs(x)+0.5)**2 + (abs(y)+0.5)**2 <= maxDie**2:
                    self.addRectangle(x,y,'grey','white')        
        self.style()
        
    def style(self):
        maxDie = self.radius
        self.ax.set_xticks(range(-maxDie,maxDie+1))
        self.ax.set_yticks(range(-maxDie,maxDie+1))
        self.ax.set_xlim(-maxDie,maxDie)
        self.ax.set_ylim(-maxDie,maxDie)
        self.ax.invert_yaxis()
    
    def dieColor(self,die):
        index = self.coordinate.index(die)
        data = self.data[index]
        median = np.median(self.data)
        if median == 0 : base = 0.001
        else : base = median
        percent = abs( (data-median)/base )
        if 0 <= percent < 0.01 : return 'blue'
        elif 0.01 <= percent <= 0.05: return 'lime'
        elif 0.05 <= percent < 0.5: return 'violet'
        else: return 'red'
    
    def addCircle(self,x,y,radius,faceColor,edgeColor):
        self.ax.add_patch(patches.Circle(
                            (x,y),          # center
                            radius,         # radius
                            facecolor = faceColor,
                            edgecolor = edgeColor)
                        )
                
    def addRectangle(self,x,y,faceColor,edgeColor):
        self.ax.add_patch(patches.Rectangle(
                            (x-0.5,y-0.5),  # left,bottom
                            1,              # width
                            1,              # height
                            facecolor = faceColor,
                            edgecolor = edgeColor)
                        )