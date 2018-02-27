from PyQt5 import QtWidgets

class Layout:
    def __init__(self): 
        self.wid = QtWidgets.QWidget()
        # self.setCentralWidget(wid)
        self.mainFrame = QtWidgets.QVBoxLayout()
        self.wid.setLayout(self.mainFrame)
        '''
                 ---------------
                |               |
                |               |
                |               | 
          wid   |   mainFrame   |
                |               |
                |               |
                |               |
                 ---------------    
        '''
        
        # define layout
        self.fileFrame = QtWidgets.QHBoxLayout()
        self.remainFrame = QtWidgets.QHBoxLayout()
        # load layout
        self.mainFrame.addLayout(self.fileFrame)
        self.mainFrame.addLayout(self.remainFrame)
        self.mainFrame.addStretch()        
        '''
                 ------------------
                |  --------------  |
                | |   fileFrame  | |
                |  --------------  |
                |  --------------  |
      mainFrame | |              | |         ^
                | |  remainFrame | |         |
                | |              | |
                | |              | |
                |  --------------  |
                 ------------------       
        '''     
        
        # define layout        
        self.leftFrame = QtWidgets.QVBoxLayout() 
        self.middleFrame = QtWidgets.QHBoxLayout()
        self.rightFrame = QtWidgets.QVBoxLayout() 
        # load layout        
        self.remainFrame.addLayout(self.leftFrame)
        self.remainFrame.addLayout(self.middleFrame)             
        self.remainFrame.addLayout(self.rightFrame)
        self.remainFrame.setStretchFactor(self.leftFrame,1)
        self.remainFrame.setStretchFactor(self.middleFrame,1)
        self.remainFrame.setStretchFactor(self.rightFrame,4)
        '''
                 -------------------------------
                |  -------   -------   -------  |
                | |       | |       | |       | |
                | | left  | | middle| | right | |
    remainFrame | | Frame | | Frame | | Frame | |          <-
                | |       | |       | |       | |
                | |       | |       | |       | |
                | |       | |       | |       | |
                |  -------   -------   -------  |
                 ------------------------------- 
        '''             

        # define layouts in leftFrame
        self.idFrame = QtWidgets.QHBoxLayout()
        self.searchFrame = QtWidgets.QHBoxLayout()   
        self.listFrame = QtWidgets.QVBoxLayout() 
        # load layouts in leftFrame
        self.leftFrame.addLayout(self.idFrame)   
        self.leftFrame.addLayout(self.searchFrame)   
        self.leftFrame.addLayout(self.listFrame)
        '''
                 ------------------
                |  --------------  | 
                | |   idFrame    | |
                |  --------------  |   
                |  --------------  |    
                | | searchFrame  | | 
                |  --------------  | 
                |  --------------  |              ^
      leftFrame | |              | |              |
                | |              | |              
                | |              | |              
                | |  listFrame   | |
                | |              | |
                | |              | |
                | |              | |
                | |              | |
                |  --------------  |       
                 ------------------  
        '''
        
        # define layouts in middleFrame
        self.m1Frame = QtWidgets.QVBoxLayout()
        self.m2Frame = QtWidgets.QVBoxLayout()
        # load layouts in leftFrame
        self.middleFrame.addLayout(self.m1Frame)   
        self.middleFrame.addLayout(self.m2Frame)        
        '''
                 ---------------------
                |  -------   -------  |
                | |       | |       | |
                | |  m1   | |  m2   | |
    middleFrame | | Frame | | Frame | |          <-
                | |       | |       | |
                | |       | |       | |
                | |       | |       | |
                |  -------   -------  |
                 ---------------------
        '''   
     
        
        # define layouts in rightFrame 
        self.DieFrame = QtWidgets.QHBoxLayout()
        self.barFrame = QtWidgets.QVBoxLayout()
        self.canvasFrame1 = QtWidgets.QVBoxLayout()
        # layout load widgets              
        self.rightFrame.addLayout(self.barFrame)
        self.rightFrame.addLayout(self.canvasFrame1)
        self.rightFrame.addLayout(self.DieFrame)
        self.rightFrame.addStretch()
        self.rightFrame.setStretchFactor(self.barFrame,1)
        self.rightFrame.setStretchFactor(self.canvasFrame1,3)
        self.rightFrame.setStretchFactor(self.DieFrame,3)
        '''
                 ----------------------- 
                |  -------------------  |
                | |     barFrame      | |
                |  -------------------  | 
                |  -------------------  |
                | |                   | | 
                | |    canvasFrame1   | |        
                | |                   | |
                | |                   | |              ^
                |  -------------------  |              |
     rightFrame |  -------------------  |
                | |                   | |
                | |                   | |
                | |     DieFrame      | |
                | |                   | |
                | |                   | |
                | |                   | |
                | |                   | |
                |  -------------------  |   
                 -----------------------  
        '''
          
        
        self.RDFrame = QtWidgets.QVBoxLayout()
        self.canvasFrame2 = QtWidgets.QVBoxLayout()
        self.DieFrame.addLayout(self.canvasFrame2)
        self.DieFrame.addLayout(self.RDFrame)
        self.DieFrame.addStretch()  
        '''
                 ------------------------------
                |  --------------   ---------  |
                | |              | |         | | 
                | |              | |         | | 
       DieFrame | | canvasFrame2 | | RDFrame | |         <-
                | |              | |         | | 
                | |              | |         | | 
                |  --------------   ---------  |
                 ------------------------------ 
        '''     
        
        # define layouts in RDFrame 
        self.specFrame = QtWidgets.QHBoxLayout()   
        self.FlagFrame = QtWidgets.QHBoxLayout()        
        self.DelFrame = QtWidgets.QHBoxLayout()
        # load layouts in RDFrame    
        self.RDFrame.addStretch()
        self.RDFrame.addLayout(self.specFrame)
        self.RDFrame.addStretch()
        self.RDFrame.addLayout(self.FlagFrame)
        self.RDFrame.addStretch()
        self.RDFrame.addLayout(self.DelFrame)
        self.RDFrame.addStretch()    
        '''
                 ------------------
                |  --------------  | 
                | |   specFrame  | |
        RDFrame |  --------------  | 
                |  --------------  |             ^
                | |   FlagFrame  | |             |  
                |  --------------  |
                |  --------------  |              
                | |   DelFrame   | | 
                |  --------------  | 
                 ------------------
        ''' 