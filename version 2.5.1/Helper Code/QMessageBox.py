'''
msg = QMessageBox()
msg.setWindowTitle("X")
msg.setText(Y")
msg.setIcon(QMessageBox.Question)
msg.setStandardButtons(X|Y|Z|...)
msg.buttonClicked.connect(self....)
x = msg.exec_()


QMessageBox_setIcon:
QMessageBox.Critical
QMessageBox.Warning
QMessageBox.Information
QMessageBox.Question

QMessageBox_setStandardButtons:
QMessageBox.Ok
QMessageBox.Open
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Yes
QMessageBox.No
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore

msg.setInformativeText("")
msg.setDetailedText("details")
'''