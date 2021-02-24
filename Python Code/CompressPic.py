import sys
import os
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget, QApplication
from PyQt5.QtWidgets import QFileDialog, QDialog
import Variables
import threading
import CompressingPic
import cv2

class Ui_CompressPic(QWidget):
    def setupUi(self, CompressPic):
        CompressPic.setObjectName("CompressPic")
        CompressPic.resize(411, 501)
        self.centralwidget = QWidget(CompressPic)
        self.centralwidget.setObjectName("centralwidget")
        
        #-------GroupBoxes-------#
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 120, 351, 291))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        #-------Labels-------#
        #CompressPic label
        self.CompressPicLabel = QtWidgets.QLabel(self.centralwidget)
        self.CompressPicLabel.setGeometry(QtCore.QRect(70, 20, 271, 31))
        self.CompressPicLabel.setFont(Variables.TLFont)
        self.CompressPicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CompressPicLabel.setObjectName("CompressPicLabel")
        #ShowPic label
        self.ShowPicLabel = QtWidgets.QLabel(self.groupBox)
        self.ShowPicLabel.setGeometry(QtCore.QRect(0, 0, 351, 291))
        self.ShowPicLabel.setFont(Variables.LFont)
        self.ShowPicLabel.setObjectName("ShowPicLabel")
        self.ShowPicLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        #-------Buttons-------#
        #"Open Picture" Button
        self.OpenPicButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenPicButton.setGeometry(QtCore.QRect(140, 70, 121, 41))
        self.OpenPicButton.setFont(Variables.BFont)
        self.OpenPicButton.setObjectName("OpenPicButton")
        self.OpenPicButton.clicked.connect(self.GetPic)
        #"Compress" Button
        self.CompressButton = QtWidgets.QPushButton(self.centralwidget)
        self.CompressButton.setGeometry(QtCore.QRect(230, 420, 121, 41))
        self.CompressButton.setFont(Variables.BFont)
        self.CompressButton.setObjectName("CompressButton")
        self.CompressButton.clicked.connect(self.CompressClicked)
        #"Back" button
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(60, 420, 121, 41))
        self.BackButton.setFont(Variables.BFont)
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(self.BackClicked)
        
        CompressPic.setCentralWidget(self.centralwidget)
        self.retranslateUi(CompressPic)
        QtCore.QMetaObject.connectSlotsByName(CompressPic)

    def retranslateUi(self, CompressPic):
        _translate = QCoreApplication.translate
        CompressPic.setWindowTitle(_translate("CompressPic", "Peditor"))
        self.BackButton.setText(_translate("CompressPic", "Back"))
        self.CompressPicLabel.setText(_translate("CompressPic", "Compress Picture"))
        self.CompressButton.setText(_translate("CompressPic", "Compress"))
        self.ShowPicLabel.setText(_translate("CompressPic", "Your Picture"))
        self.OpenPicButton.setText(_translate("CompressPic", "Open Picture"))
    
    def GetPic(self):
        dialog = QFileDialog()
        dialog.setNameFilters(["JPEG (*.jpg;*.jpeg;*.jpe;*.jfif)","PNG (*.png)"])
        dialog.setFileMode(QFileDialog.ExistingFile)
        if dialog.exec_() == QDialog.Accepted:
            global OpenAddress
            OpenAddress = str(dialog.selectedFiles()[0])
            self.ShowPic()
        else:
            return None


    def ShowPic(self):
        try:
            _ = OpenAddress
        except:
            return
        #size ShowPicLabel: (351,291)
        global FinallyImage
        Img = Image.open(OpenAddress)
        FinallyImage = Img
        (ximage,yimage) = Img.size
        minxy = min(351 / ximage, 291 / yimage)
        Resized_Img = Img.resize((int(ximage * minxy), int(yimage * minxy)))
        SaveAddress = "ImgShow" + OpenAddress[len(OpenAddress) - 4:]
        Resized_Img.save(SaveAddress)
        self.ShowPicLabel.setPixmap(QtGui.QPixmap(SaveAddress))
        self.ShowPicLabel.adjustSize()
        self.ShowPicLabel.setAlignment(QtCore.Qt.AlignCenter)
        os.remove(SaveAddress)
        
        
    def CompressClicked(self):
        try:
            _ = OpenAddress
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Peditor")
            msg.setText("You didn't select any files!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            return
        Im = cv2.imread(OpenAddress)
        self.SecondWindow = QtWidgets.QMainWindow()
        self.CompressingUi = CompressingPic.Compressing()
        self.CompressingUi.setupUi(self.SecondWindow)
        self.SecondWindow.show()
        CompressThread = threading.Thread(target = CompressingPic.EncodeImg.LoadImage, args = [CompressingPic.EncodeImg, Im])
        CompressThread.start()
        
        
            
    def BackClicked(self):
        try:
            _ = OpenAddress
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Peditor")
            msg.setText("Do you sure to want to back?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
            msg.buttonClicked.connect(self.BackClicked2)
            x = msg.exec_()
            return
            
        msg = QMessageBox()
        msg.setWindowTitle("Peditor")
        msg.setText("Do you sure to want to back?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msg.buttonClicked.connect(self.BackClicked2)
        x = msg.exec_()
        
    def BackClicked2(self, i):
        if i.text() == "&Yes":
            QApplication.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    CompressPic = QMainWindow()
    ui = Ui_CompressPic()
    ui.setupUi(CompressPic)
    CompressPic.show()
    sys.exit(app.exec_())
    
