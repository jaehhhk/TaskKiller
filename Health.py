from PIL import Image, ImageDraw, ImageFont
import numpy as np
from Character import Character


class Health:
    def __init__(self, spawn_position):
        self.appearance = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/health.png")
        self.state = 'life'
        self.health = 50
        self.position = np.array([spawn_position[0], spawn_position[1], spawn_position[0], spawn_position[1]])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"