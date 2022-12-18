from PIL import Image, ImageDraw, ImageFont
import random as rd
import numpy as np


class EnemyOOP:
    def __init__(self, spawn_position):
        self.appearance = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/enemy_oop.png")
        self.state = 'alive'
        self.health = 50
        self.position = np.array([spawn_position[0]-25, spawn_position[1]-25, spawn_position[0]+25, spawn_position[1]+25])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"