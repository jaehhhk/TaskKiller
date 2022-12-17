from PIL import Image, ImageDraw, ImageFont
import random as rd
import numpy as np

class GithubItem:
    def __init__(self, item_y_position, item_x_position):
        self.appearance = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/github_item.png")
        self.position = np.array([item_y_position,item_x_position])