import pygame as pg
from blocks import *
from random import randint
from grid_class import Grid
from world_class import World
import misc as m

mini_blocks: dict[str, list[pg.Rect]] = {
  "": [],
  "o": [pg.Rect(10, 10 , 30, 30)],
  "i": [pg.Rect(20, 5, 10, 40)],
  "s": [
    pg.Rect(6, 24, 12, 12),
    pg.Rect(18, 24, 12, 12),
    pg.Rect(18, 12, 12, 12),
    pg.Rect(30, 12, 12, 12)
    ],
  "z": [
    pg.Rect(6, 12, 12, 12),
    pg.Rect(18, 12, 12, 12),
    pg.Rect(18, 24, 12, 12),
    pg.Rect(30, 24, 12, 12)
  ],
  "l": [
    pg.Rect(13, 7, 12, 36),
    pg.Rect(25, 31, 12, 12)
  ],
  "j": [
    pg.Rect(25, 7, 12, 36),
    pg.Rect(13, 31, 12, 12)
  ],
  "t": [
    pg.Rect(6, 12, 36, 12),
    pg.Rect(18, 24, 12, 12)
  ]
}


class Player:
  def __init__(self, grid: Grid, scheme: dict, surface: pg.Surface):
    self.current_block: Block = None
    self.isheld = False
    self.heldblock: Block = None
    self.grid: Grid = grid
    self.score: int = 0
    self.rects: list[pg.Rect] = []
    self.alive: bool = True
    self.surface: pg.Surface = surface

    self.world = World((grid.columns, grid.rows))
    self.colorscheme = scheme

    self.grabbag: list[Block] = [o_Block(), i_Block(), s_Block(), z_Block(), l_Block(), j_Block(), t_Block()]
    self.nextblock = None
    self.setup()
    self.newblock()

    self.nextblock_rect = pg.Rect(25, 10, 50, 50)
    self.heldblock_rect = pg.Rect(25, 80, 50, 50)

  def setup(self):
    random_block = randint(0, len(self.grabbag) - 1)
    self.nextblock = self.grabbag[random_block]

    del self.grabbag[random_block]


  def newblock(self):
    self.current_block = self.nextblock

    random_block = randint(0, len(self.grabbag) - 1)
    self.nextblock = self.grabbag[random_block]

    del self.grabbag[random_block]

    if not self.grabbag:
      self.grabbag = [o_Block(), i_Block(), s_Block(), z_Block(), l_Block(), j_Block(), t_Block()]

    self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + (cordnate[1] - 2) * self.grid.sq_size[1] + 1), self.grid.sq_size) for cordnate in self.current_block.cords]
    for cord in self.current_block.cords:
      if not self.world.get_block(cord)[0]:
        continue
      self.alive = False

    self.isheld = False


  def movedown(self) -> bool:
    self.current_block.cords = [(cordnate[0], cordnate[1] + 1) for cordnate in self.current_block.cords]
    self.current_block.center[1] += 1
    self.update_rects()

    for cord in self.current_block.cords:
      try:
        if not self.world.get_block(cord)[0]:
          continue
      except IndexError:
        pass
      self.current_block.cords = [(cordnate[0], cordnate[1] - 1) for cordnate in self.current_block.cords]
      self.current_block.center[1] -= 1
      self.update_rects()

      self.update_world()
      self.newblock()
      return False
    return True


  def update_world(self):
    num = 0
    for cord in self.current_block.cords:
      self.world.change_block(cord, [self.rects[num], self.current_block.type])
      num += 1

    cleared_lines = self.world.check_lines(self.grid)
    if cleared_lines == 0:
      return
    self.score_lines(cleared_lines)


  def draw_blocks(self):
    for rect in self.rects:
      pg.draw.rect(self.surface, self.colorscheme[self.current_block.type], rect)


  def draw_world(self):
    for row in self.world.blocks:
      for column in row:
        if column[0] != None:
          pg.draw.rect(self.surface, self.colorscheme[column[1]], column[0])

    self.surface.blit(m.nums_font.render(str(self.score), False, m.GREEN), (500, 400))

    m.outline(self.heldblock_rect, m.BLACK, 2, self.surface)
    pg.draw.rect(self.surface, m.GREY, self.heldblock_rect)

    m.outline(self.nextblock_rect, m.BLACK, 2, self.surface)
    pg.draw.rect(self.surface, m.GREY, self.nextblock_rect)

    try:
      for block in mini_blocks[self.heldblock.type]:
        temp_block = pg.Rect(block.x, block.y, block.width, block.height)
        temp_block.x += 25
        temp_block.y += 80
        pg.draw.rect(self.surface, self.colorscheme[self.heldblock.type], temp_block)
    except AttributeError:
      pass

    for block in mini_blocks[self.nextblock.type]:
      temp_block = pg.Rect(block.x, block.y, block.width, block.height)
      temp_block.x += 25
      temp_block.y += 10
      pg.draw.rect(self.surface, self.colorscheme[self.nextblock.type], temp_block)




  def right(self):
    self.current_block.cords = [[cordnate[0] + 1, cordnate[1]] for cordnate in self.current_block.cords]
    self.current_block.center[0] += 1

    for cord in self.current_block.cords:
      try:
        if not self.world.get_block(cord)[0]:
          continue
      except IndexError:
        pass
      self.current_block.cords = [[cordnate[0] - 1, cordnate[1]] for cordnate in self.current_block.cords]
      self.current_block.center[0] -= 1

      break

    self.update_rects()


  def left(self):
    self.current_block.cords = [[cordnate[0] - 1, cordnate[1]] for cordnate in self.current_block.cords]
    self.current_block.center[0] -= 1

    for cord in self.current_block.cords:
      try:
        if cord[0] < 0:
          raise IndexError
        if not self.world.get_block(cord)[0]:
          continue
      except IndexError:
        pass
      self.current_block.cords = [[cordnate[0] + 1, cordnate[1]] for cordnate in self.current_block.cords]
      self.current_block.center[0] += 1

      break

    self.update_rects()

  def hold(self) -> None:
    if self.isheld:
      return
    if self.heldblock:
      hold = self.current_block.reset_pos()
      self.current_block = self.heldblock
      self.heldblock = hold
      self.update_rects()
      self.isheld = True
      return

    self.heldblock = self.current_block.reset_pos()
    self.newblock()
    self.isheld = True

    self.update_rects()


  def game_over(self):
    clock = pg.time.Clock()

    over_text = m.big_nums_font.render("Game Over", False, m.DEEP_BLUE)
    over_rect = over_text.get_rect()
    over_rect.center = (300, 200)

    quit_text = m.small_title_font.render("Quit", False, m.DEEP_BLUE)
    quit_text_rect = quit_text.get_rect()

    quit_rect = pg.Rect(0, 0, 200, 100)
    quit_rect.center = (300, 475)
    quit_text_rect.center = quit_rect.center

    self.surface.fill(m.T_GREY)
    is_open = True
    while is_open:
      for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
          quit()
        if event.type == pg.MOUSEBUTTONDOWN:
          if quit_rect.collidepoint(event.pos):
            is_open = False

      m.outline(quit_rect, m.BLACK, 2, self.surface)
      pg.draw.rect(self.surface, m.GREY, quit_rect)
      self.surface.blit(over_text, over_rect)
      self.surface.blit(quit_text, quit_text_rect)

      pg.display.update()
      clock.tick(60)



  def score_lines(self, lines):
    num_lines = lines
    self.score += num_lines**2

  def r_rotate(self):
    self.current_block.r_rotate(self.world)
    self.update_rects()

  def l_rotate(self):
    self.current_block.l_rotate(self.world)
    self.update_rects()

  def update_rects(self):
    self.rects = [pg.Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + (cordnate[1] - 2) * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.current_block.cords]

  def fastdrop(self):
    going = True
    while going:
      going = self.movedown()
