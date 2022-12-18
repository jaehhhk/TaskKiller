from PIL import Image, ImageDraw, ImageFont
import random as rd
import numpy as np

class ChromeItem:
    def __init__(self, item_x_position, item_y_position):
        self.appearance = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/chrome_item.png")
        self.position = np.array([item_x_position,item_y_position,item_x_position,item_y_position])
        self.state = None
    def getItem(self, laptop):
        get_github = self.overlap(self.position, laptop.position)
        if get_github:
            laptop.item += 1
            self.state = 'get'
            return True
        else: False
            
    def overlap(self, item_position, laptop_position):
        # item_position[0] > laptop_position[0] and item_position[1] > laptop_position[1]\
        # and item_position[2] < laptop_position[2] and item_position[3] < laptop_position[3]
         return laptop_position[0]< item_position[2] < laptop_position[2] and laptop_position[1] < item_position[3] < laptop_position[3]