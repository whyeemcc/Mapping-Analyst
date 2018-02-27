import sys,os
from PyQt5 import QtGui,QtCore,QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from Layout import Layout
from Help import Help
import images_qr

class Interface(QtWidgets.QMainWindow):

    def __init__(self,parent=None):
        super(Interface, self).__init__(parent)
        self.setupUi() 
    
    def setupUi(self):
        self.widget()
        self.label()
        self.draw()
        self.spec()
        self.menu()
        self.layout()
        self.statusBar()
        self.setAcceptDrops(True)
        # x,y,width,length
        self.setGeometry(100, 100, 1300, 650)
        self.setWindowTitle('Mapping Analyst')
        self.setWindowIcon(QtGui.QIcon(':/images/logo.gif')) 
        self.show()

    def widget(self):       
        self.Item_List      = QtWidgets.QListWidget(self)
        self.Id_Select      = QtWidgets.QComboBox(self) 
        self.Search_Line    = QtWidgets.QLineEdit(self)
        self.Search_Button  = QtWidgets.QPushButton("筛选")  
        self.Sigma_Flag     = QtWidgets.QRadioButton("循环筛除距离 Median 值 3σ 以外的 die")
        self.Die_Select     = QtWidgets.QComboBox(self)
        self.Delete_Button  = QtWidgets.QPushButton("剔除该die")
        self.Reset_Button   = QtWidgets.QPushButton("重置")
        # set Font style
        self.setStyleSheet("QWidget{font-family:Microsoft YaHei}")
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
        self.label_fileNow      = QtWidgets.QLabel("当前文件:\t")
        self.label_waferID      = QtWidgets.QLabel("WaferID:")
        self.label_Etest        = QtWidgets.QLabel("Etest:")
        self.label_Testkey      = QtWidgets.QLabel("Testkey:")
        self.label_Device       = QtWidgets.QLabel("Device:")
        self.label_W            = QtWidgets.QLabel("W:")
        self.label_L            = QtWidgets.QLabel("L:")
        self.label_Unit         = QtWidgets.QLabel("Unit:")
        self.label_DieCount     = QtWidgets.QLabel("DieCount:")        
        self.label_Median       = QtWidgets.QLabel("Median:")
        self.label_Average      = QtWidgets.QLabel("Average:")
        self.label_Max          = QtWidgets.QLabel("Max:")
        self.label_Min          = QtWidgets.QLabel("Min:")
        self.label_Standard     = QtWidgets.QLabel("Standard(σ):")
        self.label_3sigma       = QtWidgets.QLabel("3sigma(3σ):")
        self.label_sigmMed      = QtWidgets.QLabel("σ/median:")
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
        
    def layout(self):
        layout = Layout()
        self.setCentralWidget(layout.wid)
        
        layout.fileFrame.addWidget(self.label_fileNow)
        layout.fileFrame.addWidget(self.label_fileNow_C)
        layout.fileFrame.addStretch()
        
        layout.idFrame.addWidget(self.label_waferID)
        layout.idFrame.addWidget(self.Id_Select)   
        layout.searchFrame.addWidget(self.Search_Line)
        layout.searchFrame.addWidget(self.Search_Button)
        
        layout.listFrame.addWidget(self.Item_List)
        layout.barFrame.addWidget(self.toolbar)
        layout.canvasFrame1.addWidget(self.canvas1)
        layout.canvasFrame2.addWidget(self.canvas2)
        
        for w in [
                  QtWidgets.QLabel(""),
                  QtWidgets.QLabel(""),
                  QtWidgets.QLabel(""),
                  self.label_Etest,
                  self.label_Testkey,
                  self.label_Device,
                  self.label_W,
                  self.label_L,
                  self.label_Unit,
                  self.label_DieCount,
                  self.label_Median,
                  self.label_Average,
                  self.label_Max,
                  self.label_Min,
                  self.label_Standard,
                  self.label_3sigma,
                  self.label_sigmMed
                 ]:
            layout.m1Frame.addWidget(w)
            layout.m1Frame.addStretch()
            layout.m1Frame.setSpacing(10)         
        
        for w in [
                  QtWidgets.QLabel(""),
                  QtWidgets.QLabel(""),
                  QtWidgets.QLabel(""),
                  self.label_Etest_C,
                  self.label_Testkey_C,
                  self.label_Device_C,
                  self.label_W_C,
                  self.label_L_C,
                  self.label_Unit_C,
                  self.label_DieCount_C,
                  self.label_Median_C,
                  self.label_Average_C,
                  self.label_Max_C,
                  self.label_Min_C,
                  self.label_Standard_C,
                  self.label_3sigma_C,
                  self.label_sigmMed_C
                 ]:
            layout.m2Frame.addWidget(w)
            layout.m2Frame.addStretch()
            layout.m2Frame.setSpacing(10)
        
        for w in [
                  self.label_spec1,
                  self.label_Blue,
                  self.label_spec2,
                  self.label_Lime,
                  self.label_spec3,
                  self.label_Violet,
                  self.label_spec4,
                  self.label_Red
                 ]:
            layout.specFrame.addWidget(w)
            layout.specFrame.addStretch()

        layout.FlagFrame.addWidget(self.Sigma_Flag) 
        layout.FlagFrame.addStretch()
        
        layout.DelFrame.addWidget(self.Die_Select)
        layout.DelFrame.addWidget(self.Delete_Button)
        layout.DelFrame.addWidget(self.Reset_Button)
        layout.DelFrame.addStretch()  

    def spec(self):
        self.label_spec1    = QtWidgets.QLabel("δ(x): 0 ≤")
        self.label_Blue     = QtWidgets.QLabel("■")
        self.label_spec2    = QtWidgets.QLabel("< 1% ≤")
        self.label_Lime     = QtWidgets.QLabel("■")
        self.label_spec3    = QtWidgets.QLabel("< 5% ≤ ")
        self.label_Violet   = QtWidgets.QLabel("■")        
        self.label_spec4    = QtWidgets.QLabel("< 50% ≤")
        self.label_Red      = QtWidgets.QLabel("■")       
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
        # re-write in subclass 
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())