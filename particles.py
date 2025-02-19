# Arden Boettcher
# 2/13/25
# Partcles

import pygame as pg
import misc as m


class Particle(pg.sprite.Sprite):
  def __init__(self, groups: pg.sprite.Group, pos: list, color: tuple, direction: pg.math.Vector2, speed: int):
    super().__init__(groups)
    self.pos: tuple = pos
    self.color = color
    self.direction = direction
    self.speed = speed

    self.create_surf()


  def create_surf(self):
    self.image = pg.Surface((4, 4)).convert_alpha()
    self.image.set_colorkey(m.BLACK)
    pg.draw.circle(self.image, self.color, (2, 2), 2)

    # self.rect = self.image.get_rect(center=self.pos)


# class Clear_Line_Part(pg.sprite.Sprite):
#   def __init__(self, groups: pg.sprite.Group, pos: int, ):