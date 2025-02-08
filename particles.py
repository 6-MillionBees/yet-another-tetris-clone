# Arden Boettcher

import pygame as pg
from grid_class import Grid
import misc as m


class Particle(pg.sprite.Sprite):
  def __init__(self, groups, pos, color, direction, speed):
    super().__init__(groups)
    self.pos = pos
    self.color = color
    self.direction = direction
    self.speed = speed

    self.image = pg.Surface((4, 4)).convert_alpha()
    self.image.set_colorkey(m.BLACK)
    pg.draw.circle(self.image, self.color, (2, 2), 2)