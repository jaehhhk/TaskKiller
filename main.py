#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import time
import random as rd
import cv2 as cv
import numpy as np
from colorsys import hsv_to_rgb
from EnemyBoss import EnemyBoss
from Health import Health
from EnemyDB import EnemyDB
from EnemyESW import EnemyESW
from EnemyOOP import EnemyOOP
from EnemySYSPRO import EnemySYSPRO
from EnemyChildBullet import EnemyChildBullet
from EnemyBossBullet import EnemyBossBullet
from Bullet import Bullet
from ItemBullet import ItemBullet
from Character import Character
from ChromeItem import ChromeItem
from GithubItem import GithubItem
#from Shield import Shield
from Joystick import Joystick

def main():
    
    
    
    health1 = Health((0,0))
    health2 = Health((20,0))
    health3 = Health((40,0))
    health_list = [health3, health2, health1]
    
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
    
    #my_image.paste(health1.appearance, (health1.position[0], health1.position[1]),health1.appearance)
    
    # for health in health_list:
    #     my_image.paste(health.appearance, (health.position[0], health.position[1]),health.appearance)
    #enemy_boss_image = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/enemy_boss.png")
    #enemy_boss_image = enemy_boss_image.resize((100, 28))
    #laptop = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/laptop.png")
    #laptop = laptop.resize((45,45))
    #my_image.paste(enemy_boss_image, (70,0))
    #my_image.paste(laptop, (100, 200))
    
    

    while True:
        start_img = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/start.png")
        my_image.paste(start_img, (0,0), start_img)
        
        if not joystick.button_A.value: # A pressed
            break
        

    
    # 캐릭터 총알 리스트
    bullets = []
    item_bullets = []
    
    # 적들 총알 리스트
    db_bullets = []
    
    trash_bullet = []
        
    joystick.disp.image(my_image)
    laptop = Character(joystick.width, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
    



    # if laptop.health == 2:
    #     health_list.pop()
    # if laptop.health == 1:
    #     health_list.pop()
    # if laptop.health == 0:
    #     my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
    
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
            #command['A_pressed'] = True
            if command['move'] == True:
                bullet = Bullet(laptop.center, command)
                bullets.append(bullet)
            
        if not joystick.button_B.value: # B presseed
            if laptop.item == 2:
                if command['move'] == True:
                    item_bullet = ItemBullet(laptop.center, command)
                    item_bullets.append(item_bullet)
                         
            
        laptop.move(command)
        
        for bullet in bullets:
            bullet.collision_check(enemys)
            bullet.move()

        for item_bullet in item_bullets:
            item_bullet.collision_check(enemys)
            item_bullet.move()
            
        # 캐릭터가 총알을 쏘는 로직을 응용하여 랜덤으로 command를 받도록 했다.
        # 난이도 조절을 위해 command_list의 요소들 중간중간 null 값을 넣어주었다.
        db_bullet = EnemyChildBullet(enemy_DB.center, command_list[rd.randrange(len(command_list))])
        esw_bullet = EnemyChildBullet(enemy_ESW.center, command_list[rd.randrange(len(command_list))])
        syspro_bullet = EnemyChildBullet(enemy_SYSPRO.center, command_list[rd.randrange(len(command_list))])
        oop_bullet = EnemyChildBullet(enemy_OOP.center, command_list[rd.randrange(len(command_list))])
        
        boss_bullet = EnemyBossBullet(enemy_boss.center, command_list[rd.randrange(len(command_list))])
                                
        if enemy_DB in enemys:
            db_bullets.append(db_bullet)
        
        if enemy_ESW in enemys:
            db_bullets.append(esw_bullet)
        
        if enemy_SYSPRO in enemys:
            db_bullets.append(syspro_bullet)
        
        if enemy_OOP in enemys:    
            db_bullets.append(oop_bullet)
        
        for child_bullet in db_bullets:
            child_bullet.move()
            child_bullet.collision_check(laptop)
            

        
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
        my_image.paste(enemy_boss.appearance, (enemy_boss.position[0], enemy_boss.position[1]),enemy_boss.appearance)
        # my_image.paste(enemy_DB.appearance, (enemy_DB.position[0], enemy_DB.position[1]),enemy_DB.appearance)
        # my_image.paste(enemy_SYSPRO.appearance, (enemy_SYSPRO.position[0], enemy_SYSPRO.position[1]),enemy_SYSPRO.appearance)
        # my_image.paste(enemy_ESW.appearance, (enemy_ESW.position[0], enemy_ESW.position[1]),enemy_ESW.appearance)
        # my_image.paste(enemy_OOP.appearance, (enemy_OOP.position[0], enemy_OOP.position[1]),enemy_OOP.appearance)
        my_image.paste(laptop.appearance, (laptop.position[0], laptop.position[1]),laptop.appearance)
        #my_image.paste(chrome_item.appearance, (chrome_item.position[0], chrome_item.position[1]),chrome_item.appearance)
        #my_image.paste(github_item.appearance, (github_item.position[0], github_item.position[1]),github_item.appearance)
        
        if laptop.health == 3:
            my_image.paste(health1.appearance, (health1.position[0], health1.position[1]),health1.appearance)
            my_image.paste(health2.appearance, (health2.position[0], health2.position[1]),health2.appearance)
            my_image.paste(health3.appearance, (health3.position[0], health3.position[1]),health3.appearance)
        if laptop.health == 2:
            my_image.paste(health2.appearance, (health2.position[0], health2.position[1]),health2.appearance)
            my_image.paste(health3.appearance, (health3.position[0], health3.position[1]),health3.appearance)
            #my_draw.rectangle(tuple(health3.position), fill=(0, 0, 255))
        if laptop.health == 1:
            my_image.paste(health3.appearance, (health3.position[0], health3.position[1]),health3.appearance)
        
        for item in items:
            if item.state != 'get':
                my_image.paste(item.appearance, (item.position[0], item.position[1]),item.appearance)
            if item.getItem(laptop):
                items.remove(item)
                break
                     
        
        for enemy in enemys:
            if enemy.state != 'die':
                my_image.paste(enemy.appearance, (enemy.position[0], enemy.position[1]),enemy.appearance)
            elif enemy.state == 'die':
                enemys.remove(enemy)
                break
                
        
        for db_bullet in db_bullets:
            if db_bullet.state !='hit':
                my_draw.rectangle(tuple(db_bullet.position), outline = db_bullet.outline, fill = (235, 51, 36))
            else:
                db_bullets.remove(db_bullet)                         
        
        for bullet in bullets:
            if bullet.state != 'hit':
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0, 0, 255))
            else:
                bullets.remove(bullet)
        
        for item_bullet in item_bullets:
            if item_bullet.state != 'hit':
                my_draw.ellipse(tuple(item_bullet.position), outline = item_bullet.outline, fill = (255, 253, 85))
            else:
                item_bullets.remove(item_bullet)
                
        if len(enemys) == 0:
            boss_bullets = []
            if enemy_boss.state != 'die':
                my_image.paste(enemy_boss.appearance, (enemy_boss.position[0], enemy_boss.position[1]),enemy_boss.appearance)
                
                boss_bullets.append(boss_bullet)
                
                for child_bullet in db_bullets:
                    child_bullet.move()
                    child_bullet.collision_check(laptop)
                    
                    
                    
            elif enemy_boss.state == 'die':
                my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
                break
                
        
        # for health in health_list:
        #     if laptop.health == 3:
        #         for i in range(3):
        #             my_image.paste(health_list[i].appearance, (health_list[i].position[0], health_list[i].position[1]),health_list[i].appearance)
        #     if laptop.health == 2:
        #         health_list.pop(-1)
        #         for i in range(2):
        #             my_image.paste(health_list[i].appearance, (health_list[i].position[0], health_list[i].position[1]),health_list[i].appearance)
            
            # if laptop.health == 2:
            #     health.state == 'delete'                    
            # if laptop.health == 2:
            #     health_list.pop()
            # if laptop.health == 1:
            #     health_list.pop()
            # else: my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
      
                     
        joystick.disp.image(my_image)        

if __name__ == '__main__':
    main()

