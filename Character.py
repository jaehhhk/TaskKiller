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
        self.position = np.array([width-32, height-32, width+32, height+32])
        # 총알 발사를 위한 캐릭터 중앙 점 추가
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#FFFFFF"

    
    def check_life(self):
        if self.health <= 0:
            return 'delete'
    
    def move(self, command = None):
        if command['move'] == False:
            self.state = None
            self.outline = "#FFFFFF" #검정색상 코드!
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" #빨강색상 코드!

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