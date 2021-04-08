from PyQt5 import QtWidgets
import threading
from PIL import Image
import numpy as np
import os
import cv2
import time

class EncodeImg:
    def __init__(self, Address, Dialog, Window, SavedAddress, Main):
        self.SavedAddress = SavedAddress
        time.sleep(1.0)
        self.image = cv2.imread(Address)
        self.ImageToArray()
        self.WriteInImage(Window)
        Main.close()
        Dialog.close()

    def ImageToArray(self):
        self.width, self.height, self.deep = self.image.shape
        self.array = self.image.reshape((self.width, self.height, self.deep))

    def WriteInImage(self, Window):
        file = open('1.pcif', 'w')
        file.write("{} {} {}".format(self.width, self.height, self.deep))
        per = -1000
        print("------- Compressing Data -------")
        l = []
        for i in range(self.width):
            if per != int(i / self.height * 100):
                x = int(i / self.height * 100)
                Window.progressBar.setProperty("value", x)
                print("| ({}%) has been processed ========== |".format(x))
                per = int(i / self.height * 100)
            file.write('\n')
            k = 10
            pre = ''
            for color in range(self.deep):
                file.write('{}-{} '.format(self.array[0, i, color], 0))
                pre = self.array[0, i, color]
                pos = 0
                for j in range(self.width):
                    if self.array[j, i, color] > pre + k or self.array[j, i, color] < pre - k:
                        pre = self.array[j, i, color]
                        pos = j
                        file.write('{}-{} '.format(pre, pos))
                if pos != self.width-1:
                    file.write('{}-{} '.format(self.array[self.width - 1, i, color], self.width - 1))
                file.write("* ")
        file.close()
        print('----- Done -----')
        x = 100
        Window.progressBar.setProperty("value", x)
        Window.label_Processing.setText('Wait a minute...')
        DecodeImg(self.SavedAddress)

class DecodeImg:
    def __init__(self, SavedAddress):
        array = self.decode_arrays()
        img = Image.fromarray(array.astype(np.uint8))
        b, g, r = img.split()
        self.img = Image.merge("RGB", (r, g, b))
        self.img.save(SavedAddress)
        os.remove('1.pcif')
        
    
    def decode_arrays(self):
        file = open('1.pcif', 'r')
        w, h, d = map(int, file.readline().split())
        new_array = np.array([[[0]*d,]*h,]*w,)
        for i in range(h):
            array = file.readline().split()
            flag = 0
            pre_position = 0
            pre = ''
            for j in array:
                if len(j)==1:
                    flag += 1
                    pre_position = 0
                    pre = ''
                else:
                    item, pos = j.split("-")
                    pos = int(pos)
                    item = int(item)
                    new_array[pos][i][flag] = item
                    for m in range(pre_position, pos):
                        new_array[m][i][flag] = pre
                    pre = item
                    pre_position = pos
        return new_array