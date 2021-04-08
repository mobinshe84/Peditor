'''
msg = QMessageBox()
msg.setWindowTitle("X")
msg.setText("Y")
msg.setIcon(QMessageBox.Question)
msg.setStandardButtons(X|Y|Z|...)
msg.setDefaultButton(QMessageBox.No)
msg.buttonClicked.connect(self....)
x = msg.exec_()


QMessageBox_setIcon:
QMessageBox.Critical
QMessageBox.Warning
QMessageBox.Information
QMessageBox.Question

QMessageBox_setStandardButtons:

QMessageBox.Cancel
QMessageBox.Open
QMessageBox.Discard
QMessageBox.REset
QMessageBox.No
QMessageBox.NoToAll
QMessageBox.NoButton
QMessageBox.RestoreDefaults
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore
QMessageBox.Ok
QMessageBox.Help
QMessageBox.Save
QMessageBox.SaveAll
QMessageBox.Close
QMessageBox.Apply
QMessageBox.Yes
QMessageBox.YesToAll

msg.setInformativeText("")
msg.setDetailedText("details")
'''