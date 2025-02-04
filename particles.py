# Arden Boettcher

import pygame as pg


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


class line_clear_effect(Particle):
  def __init__(self, lines: list[int]):
    self.lines = lines
