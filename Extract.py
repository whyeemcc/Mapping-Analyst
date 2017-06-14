import sys,os
import re
import numpy as np

class ItemAll:
    def __init__(self,content):
        linesCount = len(content)
        # collect die's coordinate
        self.coordinate = []
        # collect ordered items
        self.allList = []

        i = 0
        while i < linesCount:
            if i == 0:
                i = i + 1
                while content[i][0] != '=':
                    x = eval(content[i].split(',')[0])
                    y = eval(content[i].split(',')[1])
                    self.coordinate.append((x,y))
                    i = i + 1                    
            elif 'SYS_WAFERID' in content[i]:
                waferID = content[i].rstrip('\n')
                waferIDrow = i
                # tempList conclude all items of one waferID
                tempList = []
                # two row below 'SYS_WAFERID' is data
                i = i + 2
                while content[i][0] != '=':
                    item = content[i].split(',')[0]
                    # tempList = ['ID1_MA012H_NMOS12_d9_d9' , 'ID2_MA012H_NMOS12_d9_d9' , ...]
                    tempList.append(item)
                    i = i + 1
                    # the last row occur:
                    if i == linesCount : break
                # allList = [('SYS_WAFERID,3',27,['ID1_MA012H_NMOS12_d9_d9', ...]),...]
                self.allList.append((waferID,waferIDrow,tempList))
            i = i + 1

            
class RegularData:
    def __init__(self,line,rawDie):
        self.line = line
        self.rawDie = rawDie
        self.radius = self.radius()
        self.cut()
  
    def cut(self):
        '''
        replace the error value +3.000000E+30 by blank value
        then delete the blank values and it's corresponding die 
        '''
        rawData = self.line.split(',')[4:]
        temps=[]
        for i,data in enumerate(rawData): 
            if data in ['+3.000000E+30','']:
                temps.append(i)
        self.PlotData,self.PlotDie=[],[]
        for j in range(0,len(rawData)):
            if j not in temps:
                self.PlotData.append(rawData[j])
                self.PlotDie.append(self.rawDie[j])
        self.PlotData = [eval(x) for x in self.PlotData]
        
    def radius(self):
        # max value of coordinates
        s = str(self.rawDie).lstrip('[').rstrip(']').replace('(','').replace(')','')
        maxXY = max([abs(eval(x)) for x in s.split(',') if x.strip()])
        return maxXY + 1            
            
            
class Statistic:
    def __init__(self,line,Data,Die):
        self.line = line
        self.Data = Data
        self.Die = Die
        
        self.itemSplit()
        self.numerical() 
    
    def itemSplit(self):
        item = self.line.split(',')[0]
        comp = item.split('_')

        self.L = comp[-1].replace('d','.')
        self.W = comp[-2].replace('d','.')

        # check the 2nd item if it is testkey format
        m = re.match('[A-Z]+[0-9]+[A-Z]',comp[1]) 
        if m is not None:
            '''
            testkey name locate in 2nd positon
            such as : 'RKV_MR056D_R4TNWAA_1d8_2'
            '''
            self.Testkey = m.group()
            self.Etest = comp[0]
        else:
            '''
            testkey name locate in 3rd positon
            such as : 'C1_A1_MC25A_NMCAP_MIS_d67_d61'
            '''
            self.Testkey = re.match('[A-Z]+[0-9]+[A-Z]',comp[2]).group()
            self.Etest = comp[0]+'_'+comp[1]
        lenF = len(self.Etest + self.Testkey)+2
        lenB = len(self.W + self.L)+2
        self.Device = item[ lenF : len(item)-lenB ]
        self.Unit = self.line.split(',')[3]
        
    def numerical(self):
        self.DieCount   = str(len(self.Die))
        self.Median     = str(np.median(self.Data))
        self.Average    = str(np.mean(self.Data))
        self.Max        = str(np.max(self.Data))
        self.Min        = str(np.min(self.Data))
        self.Standard   = str(np.std(self.Data))
        self._3sigma    = str(3*np.std(self.Data))
        self.sigmMed    = '%.2f'%abs(np.std(self.Data)/np.median(self.Data)*100)+'%'