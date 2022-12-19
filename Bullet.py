import numpy as np

class Bullet:
    def __init__(self, position, command):
        self.appearance = 'rectangle'
        self.speed = 10
        self.position = np.array([position[0]-2, position[1]-2, position[0]+2, position[1]+2])
        self.direction = {'up' : False, 'down' : False, 'left' : False, 'right' : False}
        self.state = None
        self.outline = "#0000FF"
        if command['up_pressed']:
            self.direction['up'] = True
        if command['down_pressed']:
            self.direction['down'] = True
        if command['right_pressed']:
            self.direction['right'] = True
        if command['left_pressed']:
            self.direction['left'] = True
            
        

    def move(self):
        if self.direction['up']:
            self.position[1] -= self.speed
            self.position[3] -= self.speed

        if self.direction['down']:
            self.position[1] += self.speed
            self.position[3] += self.speed

        if self.direction['left']:
            self.position[0] -= self.speed
            self.position[2] -= self.speed
            
        if self.direction['right']:
            self.position[0] += self.speed
            self.position[2] += self.speed
        
            
    def collision_check(self, enemys):
        for enemy in enemys:
            collision = self.overlap(self.position, enemy.position)
            
            # 일반 총알의 경우 적에게 데미지를 1만큼 준다.
            if collision:
                enemy.health -= 1
                if enemy.health <= 0:
                    enemy.state = 'die'
                self.state = 'hit'

    # 두 영역 겹치는지 여부
    def overlap(self, bullet_position, enemy_position):
        return enemy_position[0] < bullet_position[2] < enemy_position[2] and bullet_position[1] < enemy_position[3]