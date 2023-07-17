import pygame
import sys
import os
import math
from ultis import scale_image, blit_rotate_center

WHITE = (255, 255, 255)
FPS = 60


def draw(win, images,player_car):
    for img, pos in images:
        win.blit(img, pos)
    player_car.draw(win)
    pygame.display.update()


GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.6)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.6)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()

images = [(GRASS, (0, 0)), (TRACK, (0, 0))]


class AbstractCar:

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 90
        self.x,self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img,(self.x,self.y),self.angle)

    def move_forward(self):
        self.vel = min(self.vel+self.acceleration,self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal



class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180,200)


player_car = PlayerCar(4,4)

def main():
    pygame.display.set_caption("Pygame")
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_car.rotate(left=True)
        if keys[pygame.K_d]:
            player_car.rotate(right=True)
        if keys[pygame.K_w]:
            player_car.move_forward()
        draw(WIN, images,player_car)
        clock.tick(FPS)



if __name__ == '__main__':
    main()
