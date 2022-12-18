#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import time
import random as rd
import cv2 as cv
import numpy as np
from colorsys import hsv_to_rgb
from EnemyBoss import EnemyBoss
from EnemyDB import EnemyDB
from EnemyESW import EnemyESW
from EnemyOOP import EnemyOOP
from EnemySYSPRO import EnemySYSPRO
from SYSPROBullet import SYSPROBullet
from EnemyChildBullet import EnemyChildBullet
from OOPBullet import OOPBullet
from ESWBullet import ESWBullet
from Bullet import Bullet
from Character import Character
from ChromeItem import ChromeItem
from GithubItem import GithubItem
#from Shield import Shield
from Joystick import Joystick

def main():
    item_y_position = rd.randrange(130, 210)
    item_x_position = rd.randrange(100, 150)
    chrome_item = ChromeItem(item_y_position, item_x_position)
    
    item_y_position = rd.randrange(10, 90)
    item_x_position = rd.randrange(100, 150)
    github_item = GithubItem(item_y_position, item_x_position)
    
    enemy_boss = EnemyBoss((80, 30))
    enemy_DB = EnemyDB((30, 75))
    enemy_SYSPRO = EnemySYSPRO((90, 75))
    enemy_ESW = EnemyESW((150, 75))
    enemy_OOP = EnemyOOP((210, 75))
    
    enemys = [enemy_DB, enemy_SYSPRO, enemy_ESW, enemy_OOP]
    items = [chrome_item, github_item]
    
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
    
    # 캐릭터 총알 리스트
    bullets = []
    
    # 적들 총알 리스트
    db_bullets = []
    oop_bullets = []
    esw_bullets = []
    syspro_bullets = []
    
    
    joystick.disp.image(my_image)
    laptop = Character(joystick.width, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
    
    while True:

        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False, 'A_pressed' : False}
        command_list  = [' ', ' ', ' ', ' ', ' ', ' ', 'down_pressed', ' ', ' ' , ' ' , ' ', ' ', ' ', 'down_pressed', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        
        
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
            command['A_pressed'] = True
            bullet = Bullet(laptop.center, command)
            bullets.append(bullet)
            
        laptop.move(command)
        for bullet in bullets:
            bullet.collision_check(enemys)
            bullet.move()
        
        print(command_list[rd.randrange(len(command_list))])
        db_bullet = EnemyChildBullet(enemy_DB.center, command_list[rd.randrange(len(command_list))])
        esw_bullet = EnemyChildBullet(enemy_ESW.center, command_list[rd.randrange(len(command_list))])
        syspro_bullet = EnemyChildBullet(enemy_SYSPRO.center, command_list[rd.randrange(len(command_list))])
        oop_bullet = EnemyChildBullet(enemy_OOP.center, command_list[rd.randrange(len(command_list))])
                                
        
        db_bullets.append(db_bullet)
        db_bullets.append(esw_bullet)
        db_bullets.append(syspro_bullet)
        db_bullets.append(oop_bullet)
        for child_bullet in db_bullets:
            child_bullet.move()
            
            #bullet.collision_check(enemys)

        
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
        my_image.paste(enemy_boss.appearance, (enemy_boss.position[0], enemy_boss.position[1]),enemy_boss.appearance)
        # my_image.paste(enemy_DB.appearance, (enemy_DB.position[0], enemy_DB.position[1]),enemy_DB.appearance)
        # my_image.paste(enemy_SYSPRO.appearance, (enemy_SYSPRO.position[0], enemy_SYSPRO.position[1]),enemy_SYSPRO.appearance)
        # my_image.paste(enemy_ESW.appearance, (enemy_ESW.position[0], enemy_ESW.position[1]),enemy_ESW.appearance)
        # my_image.paste(enemy_OOP.appearance, (enemy_OOP.position[0], enemy_OOP.position[1]),enemy_OOP.appearance)
        my_image.paste(laptop.appearance, (laptop.position[0], laptop.position[1]),laptop.appearance)
        my_image.paste(chrome_item.appearance, (chrome_item.position[0], chrome_item.position[1]),chrome_item.appearance)
        my_image.paste(github_item.appearance, (github_item.position[0], github_item.position[1]),github_item.appearance)
        
        
        for enemy in enemys:
            if enemy.state != 'die':
                my_image.paste(enemy.appearance, (enemy.position[0], enemy.position[1]),enemy.appearance)
            elif enemy.state == 'die':
                enemys.remove(enemy)
                break
        
        for db_bullet in db_bullets:
            if db_bullet.state !='hit':
                my_draw.rectangle(tuple(db_bullet.position), outline = db_bullet.outline, fill = (235, 51, 36))
        
        for bullet in bullets:
            if bullet.state != 'hit':
                if (command['A_pressed'] == True) and (command['up_pressed']  == False) and (command['down_pressed']  == False) and (command['right_pressed']  == False) and (command['left_pressed']  == False):
                    my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0, 0, 0, 0))
                    bullets.remove(bullet)
                                       
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0, 0, 255))
            else:
                bullets.remove(bullet)
                
                
        joystick.disp.image(my_image)        

if __name__ == '__main__':
    main()

