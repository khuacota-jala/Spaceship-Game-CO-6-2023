import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGTH, BULLET_ENEMY_TYPE

class Enemy:
    Y_POS = 0
    SPEED_X = 5
    SPEED_Y = 2
    MOV_X = [LEFT, RIGTH]
    INTERVAL = 100
    SHOOTING_TIME = 30

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(image.get_width(), SCREEN_WIDTH - image.get_width())
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.index = 0
        self.shooting_time = 0
        self.is_visible = True

    def update(self, bullet_handler):
        self.index += 1
        self.shooting_time += 1
        self.move()
        self.shoot(bullet_handler)
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_visible = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x <= 0:
                self.mov_x = RIGTH
                self.index = 0
        else:
            self.rect.x += self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = LEFT
                self.index = 0

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)
