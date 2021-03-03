# ---------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------- modules ----------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------- #
import PIL.Image
from tkinter import filedialog
from tkinter import *
from moviepy.editor import *
# ---------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------- class ------------------------------------------------ #
# ---------------------------------------------------------------------------------------------------------- #
class compressing_video():
    # ---------------------------------------------------------------------------------------------------------- #
    def __init__(self):
        super(compressing_video, self).__init__()
        folder, img_name, video_name = 'frames', 'frame', 'new video/new'
        audio, video, resolution = self.load_video()
        FPS, seconds = self.get_FPS(video)
        self.save_frames(seconds, FPS, video, resolution, folder, img_name, video_name, audio)
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
        for i in range(FPS * seconds):
            video.save_frame("{}/{} {}.jpg".format(folder, img_name, i), t=i/FPS)
            self.compress_img(folder, img_name, i, resolution)
            image_paths.append("{}/{} {}.jpg".format(folder, img_name, i))
        video = ImageSequenceClip(image_paths, fps=FPS, load_images=True)
        video.audio = audio
        video.write_videofile("{}.mp4".format(video_name))
        for i in range(FPS * seconds):
            os.remove("{}/{} {}.jpg".format(folder, img_name, i))
# ---------------------------------------------------------------------------------------------------------- #
    def compress_img(self, folder, img_name, num, resolution):
        img = PIL.Image.open("{}/{} {}.jpg".format(folder, img_name, num))
        img.save("{}/{} {}.jpg".format(folder, img_name, num), optimize=True, quality=resolution)
# ---------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------- main ------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    compressing_video()
