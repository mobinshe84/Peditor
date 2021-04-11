'''
MS Reference Sans Serif
20
True
MS Reference Sans Serif
10
MS Reference Sans Serif
10
'''

from PyQt5 import QtGui

class Variables:
    def __init__(self):
        self.HelpText = '''Peditor!
You can use this app to Compress your Picture and Video!
and this app can disappear everythings you want in picture and Video!'''

        File = open('Data.txt', 'r')
        self.TLFamily = File.readline()[:-1]
        self.TLSize = int(File.readline()[:-1])
        self.TLUnderLine = bool(File.readline()[:-1] == 'True')
        self.TLFont = QtGui.QFont(self.TLFamily, self.TLSize)
        self.TLFont.setUnderline(self.TLUnderLine)
        self.BFamily = File.readline()[:-1]
        self.BSize = int(File.readline()[:-1])
        self.BFont = QtGui.QFont(self.BFamily, self.BSize)
        self.LFamily = File.readline()[:-1]
        self.LSize = int(File.readline())
        self.LFont = QtGui.QFont(self.LFamily, self.LSize)
    
    def ResetFonts(self, TLFamily, TLSize, BFamily, BSize, LFamily, LSize):
        File = open('Data.txt', 'w')
        File.write(f'{TLFamily}\n{TLSize}\nTrue\n{BFamily}\n{BSize}\n{LFamily}\n{LSize}')
        File.close()
        File = open('Data.txt', 'r')
        self.TLFamily = File.readline()[:-1]
        self.TLSize = int(File.readline()[:-1])
        self.TLUnderLine = bool(File.readline()[:-1] == 'True')
        self.TLFont = QtGui.QFont(self.TLFamily, self.TLSize)
        self.TLFont.setUnderline(self.TLUnderLine)
        self.BFamily = File.readline()[:-1]
        self.BSize = int(File.readline()[:-1])
        self.BFont = QtGui.QFont(self.BFamily, self.BSize)
        self.LFamily = File.readline()[:-1]
        self.LSize = int(File.readline())
        self.LFont = QtGui.QFont(self.LFamily, self.LSize)