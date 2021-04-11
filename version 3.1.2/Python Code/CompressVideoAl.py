import PIL.Image
from moviepy.editor import *
import time

class CompressingVideo:
    
    def __init__(self, Address, Dialog, Window, SaveAddress, Main):
        time.sleep(1.)
        self.Address, self.SaveAddress, self.folder, self.img_name = Address, SaveAddress, 'frames', 'frame'
        self.load_video()
        self.get_FPS()
        self.save_frames(Window)
        Main.close()
        Dialog.close()

    def load_video(self):
        self.video = VideoFileClip(self.Address)
        self.audio = self.video.audio
        self.resolution = 30

    def get_FPS(self):
        self.seconds = self.video.duration
        self.FPS = 29

    def save_frames(self, Window):
        self.seconds = int(self.seconds)
        self.FPS = int(self.FPS)
        image_paths = []
        x = 0
        for i in range(self.FPS * self.seconds):
            if i / (self.FPS * self.seconds) * 100 // 1 > x:
                x += 1
                Window.progressBar.setProperty("value", x)
            self.video.save_frame("{}/{} {}.jpg".format(self.folder, self.img_name, i), t = i / self.FPS)
            self.compress_img(i)
            image_paths.append("{}/{} {}.jpg".format(self.folder, self.img_name, i))
        
        x = 100
        Window.progressBar.setProperty("value", x)
        Window.label_Processing.setText('Wait a minute...')

        self.video = ImageSequenceClip(image_paths, fps=self.FPS, load_images=True)
        self.video.audio = self.audio
        self.video.write_videofile(self.SaveAddress)
        for i in range(self.FPS * self.seconds):
            os.remove("{}/{} {}.jpg".format(self.folder, self.img_name, i))
        
    def compress_img(self, num):
        img = PIL.Image.open("{}/{} {}.jpg".format(self.folder, self.img_name, num))
        img.save("{}/{} {}.jpg".format(self.folder, self.img_name, num), optimize=True, quality=self.resolution)