'''
Ice kingdom Bold
20
True
MS Reference Sans Serif
8
MS Reference Sans Serif
10
'''

from PyQt5 import QtGui
HelpText = '''Peditor!
You can use this app to Compress your Picture and Video!
and this app can disappear everythings you want in picture and Video!'''

#LoadData
FontData = []
FontDataFile = open(r'Data.txt', 'r')
for line in FontDataFile.readlines():
    if line[len(line) - 1:] != "\n":
        FontData.append(line[:len(line)])
        break
    FontData.append(line[:len(line) - 1])
FontDataFile.close()

# TL = Top Label
TLFamily = FontData[0]
TLSize = int(FontData[1])

TLUnderLine = FontData[2]
TLFont = QtGui.QFont()
TLFont.setFamily(TLFamily)
TLFont.setPointSize(TLSize)
TLFont.setUnderline(bool(TLUnderLine))

# B = Button
BFamily = FontData[3]
BSize = int(FontData[4])

BFont = QtGui.QFont()
BFont.setFamily(BFamily)
BFont.setPointSize(BSize)

# L = Label
LFamily = FontData[5]
LSize = int(FontData[6])
LFont = QtGui.QFont()
LFont.setFamily(LFamily)
LFont.setPointSize(LSize)

def LoadFont(self):
    
    FontData = []
    FontDataFile = open(r'Data.txt', 'r')
    for line in FontDataFile.readlines():
        if line[len(line) - 1:] != "\n":
            FontData.append(line[:len(line)])
            break
        FontData.append(line[:len(line) - 1])
    FontDataFile.close()
    global TLFamily
    global TLSize
    global TLUnderLine
    global TLFont
    global BFamily
    global BSize
    global BFont
    global LFamily
    global LSize
    global LFont
    
    TLFamily = FontData[0]
    TLSize = int(FontData[1])
    TLUnderLine = FontData[2]
    TLFont = QtGui.QFont()
    TLFont.setFamily(TLFamily)
    TLFont.setPointSize(TLSize)
    TLFont.setUnderline(bool(TLUnderLine))
    
    BFamily = FontData[3]
    BSize = int(FontData[4])
    BFont = QtGui.QFont()
    BFont.setFamily(BFamily)
    BFont.setPointSize(BSize)
    
    LFamily = FontData[5]
    LSize = int(FontData[6])
    LFont = QtGui.QFont()
    LFont.setFamily(LFamily)
    LFont.setPointSize(LSize)