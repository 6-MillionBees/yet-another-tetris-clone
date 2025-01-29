import pygame as pg

class Grid:
  def __init__(self, columns:int, rows:int, square_size:tuple, pos:tuple = (0, 0), hori_color: tuple = (0, 0, 0),vert_color: tuple = (0, 0, 0)):
    self.columns = columns
    self.rows = rows
    self.sq_size = square_size
    self.pos = pos

    self.color = (hori_color, vert_color)
    self.size = (self.columns * self.sq_size[0], self.rows * self.sq_size[1])

    self.vertlines = [pg.Rect(pos[0] + square_size[0] * x, pos[1], 2, self.size[1] + 1) for x in range(columns)]
    self.vertlines.append(pg.Rect(pos[0] + square_size[0] * columns + 1, pos[1], 2, self.size[1] + 1))

    self.horilines = [pg.Rect(pos[0], pos[1] + square_size[1] * x, self.size[0] + 1, 2) for x in range(rows)]
    self.horilines.append(pg.Rect(pos[0], pos[1] + square_size[1] * rows + 1, self.size[0] + 1, 2))


  def display(self, surface):
    for rect in self.vertlines:
      pg.draw.rect(surface, self.color[0], rect)
    for rect in self.horilines:
      pg.draw.rect(surface, self.color[1], rect)