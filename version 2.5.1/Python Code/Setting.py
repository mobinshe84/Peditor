from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGroupBox, QFontComboBox, QSpinBox, QPushButton
import sys
import Variables
import Main

class Ui_Setting(QWidget):
    def setupUi(self, SettingWindow):
        SettingWindow.setObjectName("MainWindow")
        SettingWindow.resize(330, 381)
        self.centralwidget = QWidget(SettingWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Variables
        global TLFamily, TLUnderline, TLSize, BFamily, BSize, LFamily, LSize
        TLFamily, TLUnderline, TLSize = Variables.TLFamily, Variables.TLUnderLine, Variables.TLSize
        BFamily, BSize = Variables.BFamily, Variables.BSize
        LFamily, LSize = Variables.LFamily, Variables.LSize
        
        #-----Labels-----#
        #NameLabel
        self.NameLabel = QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QRect(20, 10, 291, 31))
        self.NameLabel.setFont(Variables.TLFont)
        self.NameLabel.setObjectName("NameLabel")
        self.NameLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        
        #-----GroupBoxes-----#
        #MainGroupBox (FontGroupBox)
        self.FontsGroupBox = QGroupBox(self.centralwidget)
        self.FontsGroupBox.setGeometry(QRect(20, 50, 291, 251))
        self.FontsGroupBox.setFont(Variables.LFont)
        self.FontsGroupBox.setObjectName("FontsGroupBox")
        #ButtonFontGroupBox
        self.ButtonGroupBox = QGroupBox(self.FontsGroupBox)
        self.ButtonGroupBox.setGeometry(QRect(10, 40, 261, 61))
        self.ButtonGroupBox.setObjectName("ButtonFontGroupBox")
        #TopLabelGroupBox
        self.TopLabelGroupBox = QGroupBox(self.FontsGroupBox)
        self.TopLabelGroupBox.setGeometry(QRect(10, 110, 261, 61))
        self.TopLabelGroupBox.setObjectName("TopLabelGroupBox")
        #LabelGroupBox
        self.LabelGroupBox = QGroupBox(self.FontsGroupBox)
        self.LabelGroupBox.setGeometry(QRect(10, 180, 261, 61))
        self.LabelGroupBox.setObjectName("OtherLabelGroupBox")
        
        #-----ComboBoxes-----#
        #ButtonFontComboBox
        self.ButtonFontComboBox = QFontComboBox(self.ButtonGroupBox)
        self.ButtonFontComboBox.setGeometry(QRect(30, 30, 147, 22))
        self.ButtonFontComboBox.addItem("Ice kingdom Bold")
        self.ButtonFontComboBox.setObjectName("ButtonFontComboBox")
        self.ButtonFontComboBox.setCurrentFont(Variables.BFont)
        self.ButtonFontComboBox.currentFontChanged.connect(self.ButtonFCBChanged)
        #TopLabelFontComboBox
        self.TopLabelFontComboBox = QFontComboBox(self.TopLabelGroupBox)
        self.TopLabelFontComboBox.setGeometry(QRect(30, 30, 147, 22))
        self.TopLabelFontComboBox.setObjectName("TopLabelFontComboBox")
        self.TopLabelFontComboBox.setCurrentFont(Variables.TLFont)
        self.TopLabelFontComboBox.currentFontChanged.connect(self.TopLabelFCBChanged)
        #LabelFontComboBox
        self.LabelFontComboBox = QFontComboBox(self.LabelGroupBox)
        self.LabelFontComboBox.setGeometry(QRect(30, 30, 147, 22))
        self.LabelFontComboBox.setObjectName("OtherLabelFontComboBox")
        self.LabelFontComboBox.setCurrentFont(Variables.LFont)
        self.LabelFontComboBox.currentFontChanged.connect(self.LabelFCBChanged)
        
        #-----SpinBoxes-----#
        #ButtonSpinBox
        self.ButtonSpinBox = QSpinBox(self.ButtonGroupBox)
        self.ButtonSpinBox.setGeometry(QRect(200, 30, 41, 22))
        self.ButtonSpinBox.setObjectName("ButtonSpinBox")
        self.ButtonSpinBox.setValue(Variables.BSize)
        self.ButtonSpinBox.valueChanged.connect(self.ButtonSBChanged)
        #TopLabelSpinBox
        self.TopLabelSpinBox = QSpinBox(self.TopLabelGroupBox)
        self.TopLabelSpinBox.setGeometry(QRect(200, 30, 41, 22))
        self.TopLabelSpinBox.setObjectName("TopLabelSpinBox")
        self.TopLabelSpinBox.setValue(Variables.TLSize)
        self.TopLabelSpinBox.valueChanged.connect(self.TopLabelSBChanged)
        #LabelSpinBox
        self.LabelSpinBox = QSpinBox(self.LabelGroupBox)
        self.LabelSpinBox.setGeometry(QRect(200, 30, 41, 22))
        self.LabelSpinBox.setObjectName("OtherLabelSpinBox")
        self.LabelSpinBox.setValue(Variables.LSize)
        self.LabelSpinBox.valueChanged.connect(self.LabelSBChanged)
        
        #-----Buttons-----#
        #OkButton
        self.OkButton = QPushButton(self.centralwidget)
        self.OkButton.setGeometry(QRect(20, 310, 91, 31))
        self.OkButton.setFont(Variables.BFont)
        self.OkButton.setObjectName("OkButton")
        self.OkButton.clicked.connect(self.OkClicked)
        #CancelButton
        self.CancelButton = QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QRect(120, 310, 91, 31))
        self.CancelButton.setFont(Variables.BFont)
        self.CancelButton.setObjectName("CancelButton")
        #ApplyButton
        self.ApplyButton = QPushButton(self.centralwidget)
        self.ApplyButton.setGeometry(QRect(220, 310, 91, 31))
        self.ApplyButton.setFont(Variables.BFont)
        self.ApplyButton.setObjectName("ApplyButton")
        self.ApplyButton.clicked.connect(self.ApplyClicked)
        
        SettingWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(SettingWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingWindow)

    def retranslateUi(self, SettingWindow):
        _translate = QCoreApplication.translate
        SettingWindow.setWindowTitle(_translate("SettingWindow", "Peditor"))
        self.NameLabel.setText(_translate("SettingWindow", "Setting"))
        self.FontsGroupBox.setTitle(_translate("SettingWindow", "Fonts"))
        self.ButtonGroupBox.setTitle(_translate("SettingWindow", "Button Font"))
        self.TopLabelGroupBox.setTitle(_translate("SettingWindow", "Top Label Font"))
        self.LabelGroupBox.setTitle(_translate("SettingWindow", "Other Label Font"))
        self.OkButton.setText(_translate("SettingWindow", "Ok"))
        self.CancelButton.setText(_translate("SettingWindow", "Cancel"))
        self.ApplyButton.setText(_translate("SettingWindow", "Apply"))
        
    # FCB: FontComboBox
    def ButtonFCBChanged(self, i):
        global BFamily
        BFamily = i.family()
        
    def TopLabelFCBChanged(self, i):
        global TLFamily
        TLFamily = i.family()
        
    def LabelFCBChanged(self, i):
        global LFamily
        LFamily = i.family()
        
    def ButtonSBChanged(self, i):
        global BSize
        BSize = i
        
    def TopLabelSBChanged(self, i):
        global TLSize
        TLSize = i
        
    def LabelSBChanged(self, i):
        global LSize
        LSize = i
        
    def ApplyClicked(self):
        FontData = []
        FontDataFile = open(r'Data.txt', 'r')
        for line in FontDataFile.readlines():
            if line[len(line) - 1:] != "\n":
                FontData.append(line[:len(line)])
                break
            FontData.append(line[:len(line) - 1])
        FontDataFile.close()
        
        FontDataFile = open(r'Data.txt', 'w')
        FontData[0], FontData[1], FontData[2] = TLFamily, TLSize, TLUnderline
        FontData[3], FontData[4], FontData[5], FontData[6] = BFamily, BSize, LFamily, LSize
        FontDataFile.write(FontData[0]
                           + "\n" + str(FontData[1])
                           + "\n" + str(FontData[2])
                           + "\n" + FontData[3]
                           + "\n" + str(FontData[4])
                           + "\n" + FontData[5]
                           + "\n" + str(FontData[6]))
        FontDataFile.close()
        Variables.LoadFont(self)
        self.NameLabel.setFont(Variables.LFont)
        self.ReloadFont()

    def ReloadFont(self):
        self.NameLabel.setFont(Variables.TLFont)
        self.FontsGroupBox.setFont(Variables.LFont)
        self.ButtonGroupBox.setFont(Variables.LFont)
        self.TopLabelGroupBox.setFont(Variables.LFont)
        self.LabelGroupBox.setFont(Variables.LFont)
        self.OkButton.setFont(Variables.BFont)
        self.CancelButton.setFont(Variables.BFont)
        self.ApplyButton.setFont(Variables.BFont)
        self.ButtonSpinBox.setFont(Variables.LFont)
        self.TopLabelSpinBox.setFont(Variables.LFont)
        self.LabelSpinBox.setFont(Variables.LFont)
        
    
    def OkClicked(self):
        self.ApplyClicked()
        QApplication.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Setting()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
