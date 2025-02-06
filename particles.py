# Arden Boettcher

import pygame as pg
from grid_class import Grid


class Particle:
  def __init__(self, pos: list, velocity: list, size: list):
    self.pos = pos
    self.velocity = velocity

  def update(self):
    pass


class words_Part(Particle):
  def __init__(self, pos: list, velocity: list, changes: dict, text: str, font: pg.font.Font):
    Particle.__init__(pos, velocity, changes)



class rect_Part(Particle):
  def __init__(self, pos: list, velocity: list, size: list, changes: dict):
    Particle.__init__(pos, velocity, changes, size)
    self.changes = changes
    self.rect = pg.Rect(pos, size)

  def update(self):
    pass


class Line_Clear_Effect(Particle):
  def __init__(self, line: int, grid: Grid):
    self.line = line
    self.frame = 0
    self.max_frames = 60
    self.rect = pg.Rect((grid.pos[0], grid.pos[1] + grid.sq_size * line), grid.size)

  def update(self):
    self.frame += 1
    self.rect.width *= 1.5

# class Level_Up(Particle):
#   def __init__(self, ):

#   def update(self):
