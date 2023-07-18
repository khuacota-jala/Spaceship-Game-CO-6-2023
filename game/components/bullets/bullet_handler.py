from game.utils.constants import BULLET_ENEMY_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player):
        for bullet in self.bullets:
            if type(bullet) == BulletEnemy:
                bullet.update(player)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
    
    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
