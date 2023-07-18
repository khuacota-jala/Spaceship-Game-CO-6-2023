import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY

class BulletEnemy(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 20


    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)

    def update(self, player):
        if self.rect.top < 0:
            self.is_visible = False
            self.is_alive = False
        self.rect.y += self.SPEED
        super().update(player)
