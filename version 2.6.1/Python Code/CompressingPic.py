'''
This class is designed to compress photos.
Converts a photo to a .pcif format and converts it to a photo with the help of the DecodeImg class
'''


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QFileDialog, QDialog, QMessageBox
import threading
import numpy as np
from PIL import Image
import CompressPic
import Variables

class EncodeImg():
    '''
    
    '''
    def ImageToArray(self, image):
        width, height, deep = image.shape
        array = image.reshape((width, height, deep))
        return array, width, height, deep

    def WriteInImage(self, array, w, h, d, SaveAddress):
        file = open('1.pcif', 'w')
        file.write("{} {} {}".format(w, h, d))
        per = -1000
        print("------- Compressing Data -------")
        l = []
        for i in range(h):
            if per != int(i/h*100):
                global x
                x = int(i/h*100)
                ReloadCompressing(x)
                print("| ({}%) has been processed ========== |".format(x))
                per = int(i/h*100)
            file.write('\n')
            k = 10
            pre = ''
            for color in range(d):
                file.write('{}-{} '.format(array[0, i, color], 0))
                pre = array[0, i, color]
                pos = 0
                for j in range(w):
                    if array[j, i, color] > pre + k or array[j, i, color] < pre - k:
                        pre = array[j, i, color]
                        pos = j
                        file.write('{}-{} '.format(pre, pos))
                if pos != w-1:
                    file.write('{}-{} '.format(array[w-1, i, color], w-1))
                file.write("* ")
        file.close()
        
        print('----- Done -----')
        decodeThread = threading.Thread(target=DecodeImg.St, args=[DecodeImg, SaveAddress])
        decodeThread.start()
    def LoadImage(self, image, SaveAddress):
        array, width, height, deep = self.ImageToArray(self, image)
        self.WriteInImage(self, array, width, height, deep, SaveAddress)


class Compressing(QWidget):
    def setupUi(self, Peditor):
        Peditor.setObjectName("Peditor")
        Peditor.resize(331, 211)
        self.centralwidget = QtWidgets.QWidget(Peditor)
        self.centralwidget.setObjectName("centralwidget")
        
        #-----ProgressBars-----#
        Compressing.ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ProgressBar.setGeometry(QtCore.QRect(30, 90, 281, 23))
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName("ProgressBar")
        
        #-----Labels-----#
        #NameLabel
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(30, 10, 271, 31))
        self.NameLabel.setFont(Variables.TLFont)
        self.NameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NameLabel.setObjectName("NameLabel")
        #CompressStatusLabel
        self.CompressStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.CompressStatusLabel.setGeometry(QtCore.QRect(30, 60, 111, 21))
        self.CompressStatusLabel.setFont(Variables.LFont)
        self.CompressStatusLabel.setObjectName("CompressStatusLabel")
        #-----Buttons-----#
        #OpenButton
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QtCore.QRect(30, 130, 101, 31))
        self.CancelButton.setFont(Variables.BFont)
        self.CancelButton.setObjectName("CancelButton")
        self.CancelButton.clicked.connect(self.CancelClicked)
        #DecodeButton
        self.DecodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.DecodeButton.setGeometry(QtCore.QRect(161, 130, 101, 31))
        self.DecodeButton.setFont(Variables.BFont)
        self.DecodeButton.setObjectName("DecodeButton")
        
        Peditor.setCentralWidget(self.centralwidget)
        self.retranslateUi(Peditor)
        QtCore.QMetaObject.connectSlotsByName(Peditor)
        
    def retranslateUi(self, Peditor):
        _translate = QtCore.QCoreApplication.translate
        Peditor.setWindowTitle(_translate("Peditor", "Peditor"))
        self.NameLabel.setText(_translate("Peditor", "Compress Pic"))
        self.CompressStatusLabel.setText(_translate("Peditor", "Compressing..."))
        self.CancelButton.setText(_translate("Peditor", "Cancel"))
        self.DecodeButton.setText(_translate("Peditor", "Decode"))
        
    def SavePic(self, img):
        SavePicDialog = QFileDialog()
        SavePicDialog.setAcceptMode(QFileDialog.AcceptSave)
        SavePicDialog.setNameFilters(["JPEG (*.jpg;*.jpeg;*.jpe;*.jfif)","PNG (*.png)"])
        if SavePicDialog.exec_() == QDialog.Accepted:
            global SaveAddress
            SaveAddress = str(SavePicDialog.selectedFiles()[0])
            img.save(SaveAddress)
            QCoreApplication.exit()
        
    def ReloadProgressBar(self, x):
        Compressing.ProgressBar.setProperty("value", x)
        
    def CancelClicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("Peditor")
        msg.setText("Do you sure to want to back?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msg.buttonClicked.connect(self.BackClicked2)
        x = msg.exec_()
    def BackClicked2(self, i):
        i = i.text()
        if i == "&Yes":
            self.close()
            
def ReloadCompressing(x = 0):
    CompressingUi = Compressing()
    CompressingUi.ReloadProgressBar(x)
    
class DecodeImg():
    def St(self, SaveAddress):
        array = self.decode_arrays(self)
        img = Image.fromarray(array.astype(np.uint8))
        b, g, r = img.split()
        img = Image.merge("RGB", (r, g, b))
        img.save(SaveAddress)
        QCoreApplication.exit()

    def decode_arrays(self):
        file = open('1.pcif', 'r')
        w, h, d = map(int, file.readline().split())
        new_array = np.array([[[0]*d,]*h,]*w,)
        for i in range(h):
            array = file.readline().split()
            flag = 0
            pre_position = 0
            pre = ''
            for j in array:
                if len(j)==1:
                    flag += 1
                    pre_position = 0
                    pre = ''
                else:
                    item, pos = j.split("-")
                    pos = int(pos)
                    item = int(item)
                    new_array[pos][i][flag] = item
                    for m in range(pre_position, pos):
                        new_array[m][i][flag] = pre
                    pre = item
                    pre_position = pos
        return new_array

