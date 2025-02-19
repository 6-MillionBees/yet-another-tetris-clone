import pygame as pg

class Grid:
  def __init__(self, columns:int, rows:int, square_size:tuple, pos:tuple = (0, 0), hori_color: tuple = (0, 0, 0),vert_color: tuple = (0, 0, 0)):
    self.columns = columns
    self.rows = rows
    self.sq_size = square_size
    self.pos = pos
    self.x = pos[0]
    self.y = pos[1]

    self.color = (hori_color, vert_color)
    self.size = (self.columns * self.sq_size[0], self.rows * self.sq_size[1])



  def display(self, surface):
    for x in range(self.rows + 1):
      pg.draw.line(surface, self.color[0], (self.x, self.y + self.sq_size[1] * x), (self.x + self.size[0], self.y + self.sq_size[1] * x), 2)
    for x in range(self.columns + 1):
      pg.draw.line(surface, self.color[0], (self.x + self.sq_size[0] * x, self.y), (self.x + self.sq_size[0] * x, self.y + self.size[1]), 2)