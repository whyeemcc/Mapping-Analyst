from PyQt5 import QtCore
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from Calculate import Cal
        
class DataVisualize(QtCore.QThread):
    # return a signal as self.run is over
    finishSignal  = QtCore.pyqtSignal()
    '''
    measured data dot and median value line
    '''
    def __init__(self,fig,data,die,parent=None):
        super(DataVisualize, self).__init__(parent)
        fig.clear()
        fig.subplots_adjust(left=0.12, right=0.98, top=0.93, bottom=0.18)   
        self.ax1 = fig.add_subplot(111)
        
        self.data = data
        self.coordinate = die
        
    def __del__(self):
        self.exiting = True
        self.wait()

    def run(self):   
        if self.data == []:
            self.ax1.plot([])
        else:
            cal = Cal()
            self.ax1.axhline(cal.median(self.data), color='g', label="Median")
            self.ax1.plot(self.data,'ro')        
            self.style()
        self.finishSignal.emit()
        
    def style(self):
        try:
            self.ax1.legend(frameon=False,loc ='upper right')
            self.ax1.set_xticks(range(len(self.coordinate)))
            self.ax1.set_xticklabels(self.coordinate,rotation=30)
        except:
            pass
        
class DieVisualize(QtCore.QThread):
    # return a signal as self.run is over
    finishSignal  = QtCore.pyqtSignal()
    '''
    draw a circle signify a wafer
    square means independent die
    die's color means the difference between data and median value
    '''
    def __init__(self,fig,data,die,radius,parent=None):
        super(DieVisualize, self).__init__(parent)
        fig.clear()
        self.ax2 = fig.add_subplot(111,aspect='equal')

        self.data = data
        self.coordinate = die
        self.radius = radius
        
    def __del__(self):
        self.exiting = True
        self.wait()
        
    def run(self):
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
        self.finishSignal.emit()
        
    def style(self):
        maxDie = self.radius
        try:
            self.ax2.set_xticks(range(-maxDie,maxDie+1))
            self.ax2.set_yticks(range(-maxDie,maxDie+1))
            self.ax2.set_xlim(-maxDie,maxDie)
            self.ax2.set_ylim(-maxDie,maxDie)
        except:
            pass
        self.ax2.invert_yaxis() 
        
    def dieColor(self,die):
        index = self.coordinate.index(die)
        data = self.data[index]
        cal = Cal()
        median = cal.median(self.data)
        if median == 0 : base = 0.001
        else : base = median
        percent = abs( (data-median)/base )
        if 0 <= percent < 0.01 : return 'blue'
        elif 0.01 <= percent <= 0.05: return 'lime'
        elif 0.05 <= percent < 0.5: return 'violet'
        else: return 'red'
    
    def addCircle(self,x,y,radius,faceColor,edgeColor):
        self.ax2.add_patch(patches.Circle(
                            (x,y),          # center
                            radius,         # radius
                            facecolor = faceColor,
                            edgecolor = edgeColor)
                        )
                
    def addRectangle(self,x,y,faceColor,edgeColor):
        self.ax2.add_patch(patches.Rectangle(
                            (x-0.5,y-0.5),  # left,bottom
                            1,              # width
                            1,              # height
                            facecolor = faceColor,
                            edgecolor = edgeColor)
                        )