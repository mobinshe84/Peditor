
'''
def SaveFile(self):
    filename = QtWidgets.QFileDialog()
    filename.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
    filename.setNameFilters(["JPEG (*.jpg;*.jpeg;*.jpe;*.jfif)","PNG (*.png)"])
    if filename.exec_() == QtWidgets.QDialog.Accepted:
        global SavedAddress
        SavedAddress = str(filename.selectedFiles()[0])
        print(SavedAddress)
    else:
        return
'''