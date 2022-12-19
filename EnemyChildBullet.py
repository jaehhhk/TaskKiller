import numpy as np

class EnemyChildBullet:
    def __init__(self, position, command):
        self.appearance = 'rectangle'
        self.speed = 5
        self.damage = 20
        self.position = np.array([position[0]-1, position[1]-1, position[0]+1, position[1]+1])
        self.direction = {'up' : False, 'down' : False, 'left' : False, 'right' : False, 'static' : False}
        self.state = None
        self.outline = "#EB3324"
        if command == 'up_pressed':
            self.direction['up'] = True
        if command == 'down_pressed':
            self.direction['down'] = True
        if command == 'right_pressed':
            self.direction['right'] = True
        if command == 'left_pressed':
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
        
            
    def collision_check(self, laptop):
        collision = self.overlap(self.position, laptop.position)
        
        # 적의 총알은 캐릭터의 체력 1을 소진시킨다.
        if collision:
            laptop.health -= 1
            if laptop.health == 0:
                laptop.state = 'die'
            self.state = 'hit'

    def overlap(self, bullet_position, laptop_position):
        return laptop_position[0]< bullet_position[2] < laptop_position[2] and laptop_position[0] <bullet_position[0] < laptop_position[2] and laptop_position[1] < bullet_position[3] < laptop_position[3]