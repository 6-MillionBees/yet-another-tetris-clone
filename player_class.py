import pygame as pg
from blocks import *
from random import randint
from grid_class import Grid
from world_class import World

class Player:
  def __init__(self, grid: Grid, scheme):
    self.current_block: Block = None
    self.heldblock = None
    self.grid = grid
    self.score = 0
    self.rects = []

    self.world = World((grid.columns, grid.rows))
    self.colorscheme = scheme

    self.grabbag = [o_Block(), i_Block()] #, s_Block(), z_Block(), l_Block(), j_Block(), t_Block()]
    self.newblock()

  def newblock(self):
    x = randint(0, len(self.grabbag) - 1)
    self.current_block = self.grabbag[x]

    del self.grabbag[x]

    if not self.grabbag:
      self.grabbag = [o_Block(), i_Block()] #, s_Block(), z_Block(), l_Block(), j_Block(), t_Block()]

    self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0], self.grid.pos[1] + cordnate[1] * self.grid.sq_size[1]), self.grid.sq_size) for cordnate in self.current_block.cords]
    for cord in self.current_block.cords:
      if not self.world.get_block(cord)[0]:
        continue
      self.game_over()


  def movedown(self):
    self.current_block.cords = [(cordnate[0], cordnate[1] + 1) for cordnate in self.current_block.cords]
    self.current_block.center
    self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + cordnate[1] * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.current_block.cords]

    for cord in self.current_block.cords:
      try:
        if not self.world.get_block(cord)[0]:
          continue
      except IndexError:
        pass
      self.current_block.cords = [(cordnate[0], cordnate[1] - 1) for cordnate in self.current_block.cords]
      self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + cordnate[1] * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.current_block.cords]

      self.update_world()
      self.newblock()
      break


  def update_world(self):
    num = 0
    for cord in self.current_block.cords:
      self.world.change_block(cord, [self.rects[num], self.current_block.type])
      num += 1

    cleared_lines = self.world.check_lines(self.grid)
    if cleared_lines == 0:
      return
    self.score_lines(cleared_lines)


  def draw_blocks(self, surface):
    for rect in self.rects:
      pg.draw.rect(surface, self.colorscheme[self.current_block.type], rect)


  def draw_world(self, surface):
    for row in self.world.blocks:
      for column in row:
        if column[0] != None:
          pg.draw.rect(surface, self.colorscheme[column[1]], column[0])





  def right(self):
    self.current_block.cords = [(cordnate[0] + 1, cordnate[1]) for cordnate in self.current_block.cords]
    self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + cordnate[1] * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.current_block.cords]

    for cord in self.current_block.cords:
      try:
        if not self.world.get_block(cord)[0]:
          continue
      except IndexError:
        pass
      self.current_block.cords = [(cordnate[0] - 1, cordnate[1]) for cordnate in self.current_block.cords]
      self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + cordnate[1] * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.current_block.cords]

      break

  def left(self):
    self.current_block.cords = [(cordnate[0] - 1, cordnate[1]) for cordnate in self.current_block.cords]
    self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + cordnate[1] * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.current_block.cords]

    for cord in self.current_block.cords:
      try:
        if cord[0] < 0:
          raise IndexError
        if not self.world.get_block(cord)[0]:
          continue
      except IndexError:
        pass
      self.current_block.cords = [(cordnate[0] + 1, cordnate[1]) for cordnate in self.current_block.cords]
      self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + cordnate[1] * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.current_block.cords]

      break



  # def game_over(self):
  #   is_open = True
  #   while is_open:
