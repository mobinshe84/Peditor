import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMessageBox
import CompressPic
import CompressVideo
import Variables
import Setting
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        """This Function sets the Ui Things"""
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        Variables.LoadFont(self)
        
        #-------GroupBoxes-------#
        self.groupBox_Help = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Help.setGeometry(QtCore.QRect(260, 100, 511, 431))
        self.groupBox_Help.setTitle("")
        self.groupBox_Help.setObjectName("groupBox_Help")
        
        #-------Labels-------#
        #Peditor label
        self.PeditorLabel = QtWidgets.QLabel(self.centralwidget)
        self.PeditorLabel.setGeometry(QtCore.QRect(40, 30, 151, 31))
        self.PeditorLabel.setFont(Variables.TLFont)
        self.PeditorLabel.setObjectName("PeditorLabel")
        #Help label
        self.HelpLabel = QtWidgets.QLabel(self.groupBox_Help)
        self.HelpLabel.setGeometry(QtCore.QRect(10, 10, 481, 111))
        self.HelpLabel.setFont(Variables.LFont)
        self.HelpLabel.setScaledContents(True)
        self.HelpLabel.setObjectName("HelpLabel")
        
        
        #-------Buttons-------#
        #CompressPic button
        self.CompressPicButton = QtWidgets.QPushButton(self.centralwidget)
        self.CompressPicButton.setGeometry(QtCore.QRect(40, 100, 201, 41))
        self.CompressPicButton.setFont(Variables.BFont)
        self.CompressPicButton.setObjectName("CompressPicButton")
        self.CompressPicButton.clicked.connect(self.CompressPicClicked)
        #CompressVideo button
        self.CompressVideoButton = QtWidgets.QPushButton(self.centralwidget)
        self.CompressVideoButton.setGeometry(QtCore.QRect(40, 160, 201, 41))
        self.CompressVideoButton.setFont(Variables.BFont)
        self.CompressVideoButton.setObjectName("CompressVideoButton")
        self.CompressVideoButton.clicked.connect(self.CompressVideoClicked)
        #DisappearObjectPic button
        self.DisappearPicButton = QtWidgets.QPushButton(self.centralwidget)
        self.DisappearPicButton.setGeometry(QtCore.QRect(40, 220, 201, 41))
        self.DisappearPicButton.setFont(Variables.BFont)
        self.DisappearPicButton.setObjectName("DisappearPicButton")
        self.DisappearPicButton.clicked.connect(self.DisappearPicClicked)
        #DisappearObjectVideo button
        self.DisappearVideoButton = QtWidgets.QPushButton(self.centralwidget)
        self.DisappearVideoButton.setGeometry(QtCore.QRect(40, 280, 201, 41))
        self.DisappearVideoButton.setFont(Variables.BFont)
        self.DisappearVideoButton.setObjectName("DisappearVideoButton")
        self.DisappearVideoButton.clicked.connect(self.DisappearVideoClicked)
        #Exit button
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(40, 490, 101, 41))
        self.ExitButton.setFont(Variables.BFont)
        self.ExitButton.setObjectName("ExitButton")
        self.ExitButton.clicked.connect(self.ExitClicked)
        #Setting button
        self.SettingButton = QtWidgets.QPushButton(self.centralwidget)
        self.SettingButton.setGeometry(QtCore.QRect(40, 340, 201, 41))
        self.SettingButton.setFont(Variables.BFont)
        self.SettingButton.setObjectName("SettingButton")
        self.SettingButton.clicked.connect(self.SettingClicked)
        MainWindow.setCentralWidget(self.centralwidget)
        
        #-------Menubar-------#
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCompress = QtWidgets.QMenu(self.menubar)
        self.menuCompress.setObjectName("menuCompress")
        self.menuDisappear = QtWidgets.QMenu(self.menubar)
        self.menuDisappear.setObjectName("menuDisappear")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.ExitMenu = QtWidgets.QAction(MainWindow)
        self.ExitMenu.setObjectName("ExitMenu")
        self.ExitMenu.triggered.connect(self.ExitClicked)
        
        self.CompressPicMenu = QtWidgets.QAction(MainWindow)
        self.CompressPicMenu.setObjectName("CompressPicMenu")
        self.CompressPicMenu.triggered.connect(self.CompressPicClicked)
        
        self.CompressVideoMenu = QtWidgets.QAction(MainWindow)
        self.CompressVideoMenu.setObjectName("CompressVideoMenu")
        self.CompressVideoMenu.triggered.connect(self.CompressVideoClicked)
        
        self.DisappearPicMenu = QtWidgets.QAction(MainWindow)
        self.DisappearPicMenu.setObjectName("DisappearPicMenu")
        
        self.DisappearVideoMenu = QtWidgets.QAction(MainWindow)
        self.DisappearVideoMenu.setObjectName("DisappearVideoMenu")
        
        self.FontMenu = QtWidgets.QAction(MainWindow)
        self.FontMenu.setObjectName("FontMenu")
        self.FontMenu.triggered.connect(self.SettingClicked)
        
        self.ReloadFontMenu = QtWidgets.QAction(MainWindow)
        self.ReloadFontMenu.setObjectName("ReloadFontMenu")
        self.ReloadFontMenu.triggered.connect(self.ReloadFont)
        
        self.menuFile.addAction(self.ExitMenu)
        self.menuCompress.addAction(self.CompressPicMenu)
        self.menuCompress.addAction(self.CompressVideoMenu)
        self.menuDisappear.addAction(self.DisappearPicMenu)
        self.menuDisappear.addAction(self.DisappearVideoMenu)
        self.menuSetting.addAction(self.FontMenu)
        self.menuSetting.addAction(self.ReloadFontMenu)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCompress.menuAction())
        self.menubar.addAction(self.menuDisappear.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Peditor"))
        self.PeditorLabel.setText(_translate("MainWindow", "PeDiToR"))
        self.PeditorLabel.adjustSize()
        self.HelpLabel.setText(_translate("MainWindow", Variables.HelpText))
        self.HelpLabel.adjustSize()
        self.CompressPicButton.setText(_translate("MainWindow", "Compress Pic"))
        self.CompressVideoButton.setText(_translate("MainWindow", "Compress Video"))
        self.DisappearPicButton.setText(_translate("MainWindow", "disappear a Object in Pic"))
        self.DisappearVideoButton.setText(_translate("MainWindow", "disappear a Object in Video"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))
        self.SettingButton.setText(_translate("MainWindow", "Setting"))
        
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCompress.setTitle(_translate("MainWindow", "Compress"))
        self.menuDisappear.setTitle(_translate("MainWindow", "Disappear"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        
        self.ExitMenu.setText(_translate("MainWindow", "Exit"))
        self.CompressPicMenu.setText(_translate("MainWindow", "Pic"))
        self.CompressVideoMenu.setText(_translate("MainWindow", "Video"))
        self.DisappearPicMenu.setText(_translate("MainWindow", "Pic"))
        self.DisappearVideoMenu.setText(_translate("MainWindow", "Video"))
        self.FontMenu.setText(_translate("MainWindow", "Font"))
        self.ReloadFontMenu.setText(_translate("MainWindow", "Reload font"))
        
        self.ExitMenu.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.CompressPicMenu.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.CompressVideoMenu.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.DisappearPicMenu.setShortcut(_translate("MainWindow", "Alt+P"))
        self.DisappearVideoMenu.setShortcut(_translate("MainWindow", "Alt+V"))
        self.FontMenu.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.ReloadFontMenu.setShortcut(_translate("MainWindow", "Ctrl+R+F"))
    
    def ExitClicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("Peditor")
        msg.setText("do you sure to want to exit?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.ExitPopupClicked)
        x = msg.exec_()
    def ExitPopupClicked(self, i):
        if i.text() == "&Yes":
            sys.exit()
    
    def CompressPicClicked(self):
        self.SecondWindow = QtWidgets.QMainWindow()
        self.CompressPicUi = CompressPic.Ui_CompressPic()
        self.CompressPicUi.setupUi(self.SecondWindow)
        self.SecondWindow.show()
    
    def CompressVideoClicked(self):
        self.SecondWindow = QtWidgets.QMainWindow()
        self.CompressVideoUi = CompressVideo.Ui_CompressVideo()
        self.CompressVideoUi.setupUi(self.SecondWindow)
        self.SecondWindow.show()
    
    def DisappearPicClicked(self):
        print("DisappearPicClicked")
    
    def DisappearVideoClicked(self):
        print("DisappearVideoClicked")
    
    def SettingClicked(self):
        self.SecondWindow = QtWidgets.QMainWindow()
        self.CompressVideoUi = Setting.Ui_Setting()
        self.CompressVideoUi.setupUi(self.SecondWindow)
        self.SecondWindow.show()
        self.ReloadFont()
        
    def ReloadFont(self):
        self.PeditorLabel.setFont(Variables.TLFont)
        self.HelpLabel.setFont(Variables.LFont)
        self.CompressPicButton.setFont(Variables.BFont)
        self.CompressVideoButton.setFont(Variables.BFont)
        self.DisappearPicButton.setFont(Variables.BFont)
        self.DisappearVideoButton.setFont(Variables.BFont)
        self.SettingButton.setFont(Variables.BFont)
        self.ExitButton.setFont(Variables.BFont)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mainui = Ui_MainWindow()
    mainui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())