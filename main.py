from PIL import Image, ImageDraw, ImageFont
import time
import random as rd
import cv2 as cv
import numpy as np
from colorsys import hsv_to_rgb
from EnemyBoss import EnemyBoss
from Bullet import Bullet
from Character import Character
from Item import Item
#from Shield import Shield
from Joystick import Joystick

def main():
    item_y_position = rd.randrange(10, 210)
    item_x_position = rd.randrange(100, 150)
    chrome_item = Item(item_y_position, item_x_position)
    github_item = Item(item_y_position, item_x_position)
    
    enemy_boss = EnemyBoss((80, 30))
    
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
    #enemy_boss_image = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/enemy_boss.png")
    #enemy_boss_image = enemy_boss_image.resize((100, 28))
    #laptop = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/laptop.png")
    #laptop = laptop.resize((45,45))
    #my_image.paste(enemy_boss_image, (70,0))
    #my_image.paste(laptop, (100, 200))
    
    bullets = []
    joystick.disp.image(my_image)
    laptop = Character(joystick.width, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
    
    while True:

        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True
        
        if not joystick.button_A.value: # A pressed
            bullet = Bullet(laptop.position, command)
            bullets.append(bullet)
            
        laptop.move(command)
        
        for bullet in bullets:
            #bullet.collision_check(enemys_list)
            bullet.move()

        
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
        my_image.paste(enemy_boss.appearance, (enemy_boss.position[0], enemy_boss.position[1]),enemy_boss.appearance)
        my_image.paste(laptop.appearance, (laptop.position[0], laptop.position[1]),laptop.appearance)
        my_image.paste(chrome_item.appearance, (chrome_item.position[0], chrome_item.position[1]),chrome_item.appearance)
        
        
        for bullet in bullets:
            if bullet.state != 'hit':
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0, 0, 255))
        
        #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        #joystick.disp.image(my_image)
        joystick.disp.image(my_image)        

if __name__ == '__main__':
    main()

