import sys,os
from PyQt5 import QtGui,QtCore,QtWidgets
from Ui import Interface
from Extract import ItemAll,RegularData,Statistic
from Visualize import DataVisualize,DieVisualize
from Calculate import Cal

class Main(Interface):

    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.stateCheck()
        
    def judgeFile(self,fname):
        if fname == '':
            pass
        elif os.path.splitext(fname)[1] != '.dat':
            QtWidgets.QMessageBox.critical(self,'Error','文件后缀名不正确，请载入 .dat 文件。')
        else:
            self.label_fileNow_C.setText(os.path.split(fname)[1])
            self.Search_Line.setText('')
            try:
                self.loadFile(fname)
            except:
                QtWidgets.QMessageBox.critical(self,"Error","解析文件失败，请检查数据格式。")
                    
    def loadFile(self,fname):
        self.content = open(fname,'r').readlines()
        itemAll = ItemAll(self.content)
        self.coordinate = itemAll.coordinate
        self.radius = itemAll.radius()
        self.allList = itemAll.allList
        self.totalDie = str(len(self.coordinate))
        self.loadID()

    def loadID(self):
        self.Id_Select.clear()
        for i,v in enumerate(self.allList):
            self.Id_Select.insertItem(i,v[0].split(',')[1])
        self.loadList()

    def loadList(self):
        try:
            self.list = self.allList[self.Id_Select.currentIndex()][2]    
            self.Item_List.clear()  
            key = self.Search_Line.text()
            '''
            filter: 
            if it is none in the searchline, show the all of item
            else show the item which contain the key words in searchline
            '''
            if key == '':
                listShow = self.list
            else:
                listShow = [x for x in self.list if key in x]       
            # reload the filtered items in the QListWidget
            for item in listShow:
                self.Item_List.addItem(item)
            self.Item_List.setCurrentRow(0)              
        except AttributeError:
            pass
        
    def justDoIt(self):
        if self.Item_List.currentRow() == -1:
            pass
        else:
            currentIndex = self.Item_List.currentRow()
            currentItem = self.Item_List.item(currentIndex).text()
            waferIDrow = self.allList[self.Id_Select.currentIndex()][1]
            dataRow = waferIDrow + 2 + self.list.index(currentItem)
            self.line = self.content[dataRow].rstrip('\n')
            # show the original line row index on the statusBar
            self.statusBar().showMessage('原始文件所在行数：'+str(dataRow+1))

            # extract data informations from the raw file
            regularData = RegularData(self.line,self.coordinate)
            self.plotDie = regularData.PlotDie
            self.plotData = regularData.PlotData
           
            if self.plotData == []:
                QtWidgets.QMessageBox.critical(self,'数据为空,可能是以下原因：',
                "1：该行数据全为空；\n2：踢除错误值(+3.000000E+30)后数据全为空。")
                self.showIt([],[])
            else:
                # check sigma flag status 
                if self.Sigma_Flag.isChecked():
                    cal = Cal()
                    fd = cal.sigmaFilter(self.plotData,self.plotDie)
                    self.plotData,self.plotDie = fd[0],fd[1]
                # draw figure and reload the Die_Select QComboBox
                self.showIt(self.plotData,self.plotDie)
                self.loadDies(self.plotDie)
                # two new var for recording delete dies
                self.pltDatTemp = self.plotData[:]
                self.pltDieTemp = self.plotDie[:]    

    def showIt(self,PlotData,PlotDie):
        # show the curve and wafer image
        self.thread1 = DataVisualize(self.fig1,PlotData,PlotDie)
        self.thread2 = DieVisualize(self.fig2,PlotData,PlotDie,self.radius)
        self.thread1.finishSignal.connect(self.canvas1.draw)
        self.thread2.finishSignal.connect(self.canvas2.draw)
        self.thread1.start()
        self.thread2.start()
        # show the information and statistical results
        numer = Statistic(self.line,PlotData)
        self.label_Etest_C.setText(numer.Etest)
        self.label_Testkey_C.setText(numer.Testkey)
        self.label_Device_C.setText(numer.Device)
        self.label_W_C.setText(numer.W)
        self.label_L_C.setText(numer.L)
        self.label_Unit_C.setText(numer.Unit)
        self.label_DieCount_C.setText(numer.DieCount+' (%s)'%self.totalDie)
        self.label_Median_C.setText(numer.Median)
        self.label_Average_C.setText(numer.Average)
        self.label_Max_C.setText(numer.Max)
        self.label_Min_C.setText(numer.Min)
        self.label_Standard_C.setText(numer.Standard)
        self.label_3sigma_C.setText(numer._3sigma)    
        self.label_sigmMed_C.setText(numer.sigmMed) 
  
    def loadDies(self,dies):
        self.Die_Select.clear()
        for i,d in enumerate(dies):
            self.Die_Select.insertItem(i,str(d))
    
    def delDie(self):
        try:
            if len(self.pltDieTemp) == 0:
                QtWidgets.QMessageBox.critical(self,'警告',"该行数据为空。")
            elif len(self.pltDieTemp) == 1:
                QtWidgets.QMessageBox.critical(self,'警告',"只剩一个 Die ，不能继续剔除。")
            else:
                index = self.Die_Select.currentIndex()
                del self.pltDatTemp[index]
                del self.pltDieTemp[index]
                # draw figure and reload the Die_Select QComboBox
                self.showIt(self.pltDatTemp,self.pltDieTemp)
                self.loadDies(self.pltDieTemp)    
        except AttributeError:
            pass        
    
    def reShow(self):
        self.Item_List.setCurrentRow(0)
        self.justDoIt()        
    
    def changeId(self):
        self.loadList()
        self.reShow()
    
    def stateCheck(self):
        # signals and slots
        self.Search_Line.textChanged.connect(self.loadList)
        self.Search_Line.returnPressed.connect(self.reShow)
        self.Id_Select.currentIndexChanged.connect(self.changeId)
        self.Item_List.clicked.connect(self.justDoIt)
        self.Item_List.itemActivated.connect(self.justDoIt)
        self.Sigma_Flag.clicked.connect(self.justDoIt)
        self.Delete_Button.clicked.connect(self.delDie)
        self.Reset_Button.clicked.connect(self.justDoIt)
               
               
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())