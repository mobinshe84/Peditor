from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
import PIL.Image
from moviepy.editor import *
import threading


class Ui_CompressingVideo(QWidget):
    def setupUi(self, Peditor):
        Peditor.setObjectName("MainWindow")
        Peditor.resize(339, 239)
        self.centralwidget = QtWidgets.QWidget(Peditor)
        self.centralwidget.setObjectName("centralwidget")
        #-------Labels-------#
        #CompressVideoLabel
        self.CompressVideoLabel = QtWidgets.QLabel(self.centralwidget)
        self.CompressVideoLabel.setGeometry(QtCore.QRect(0, 10, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Ice kingdom")
        font.setPointSize(20)
        font.setUnderline(True)
        font.setWeight(75)
        self.CompressVideoLabel.setFont(font)
        self.CompressVideoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CompressVideoLabel.setObjectName("NameLabel")
        #CompressingLabel
        self.CompressingLabel = QtWidgets.QLabel(self.centralwidget)
        self.CompressingLabel.setGeometry(QtCore.QRect(30, 80, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.CompressingLabel.setFont(font)
        self.CompressingLabel.setObjectName("CompressingLabel")
        #-------ProgressBars-------#
        Ui_CompressingVideo.ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ProgressBar.setGeometry(QtCore.QRect(30, 110, 291, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.ProgressBar.setFont(font)
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName("progressBar")
        #-------Buttons-------#
        #CancelButton
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QtCore.QRect(120, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.CancelButton.setFont(font)
        self.CancelButton.setObjectName("CancelButton")
        self.CancelButton.clicked.connect(self.CancelClicked)
        Peditor.setCentralWidget(self.centralwidget)

        self.retranslateUi(Peditor)
        QtCore.QMetaObject.connectSlotsByName(Peditor)

    def retranslateUi(self, Peditor):
        _translate = QtCore.QCoreApplication.translate
        Peditor.setWindowTitle(_translate("Peditor", "Peditor"))
        self.CompressVideoLabel.setText(_translate("Peditor", "Video Compressing"))
        self.CompressingLabel.setText(_translate("Peditor", "Compressing..."))
        self.CancelButton.setText(_translate("Peditor", "Cancel"))
        
    def SaveFile(self):
        filename = QtWidgets.QFileDialog()
        filename.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        filename.setNameFilters(["mp4 video (*.mp4)",
                               "wmv Video (*.wmv)",
                               "Matroska (*.mkv)",
                               "Quick Time (*.mov)",
                               "avi video (*.avi)"])
        if filename.exec_() == QtWidgets.QDialog.Accepted:
            global SavedAddress
            SavedAddress = str(filename.selectedFiles()[0])
        else:
            return
    
    def CancelClicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("Peditor")
        msg.setText("Do you sure to want to back?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msg.buttonClicked.connect(self.BackClicked2)
        x = msg.exec_()
    def CancelClicked2(self, i):
        i = i.text()
        if i == "&Yes":
            exit()
    
    def ReloadProgressBar(self, x):
        Ui_CompressingVideo.ProgressBar.setProperty("value", x)

class CompressingVideo():
    # ---------------------------------------------------------------------------------------------------------- #
    def Compress(self, Address):
        folder, img_name, video_name = 'frames', 'frame', 'new video/new'
        audio, video, resolution = self.load_video(self, Address)
        FPS, seconds = self.get_FPS(self, video)
        self.save_frames(self, seconds, FPS, video, resolution, folder, img_name, video_name, audio)
        exit()
# ---------------------------------------------------------------------------------------------------------- #
    def load_video(self, Address):
        try:
            videoclip = VideoFileClip(Address)
            audioclip = videoclip.audio
            resolution = 30
        except:
            print("Cannot read format file! Please pick a right one")
            audioclip, videoclip, resolution = self.open_movie()
        return audioclip, videoclip, resolution
# ---------------------------------------------------------------------------------------------------------- #
    def get_FPS(self, video):
        seconds = video.duration
        FPS = 29
        return FPS, seconds
# ---------------------------------------------------------------------------------------------------------- #
    def save_frames(self, seconds, FPS, video, resolution, folder, img_name, video_name, audio):
        seconds = int(seconds)
        FPS = int(FPS)
        image_paths = []
        x = 0
        for i in range(FPS * seconds):
            if i / (FPS * seconds) * 100 // 1 > x:
                x += 1
                print(x)
                ReloadCompressing(x)
            video.save_frame("{}/{} {}.jpg".format(folder, img_name, i), t=i/FPS)
            self.compress_img(self, folder, img_name, i, resolution)
            image_paths.append("{}/{} {}.jpg".format(folder, img_name, i))
        ReloadCompressing(x + 1)
        Ui_CompressingVideo.SaveFile(Ui_CompressingVideo)
        video = ImageSequenceClip(image_paths, fps=FPS, load_images=True)
        video.audio = audio
        video.write_videofile("{}.mp4".format(video_name))
        for i in range(FPS * seconds):
            os.remove("{}/{} {}.jpg".format(folder, img_name, i))
        
# ---------------------------------------------------------------------------------------------------------- #
    def compress_img(self, folder, img_name, num, resolution):
        img = PIL.Image.open("{}/{} {}.jpg".format(folder, img_name, num))
        img.save("{}/{} {}.jpg".format(folder, img_name, num), optimize=True, quality=resolution)
        
def ReloadCompressing(x = 0):
    CompressingUi = Ui_CompressingVideo()
    CompressingUi.ReloadProgressBar(x)
# ---------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------- main ------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Peditor = QtWidgets.QMainWindow()
    ui = Ui_CompressingVideo()
    ui.setupUi(Peditor)
    UiThread = threading.Thread(target = Peditor.show())
    sys.exit(app.exec_())
