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
from Bullet import Bullet
from ItemBullet import ItemBullet
from Character import Character
from ChromeItem import ChromeItem
from GithubItem import GithubItem
from Joystick import Joystick

def main():
    
    # 화면에 표시되는 체력 객체
    health1 = Health((0,0))
    health2 = Health((20,0))
    health3 = Health((40,0))
    health_list = [health3, health2, health1]
    
    # 아이템의 스폰 위치는 화면내 일정 범위 안에서 랜덤으로
    item_y_position = rd.randrange(130, 210)
    item_x_position = rd.randrange(100, 150)
    chrome_item = ChromeItem(item_y_position, item_x_position)
    
    item_y_position = rd.randrange(10, 90)
    item_x_position = rd.randrange(100, 150)
    github_item = GithubItem(item_y_position, item_x_position)
    
    # LMS 와 부하 적들 객체 생성
    enemy_boss = EnemyBoss((80, 30))
    enemy_DB = EnemyDB((30, 75))
    enemy_SYSPRO = EnemySYSPRO((90, 75))
    enemy_ESW = EnemyESW((150, 75))
    enemy_OOP = EnemyOOP((210, 75))
    
    # 적들과 아이템 객체 담는 리스트 
    enemys = [enemy_DB, enemy_SYSPRO, enemy_ESW, enemy_OOP]
    items = [chrome_item, github_item]
    
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
    
    # 결과 페이지
    result_A = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/aplus.png")
    result_B = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/bplus.png")
    result_C = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/cplus.png")
    result_F = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/fail.png")
    
    start_img = Image.open("/home/jaehyeok/Desktop/TaskKiller/Image/start.png")
    # my_image.paste(start_img, (0,0), start_img)
    
    # 웰컴 페이지
    def welcome():
        while True:
            my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
            my_image.paste(start_img, (0,0), start_img) 
            if not joystick.button_A.value: # A pressed
                break
            joystick.disp.image(my_image)
    
    welcome()
    
    # 캐릭터 총알 리스트
    bullets = []
    item_bullets = []
    
    # 적들 총알 리스트
    db_bullets = []
    
    trash_bullet = []
        
    joystick.disp.image(my_image)
    laptop = Character(joystick.width, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
      
    
    while True:
        
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False, 'A_pressed' : False}
        
        # 난이도 조절을 위해 command_list의 요소들 중간중간 null 값을 넣어주었다.
        command_list  = [' ', ' ', ' ', ' ', ' ', ' ', 'down_pressed', ' ', ' ' , ' ' , ' ', ' ', ' ', 'down_pressed', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        
        
        if not joystick.button_U.value:  # up pressed
            if laptop.position[1] >= 0:
                command['up_pressed'] = True
                command['move'] = True

        if not joystick.button_D.value:  # down pressed
            if laptop.position[3] <= 240:
                command['down_pressed'] = True
                command['move'] = True

        if not joystick.button_L.value:  # left pressed
            if laptop.position[0] >= 0:
                command['left_pressed'] = True
                command['move'] = True

        if not joystick.button_R.value:  # right pressed
            if laptop.position[2] <= 240:
                command['right_pressed'] = True
                command['move'] = True
        
        if not joystick.button_A.value: # A pressed
            if command['move'] == True:
                bullet = Bullet(laptop.center, command)
                bullets.append(bullet)
            
        if not joystick.button_B.value: # B presseed 아이템 사용
            if laptop.item == 2:
                if command['move'] == True:
                    item_bullet = ItemBullet(laptop.center, command)
                    item_bullets.append(item_bullet)
                         
            
        laptop.move(command)
        
        # 캐릭터가 쏜 일반 총알과 필살기 총알 적에 맞았는지 여부
        for bullet in bullets:
            bullet.collision_check(enemys)
            bullet.move()

        for item_bullet in item_bullets:
            item_bullet.collision_check(enemys)
            item_bullet.move()
            
        # 캐릭터가 총알을 쏘는 로직을 응용하여 랜덤으로 command를 받도록 했다.
        db_bullet = EnemyChildBullet(enemy_DB.center, command_list[rd.randrange(len(command_list))])
        esw_bullet = EnemyChildBullet(enemy_ESW.center, command_list[rd.randrange(len(command_list))])
        syspro_bullet = EnemyChildBullet(enemy_SYSPRO.center, command_list[rd.randrange(len(command_list))])
        oop_bullet = EnemyChildBullet(enemy_OOP.center, command_list[rd.randrange(len(command_list))])
        
        
        # 총알 객체 생성                        
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
        my_image.paste(laptop.appearance, (laptop.position[0], laptop.position[1]),laptop.appearance)

        # 캐릭터가 총알에 맞으면 체력이 깎임
        if laptop.health == 3:
            my_image.paste(health1.appearance, (health1.position[0], health1.position[1]),health1.appearance)
            my_image.paste(health2.appearance, (health2.position[0], health2.position[1]),health2.appearance)
            my_image.paste(health3.appearance, (health3.position[0], health3.position[1]),health3.appearance)
        if laptop.health == 2:
            my_image.paste(health2.appearance, (health2.position[0], health2.position[1]),health2.appearance)
            my_image.paste(health3.appearance, (health3.position[0], health3.position[1]),health3.appearance)
        if laptop.health == 1:
            my_image.paste(health3.appearance, (health3.position[0], health3.position[1]),health3.appearance)
        
        # 아이템 얻기
        for item in items:
            if item.state != 'get':
                my_image.paste(item.appearance, (item.position[0], item.position[1]),item.appearance)
            if item.getItem(laptop):
                items.remove(item)
                break
                     
        # 적들 체력이 다 끝나면 화면에 사라지기
        for enemy in enemys:
            if enemy.state != 'die':
                my_image.paste(enemy.appearance, (enemy.position[0], enemy.position[1]),enemy.appearance)
            elif enemy.state == 'die':
                enemys.remove(enemy)
                break
                
        # 적들이 쏘는 랜덤 총알이 적에 맞으면 해당 객체는 총알 리스트에 사라져야
        for db_bullet in db_bullets:
            if db_bullet.state !='hit':
                my_draw.rectangle(tuple(db_bullet.position), outline = db_bullet.outline, fill = (235, 51, 36))
            else:
                db_bullets.remove(db_bullet)                         
        
        # 캐릭터가 쏘는 총알이 적에 맞으면 해당 객체는 총알 리스트에 사라져야
        for bullet in bullets:
            if bullet.state != 'hit':
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0, 0, 255))
            else:
                bullets.remove(bullet)
        
        # 캐릭터가 쏜 아이템 필살기 총알
        for item_bullet in item_bullets:
            if item_bullet.state != 'hit':
                my_draw.ellipse(tuple(item_bullet.position), outline = item_bullet.outline, fill = (255, 253, 85))
            else:
                item_bullets.remove(item_bullet)

        # 케릭터가 남은 체력을 다 소진하면 F학점을 맞고 게임 종료
        if laptop.health <= 0:
            my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
            my_image.paste(result_F, (0,0), result_F)
            if not joystick.button_A.value: # A pressed
                    main()
            
        
        # 적들을 전부ㅡ 제거한 후 남아있는 체력을 합산해 점수 도출
        if len(enemys) == 0:
            if laptop.health == 3:
                my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
                my_image.paste(result_A, (0,0), result_A)
                if not joystick.button_A.value: # A pressed
                    main()
                
            
            if laptop.health == 2:
                my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
                my_image.paste(result_B, (0,0), result_B)
                if not joystick.button_A.value: # A pressed
                    main()
                
            if laptop.health == 1:
                my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 0))
                my_image.paste(result_C, (0,0), result_C)
                if not joystick.button_A.value: # A pressed
                    main()
        

                     
        joystick.disp.image(my_image)        

if __name__ == '__main__':
    main()

