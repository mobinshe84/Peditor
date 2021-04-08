'''
    def BackClicked(self):
        try:
            _ = OpenAddress
        except:
            QCoreApplication.exit()
            return
        DontSaveFileMessage = QMessageBox()
        DontSaveFileMessage.setWindowTitle("Peditor")
        DontSaveFileMessage.setText("Do you want to save changes?")
        DontSaveFileMessage.setIcon(QMessageBox.Question)
        DontSaveFileMessage.setStandardButtons(QMessageBox.Save|QMessageBox.Close|QMessageBox.Cancel)
        DontSaveFileMessage.buttonClicked.connect(self.BackSaveClicked)
        x = DontSaveFileMessage.exec_()
    
    def BackSaveClicked(self, i):
        Answer = i.text()
        if Answer == "Save":
            print("Save")
        elif Answer == "Close":
            QCoreApplication.exit()
'''