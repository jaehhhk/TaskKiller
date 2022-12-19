import numpy as np

class ItemBullet:
    def __init__(self, position, command):
        self.appearance = 'rectangle'
        self.speed = 10
        self.damage = 10
        self.position = np.array([position[0]-3, position[1]-3, position[0]+3, position[1]+3])
        self.direction = {'up' : False, 'down' : False, 'left' : False, 'right' : False, 'static' : False}
        self.state = None
        self.outline = "#FFFD55"
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
            
            if collision:
                enemy.health -= 5   # 필살기 총알은 일반 총알에 5배 데미지
                if enemy.health <= 0:
                    enemy.state = 'die'
                self.state = 'hit'

    def overlap(self, bullet_position, enemy_position):
        return enemy_position[0] < bullet_position[2] < enemy_position[2] and bullet_position[1] < enemy_position[3]