import sys,os
from PyQt5 import QtGui,QtCore,QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from Extract import ItemAll,RegularData,Statistic
from Visualize import DataVisualize,DieVisualize
from Calculate import Cal
from Layout import Layout
from Help import Help
import images_qr

class Interface(QtWidgets.QMainWindow):

    def __init__(self,parent=None):
        super(Interface, self).__init__(parent)
        self.initUI() 
    
    def initUI(self):
        self.widget()
        self.label()
        self.draw()
        self.spec()
        self.menu()
        self.layout()
        self.statusBar()
        self.stateCheck()
        self.setAcceptDrops(True)
        # x,y,width,length
        self.setGeometry(100, 100, 1300, 650)
        self.setWindowTitle('Mapping Analyst')
        self.setWindowIcon(QtGui.QIcon(':/images/logo.gif')) 
        self.show()

    def widget(self):       
        self.Item_List = QtWidgets.QListWidget(self)
        self.Id_Select = QtWidgets.QComboBox(self) 
        self.Search_Line = QtWidgets.QLineEdit(self)
        self.Search_Button = QtWidgets.QPushButton("筛选")  
        self.Sigma_Flag = QtWidgets.QRadioButton("循环筛除距离 Median 值 3σ 以外的 die")
        self.Die_Select = QtWidgets.QComboBox(self)
        self.Delete_Button = QtWidgets.QPushButton("剔除该die")
        self.Reset_Button = QtWidgets.QPushButton("重置")
        # set Font style
        self.Search_Button.setFont(QtGui.QFont("Microsoft YaHei"))
        self.Sigma_Flag.setFont(QtGui.QFont("Microsoft YaHei"))
        self.Delete_Button.setFont(QtGui.QFont("Microsoft YaHei"))
        self.Reset_Button.setFont(QtGui.QFont("Microsoft YaHei"))
        self.Item_List.setFont(QtGui.QFont('Microsoft YaHei',9, QtGui.QFont.Bold))
               
    def draw(self):        
        self.fig1 = plt.figure(facecolor=('none'))
        self.fig2 = plt.figure(facecolor=('none'))
        # canvas1 for showing data dot
        self.canvas1 = FigureCanvas(self.fig1)
        # toolbar for canvas1
        self.toolbar = NavigationToolbar(self.canvas1, self)
        # canvas2 for showing wafer and die image
        self.canvas2 = FigureCanvas(self.fig2)        

    def label(self):
        # fixed label
        self.label_fileNow   = QtWidgets.QLabel("当前文件:\t")
        self.label_waferID   = QtWidgets.QLabel("WaferID:")
        self.label_Etest     = QtWidgets.QLabel("Etest:")
        self.label_Testkey   = QtWidgets.QLabel("Testkey:")
        self.label_Device    = QtWidgets.QLabel("Device:")
        self.label_W         = QtWidgets.QLabel("W:")
        self.label_L         = QtWidgets.QLabel("L:")
        self.label_Unit      = QtWidgets.QLabel("Unit:")
        self.label_DieCount  = QtWidgets.QLabel("DieCount:")        
        self.label_Median    = QtWidgets.QLabel("Median:")
        self.label_Average   = QtWidgets.QLabel("Average:")
        self.label_Max       = QtWidgets.QLabel("Max:")
        self.label_Min       = QtWidgets.QLabel("Min:")
        self.label_Standard  = QtWidgets.QLabel("Standard(σ):")
        self.label_3sigma    = QtWidgets.QLabel("3sigma(3σ):")
        self.label_sigmMed   = QtWidgets.QLabel("σ/median:")
        # calculated value
        self.label_fileNow_C    = QtWidgets.QLabel("")
        self.label_Etest_C      = QtWidgets.QLabel("")
        self.label_Testkey_C    = QtWidgets.QLabel("")
        self.label_Device_C     = QtWidgets.QLabel("")
        self.label_W_C          = QtWidgets.QLabel("")
        self.label_L_C          = QtWidgets.QLabel("")
        self.label_Unit_C       = QtWidgets.QLabel("")
        self.label_DieCount_C   = QtWidgets.QLabel("")
        self.label_Median_C     = QtWidgets.QLabel("")
        self.label_Average_C    = QtWidgets.QLabel("")
        self.label_Max_C        = QtWidgets.QLabel("")
        self.label_Min_C        = QtWidgets.QLabel("")
        self.label_Standard_C   = QtWidgets.QLabel("")
        self.label_3sigma_C     = QtWidgets.QLabel("")
        self.label_sigmMed_C    = QtWidgets.QLabel("")
        self.setStyleSheet("QLabel{font-family:Microsoft YaHei}")
        
    def layout(self):
        layout = Layout(
                        self.Item_List,
                        self.toolbar,
                        self.canvas1,
                        self.canvas2
                        )
        self.setCentralWidget(layout.wid)
        
        layout.fileFrame.addWidget(self.label_fileNow)
        layout.fileFrame.addWidget(self.label_fileNow_C)
        layout.fileFrame.addStretch()
        
        layout.idFrame.addWidget(self.label_waferID)
        layout.idFrame.addWidget(self.Id_Select)   
        layout.searchFrame.addWidget(self.Search_Line)
        layout.searchFrame.addWidget(self.Search_Button)

        layout.m1Frame.addWidget(QtWidgets.QLabel(""))
        layout.m1Frame.addWidget(QtWidgets.QLabel(""))
        layout.m1Frame.addWidget(QtWidgets.QLabel(""))
        layout.m1Frame.addWidget(self.label_Etest)
        layout.m1Frame.addWidget(self.label_Testkey)
        layout.m1Frame.addWidget(self.label_Device)
        layout.m1Frame.addWidget(self.label_W)
        layout.m1Frame.addWidget(self.label_L)
        layout.m1Frame.addWidget(self.label_Unit)
        layout.m1Frame.addWidget(self.label_DieCount)
        layout.m1Frame.addWidget(self.label_Median)
        layout.m1Frame.addWidget(self.label_Average)
        layout.m1Frame.addWidget(self.label_Max)
        layout.m1Frame.addWidget(self.label_Min)
        layout.m1Frame.addWidget(self.label_Standard)
        layout.m1Frame.addWidget(self.label_3sigma) 
        layout.m1Frame.addWidget(self.label_sigmMed) 
        layout.m1Frame.addStretch()
        layout.m1Frame.setSpacing(10) 
        layout.m2Frame.addWidget(QtWidgets.QLabel(""))
        layout.m2Frame.addWidget(QtWidgets.QLabel(""))
        layout.m2Frame.addWidget(QtWidgets.QLabel(""))
        layout.m2Frame.addWidget(self.label_Etest_C)
        layout.m2Frame.addWidget(self.label_Testkey_C)
        layout.m2Frame.addWidget(self.label_Device_C)
        layout.m2Frame.addWidget(self.label_W_C)
        layout.m2Frame.addWidget(self.label_L_C)
        layout.m2Frame.addWidget(self.label_Unit_C)
        layout.m2Frame.addWidget(self.label_DieCount_C)
        layout.m2Frame.addWidget(self.label_Median_C)
        layout.m2Frame.addWidget(self.label_Average_C)
        layout.m2Frame.addWidget(self.label_Max_C)
        layout.m2Frame.addWidget(self.label_Min_C)
        layout.m2Frame.addWidget(self.label_Standard_C)
        layout.m2Frame.addWidget(self.label_3sigma_C) 
        layout.m2Frame.addWidget(self.label_sigmMed_C)
        layout.m2Frame.addStretch()  
        layout.m2Frame.setSpacing(10)         

        layout.specFrame.addWidget(self.label_spec1)
        layout.specFrame.addWidget(self.label_Blue)        
        layout.specFrame.addWidget(self.label_spec2)
        layout.specFrame.addWidget(self.label_Lime)          
        layout.specFrame.addWidget(self.label_spec3)
        layout.specFrame.addWidget(self.label_Violet)          
        layout.specFrame.addWidget(self.label_spec4) 
        layout.specFrame.addWidget(self.label_Red)         
        layout.specFrame.addStretch()

        layout.FlagFrame.addWidget(self.Sigma_Flag) 
        layout.FlagFrame.addStretch()
        
        layout.DelFrame.addWidget(self.Die_Select)
        layout.DelFrame.addWidget(self.Delete_Button)
        layout.DelFrame.addWidget(self.Reset_Button)
        layout.DelFrame.addStretch()  

    def spec(self):
        self.label_spec1 = QtWidgets.QLabel("δ(x): 0 ≤")
        self.label_Blue = QtWidgets.QLabel("■")
        self.label_spec2 = QtWidgets.QLabel("< 1% ≤")
        self.label_Lime = QtWidgets.QLabel("■")
        self.label_spec3 = QtWidgets.QLabel("< 5% ≤ ")
        self.label_Violet = QtWidgets.QLabel("■")        
        self.label_spec4 = QtWidgets.QLabel("< 50% ≤")
        self.label_Red = QtWidgets.QLabel("■")       
        self.label_spec1.setFont(QtGui.QFont("Arial",10))
        self.label_spec2.setFont(QtGui.QFont("Arial",10))
        self.label_spec3.setFont(QtGui.QFont("Arial",10))
        self.label_spec4.setFont(QtGui.QFont("Arial",10))        
        self.label_Blue.setFont(QtGui.QFont("Arial",12)) 
        self.label_Lime.setFont(QtGui.QFont("Arial",12))            
        self.label_Violet.setFont(QtGui.QFont("Arial",12))        
        self.label_Red.setFont(QtGui.QFont("Arial",12))      
        
        pe1 = QtGui.QPalette()
        pe2 = QtGui.QPalette()
        pe3 = QtGui.QPalette()
        pe4 = QtGui.QPalette()        
        
        pe1.setColor(QtGui.QPalette.WindowText,QtCore.Qt.blue)
        pe2.setColor(QtGui.QPalette.WindowText,QtCore.Qt.green)
        pe3.setColor(QtGui.QPalette.WindowText,QtCore.Qt.magenta)
        pe4.setColor(QtGui.QPalette.WindowText,QtCore.Qt.red)  
        
        self.label_Blue.setPalette(pe1)        
        self.label_Lime.setPalette(pe2)        
        self.label_Violet.setPalette(pe3)        
        self.label_Red.setPalette(pe4) 
    
    def menu(self):
        # load new file action
        openFile = QtWidgets.QAction('Open', self)
        openFile.setStatusTip('载入新的数据')
        openFile.triggered.connect(self.showDialog)
        # exit action
        exitAction = QtWidgets.QAction('Exit', self)
        exitAction.setStatusTip('退出')
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        # about action
        aboutAction = QtWidgets.QAction('About', self)
        aboutAction.setStatusTip('关于')
        aboutAction.triggered.connect(self.about)        
        # add menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(exitAction)
        aboutMenu = menubar.addMenu('Help')
        aboutMenu.addAction(aboutAction)
       
    def about(self):
        QtWidgets.QMessageBox.about(self,"About",Help.about)  
        
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,'Message',"确认要退出吗?", 
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 

    # drag the file to mainwindow ---start
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(Interface, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        super(Interface, self).dragMoveEvent(event)
        
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            # event.mimeData().urls() is a list contain all file that dragged in
            fname = event.mimeData().urls()[0].toLocalFile()
            self.judgeFile(fname)
            event.acceptProposedAction()
        else:
            super(Interface,self).dropEvent(event)  
    # drag the file to mainwindow ---end
        
    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self,'载入 Mapping Data','/.dat')[0]
        self.judgeFile(fname)
        
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
           
            self.fig1.clear()
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
        DataVisualize(self.fig1,PlotData,PlotDie)
        DieVisualize(self.fig2,PlotData,PlotDie,self.radius)
        self.canvas1.draw()
        self.canvas2.draw()     
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
                self.fig1.clear()
                self.showIt(self.pltDatTemp,self.pltDieTemp)
                self.loadDies(self.pltDieTemp)    
        except AttributeError:
            pass        
    
    def stateCheck(self):
        # signals and slots
        self.Search_Line.returnPressed.connect(self.loadList)
        self.Search_Button.clicked.connect(self.loadList)
        self.Id_Select.currentIndexChanged.connect(self.loadList)
        self.Item_List.currentRowChanged.connect(self.justDoIt)
        self.Sigma_Flag.clicked.connect(self.justDoIt)
        self.Delete_Button.clicked.connect(self.delDie)
        self.Reset_Button.clicked.connect(self.justDoIt)
               
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()