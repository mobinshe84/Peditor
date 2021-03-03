import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QDialog
import Variables
import CompressingVideo
import threading
class Ui_CompressVideo(QWidget):
    def setupUi(self, CompressVideo):
        CompressVideo.setObjectName("CompressVideo")
        CompressVideo.resize(411, 361)
        self.centralwidget = QtWidgets.QWidget(CompressVideo)
        self.centralwidget.setObjectName("centralwidget")
        #-------Labels-------#
        #"CompressVideo"label
        self.CompressVideoLabel = QtWidgets.QLabel(self.centralwidget)
        self.CompressVideoLabel.setGeometry(QtCore.QRect(40, 20, 331, 41))
        self.CompressVideoLabel.setFont(Variables.TLFont)
        self.CompressVideoLabel.setObjectName("CompressVideoLabel")
        self.CompressVideoLabel.setAlignment(QtCore.Qt.AlignCenter)
        #VideoStatus label
        self.VideoStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.VideoStatusLabel.setGeometry(QtCore.QRect(50, 130, 311, 31))
        self.VideoStatusLabel.setFont(Variables.LFont)
        self.VideoStatusLabel.setObjectName("VideoStatusLabel")
        
        #-------Buttons-------#
        #"Open Video" Button
        self.OpenVideoButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenVideoButton.setGeometry(QtCore.QRect(140, 70, 131, 41))
        self.OpenVideoButton.setFont(Variables.BFont)
        self.OpenVideoButton.setObjectName("OpenVideoButton")
        self.OpenVideoButton.clicked.connect(self.GetVideo)
        #"Compress" Button
        self.CompressButton = QtWidgets.QPushButton(self.centralwidget)
        self.CompressButton.setGeometry(QtCore.QRect(240, 260, 121, 41))
        self.CompressButton.setFont(Variables.BFont)
        self.CompressButton.setObjectName("CompressButton")
        self.CompressButton.clicked.connect(self.CompressClicked)
        #"Back" Button
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(50, 260, 121, 41))
        self.BackButton.setFont(Variables.BFont)
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(self.BackClicked)
        
        CompressVideo.setCentralWidget(self.centralwidget)
        self.retranslateUi(CompressVideo)
        QtCore.QMetaObject.connectSlotsByName(CompressVideo)

    def retranslateUi(self, CompressVideo):
        _translate = QtCore.QCoreApplication.translate
        CompressVideo.setWindowTitle(_translate("CompressVideo", "Peditor"))
        self.CompressVideoLabel.setText(_translate("CompressVideo", "Compress Video"))
        self.VideoStatusLabel.setText(_translate("CompressVideo", "You didn't select any file"))
        self.OpenVideoButton.setText(_translate("CompressVideo", "Open Video"))
        self.CompressButton.setText(_translate("CompressVideo", "Compress"))
        self.BackButton.setText(_translate("CompressVideo", "Back"))
        self.VideoStatusLabel.adjustSize()
    
    def GetVideo(self):
        dialog = QFileDialog()
        dialog.setWindowTitle('Open Coil Definition File')
        dialog.setNameFilters(["mp4 video (*.mp4)",
                               "wmv Video (*.wmv)",
                               "Matroska (*.mkv)",
                               "Quick Time (*.mov)",
                               "avi video (*.avi)"])
        dialog.setFileMode(QFileDialog.ExistingFile)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            global Address
            Address = str(dialog.selectedFiles()[0])
            self.UpdateVideoStatus()
            
        else:
            return None
    
    def UpdateVideoStatus(self):
        try:
            _ = Address
        except:
            return
        self.VideoStatusLabel.setText("Your video name is: '" + Address.split("/")[-1] + "'")
        self.VideoStatusLabel.adjustSize()
    
    def CompressClicked(self):
        try:
            _ = Address
        except:
            UnselectedFileMessage = QMessageBox()
            UnselectedFileMessage.setWindowTitle("Peditor")
            UnselectedFileMessage.setText("You didn't select any files!")
            UnselectedFileMessage.setIcon(QMessageBox.Warning)
            x = UnselectedFileMessage.exec_()
            return
        SaveVideoMessage = QMessageBox()
        SaveVideoMessage.setWindowTitle("Peditor")
        SaveVideoMessage.setText("You have to defining us the location of the output!")
        SaveVideoMessage.setIcon(QMessageBox.Warning)
        x = SaveVideoMessage.exec_()
        self.SaveVideo()
        self.SecondWindow = QtWidgets.QMainWindow()
        self.CompressingUi = CompressingVideo.Ui_CompressingVideo()
        self.CompressingUi.setupUi(self.SecondWindow)
        self.SecondWindow.show()
        CompressThread = threading.Thread(target = CompressingVideo.CompressingVideo.Compress, args = [CompressingVideo.CompressingVideo, Address, SaveAddress])
        CompressThread.start()
    
    def BackClicked(self):
        try:
            _ = Address
        except:
            QCoreApplication.exit()
            return
        DontSaveFileMessage = QMessageBox()
        DontSaveFileMessage.setWindowTitle("Peditor")
        DontSaveFileMessage.setText("Do you want to save changes to Untitled?")
        DontSaveFileMessage.setIcon(QMessageBox.Question)
        DontSaveFileMessage.setStandardButtons(QMessageBox.Save|QMessageBox.Close|QMessageBox.Cancel)
        DontSaveFileMessage.buttonClicked.connect(self.BackSaveClicked)
        x = DontSaveFileMessage.exec_()
    def BackClicked2(self, i):
        Answer = i.text()
        if Answer == "Save":
            self.SaveVideo()
            QCoreApplication.exit()
        elif Answer == "Close":
            QCoreApplication.exit()
    
    def SaveVideo(self):
        SaveVideoDialog = QFileDialog()
        SaveVideoDialog.setAcceptMode(QFileDialog.AcceptSave)
        SaveVideoDialog.setNameFilters(["mp4 video (*.mp4)",
                               "wmv Video (*.wmv)",
                               "Matroska (*.mkv)",
                               "Quick Time (*.mov)",
                               "avi video (*.avi)"])
        if SaveVideoDialog.exec_() == QDialog.Accepted:
            global SaveAddress
            SaveAddress = str(SaveVideoDialog.selectedFiles()[0])
            print(SaveAddress)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    CompressVideo = QMainWindow()
    ui = Ui_CompressVideo()
    ui.setupUi(CompressVideo)
    CompressVideo.show()
    sys.exit(app.exec_())