import numpy as np
from PIL import Image, ImageDraw, ImageFont

class Character:
    def __init__(self, width, height):
        self.appearance = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/laptop.png").convert("RGBA")
        print(self.appearance)
        self.state = None
        self.item = 0
        self.health = 3
        self.life = 'live'
        self.position = np.array([width-32, height-32, width, height])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
    
    def check_life(self):
        if self.health <= 0:
            return 'delete'
    
    def move(self, command = None):
        if command['move'] == False:
            self.state = None
            self.outline = "#FFFFFF"
        
        else:
            self.state = 'move'
            self.outline = "#FF0000"

            if command['up_pressed']:
                self.position[1] -= 5
                self.position[3] -= 5

            elif command['down_pressed']:
                self.position[1] += 5
                self.position[3] += 5

            elif command['left_pressed']:
                self.position[0] -= 5
                self.position[2] -= 5
                
            elif command['right_pressed']:
                self.position[0] += 5
                self.position[2] += 5
        #center update
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])