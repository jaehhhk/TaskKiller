from PIL import Image, ImageDraw, ImageFont
import random as rd
import numpy as np

class GithubItem:
    def __init__(self, item_x_position, item_y_position):
        self.appearance = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/github_item.png")
        self.position = np.array([item_x_position,item_y_position,item_x_position,item_y_position])
        self.state = None
        
    def getItem(self, laptop):
        get_github = self.overlap(self.position, laptop.position)
        if get_github:
            laptop.item += 1    # 아이템 갯수 추가
            self.state = 'get'
            return True
        else: False
            
    def overlap(self, item_position, laptop_position):
         return laptop_position[0]< item_position[2] < laptop_position[2] and laptop_position[1] < item_position[3] < laptop_position[3]