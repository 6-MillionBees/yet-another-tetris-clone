# Arden Boettcher
# 2/20/25
# Game Class


import pygame as pg
from buttons import Button
from blocks import *
from random import randint
from grid_class import Grid
from world_class import World
# import particles as part
import misc as m



class Game:
  def __init__(self, grid: Grid, scheme: dict, surface: pg.Surface):
    # Particles
    # self.particles: list[part.Particle] = [] # WIP

    # Speed & lines
    self.level: int = 0
    self.max_lines: int = 10
    self.lines_cleared: int = 0
    self.speed: int = int(1000 / m.FPS * m.SPEEDS[self.level])

    # Line Scoring
    self.combo: int = 0

    # Scores
    self.max_combo: int = 0

# |============================================================|    IMPORTANT    |============================================================|

    self.alive: bool = True # self.alive is the boolian keeping the gameloop going BE CAREFUL WITH THIS ONE

# |===========================================================================================================================================|


    # Misc things
    self.surface: pg.Surface = surface
    self.colorscheme: dict[str, tuple] = scheme[0]


    # World
    self.world: World = World((grid.columns, grid.rows))

    # Blocks
    self.current_block: Block = None
    self.has_held: bool = False
    self.heldblock: Block = None
    self.grid: Grid = grid
    self.score: int = 0
    self.grabbag: list[Block] = [
      o_Block(self.grid, self.world),
      i_Block(self.grid, self.world),
      s_Block(self.grid, self.world),
      z_Block(self.grid, self.world),
      l_Block(self.grid, self.world),
      j_Block(self.grid, self.world),
      t_Block(self.grid, self.world)
    ]
    self.nextblock: Block = None
    self.fastdrop_safety = False

    self.setup()
    self.newblock()

    self.nextblock_rect = pg.Rect(25, 10, 50, 50)
    self.heldblock_rect = pg.Rect(25, 80, 50, 50)




  # This sets up self.nextblock
  def setup(self):
    # Grabs a random block from the grab-bag
    random_block = randint(0, len(self.grabbag) - 1)
    self.nextblock = self.grabbag[random_block]

    # Removes the block from the grab-bag
    del self.grabbag[random_block]



  def movedown(self) -> bool:
    # Check blocks.py for
    boolian = self.current_block.movedown(self.world)
    if not boolian:
      self.update_world()
      self.newblock()
    return boolian





  def newblock(self):
    self.current_block = self.nextblock
    self.current_block.update_rects(self.world)
    # self.define_hoverblock(self.current_block)

    random_block = randint(0, len(self.grabbag) - 1)
    self.nextblock = self.grabbag[random_block]

    del self.grabbag[random_block]

    # Checks if grabbag is empty, if it is then it gets refilled
    if not self.grabbag:
      self.grabbag = [
        o_Block(self.grid, self.world),
        i_Block(self.grid, self.world),
        s_Block(self.grid, self.world),
        z_Block(self.grid, self.world),
        l_Block(self.grid, self.world),
        j_Block(self.grid, self.world),
        t_Block(self.grid, self.world)
      ]

    for cord in self.current_block.cords:
      if not self.world.get_block(cord)[0]:
        continue
      self.alive = False

    self.has_held = False





  def update_world(self):
    num = 0
    for cord in self.current_block.cords:
      self.world.change_block(cord, [self.current_block.rects[num], self.current_block.type])
      num += 1

    cleared_lines = self.world.check_lines(self.grid)
    if not cleared_lines:
      return

    # for line in cleared_lines: # WIP
    #   self.particles.append(part.Line_Clear_Particle(line))

    self.score_lines(len(cleared_lines))



  def draw_blocks(self, surface):
    self.surface = surface

    self.current_block.hover_block.display(self.surface, self.colorscheme)
    self.current_block.display(self.surface, self.colorscheme)





  def draw_world(self, surface):
    self.surface = surface

    for row in self.world.blocks:
      for column in row:
        if column[0] != None:
          pg.draw.rect(self.surface, self.colorscheme[column[1]], column[0])

    score_text = m.nums_font.render(str(self.score), False, m.GREEN)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (500, 400)

    self.surface.blit(score_text, score_text_rect)

    combo_text = m.nums_font.render(str(self.combo), False, m.GREEN)
    combo_text_rect = combo_text.get_rect()
    combo_text_rect.center = (40, 150)

    self.surface.blit(combo_text, combo_text_rect)

    m.outline(self.heldblock_rect, m.BLACK, 2, self.surface)
    pg.draw.rect(self.surface, self.colorscheme["back"], self.heldblock_rect)

    m.outline(self.nextblock_rect, m.BLACK, 2, self.surface)
    pg.draw.rect(self.surface, self.colorscheme["back"], self.nextblock_rect)

    try:
      for block in m.MINI_BLOCKS[self.heldblock.type]:
        temp_block = pg.Rect(block.x, block.y, block.width, block.height)
        temp_block.x += 25
        temp_block.y += 80
        pg.draw.rect(self.surface, self.colorscheme[self.heldblock.type], temp_block)
    except AttributeError:
      pass

    for block in m.MINI_BLOCKS[self.nextblock.type]:
      temp_block = pg.Rect(block.x, block.y, block.width, block.height)
      temp_block.x += 25
      temp_block.y += 10
      pg.draw.rect(self.surface, self.colorscheme[self.nextblock.type], temp_block)







  def hold(self) -> None:
    if self.has_held:
      return
    if self.heldblock:
      temp_hold = self.current_block.reset_pos(self.grid, self.world)
      self.current_block = self.heldblock
      self.current_block.getworld(self.world)
      self.heldblock = temp_hold
      self.current_block.update_rects(self.world)
      self.has_held = True
      return

    self.heldblock = self.current_block.reset_pos(self.grid, self.world)
    self.newblock()
    self.has_held = True




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

    score_text = m.nums_font.render(str(self.score), False, m.GREEN)
    score_rect = score_text.get_rect()
    score_rect.center = (300, 300)

    quit_colors = (self.colorscheme["back"], m.BLACK)

    is_open = True
    while is_open:
      for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
          quit()
        if event.type == pg.MOUSEBUTTONDOWN:
          if quit_rect.collidepoint(event.pos):
            is_open = False
        if event.type == pg.MOUSEMOTION:
          if quit_rect.collidepoint(event.pos):
            quit_colors = (self.colorscheme["highlight"], m.WHITE)
            quit_text = m.small_title_font.render("Quit", False, m.WHITE)
          else:
            quit_colors = (self.colorscheme["back"], m.BLACK)
            quit_text = m.small_title_font.render("Quit", False, m.DEEP_BLUE)

      self.surface.fill(self.colorscheme["back"])

      m.outline(quit_rect, quit_colors[1], 2, self.surface)
      pg.draw.rect(self.surface, quit_colors[0], quit_rect)
      self.surface.blit(score_text, score_rect)
      self.surface.blit(over_text, over_rect)
      self.surface.blit(quit_text, quit_text_rect)

      pg.display.update()
      clock.tick(60)

    self.alive = False



  def score_lines(self, lines):
    self.lines_cleared += lines

    if lines == 4:
      self.score += 1200 * (self.level + 1) + (self.combo * 100 * self.level + 1)
      self.combo += 1
      if self.combo > self.max_combo:
        self.max_combo = self.combo


    elif lines == 3:
      self.score += 300 * (self.level + 1)
      if self.combo > self.max_combo:
        self.max_combo = self.combo
      self.combo = 0

    elif lines == 2:
      self.score += 100 * (self.level + 1)
      if self.combo > self.max_combo:
        self.max_combo = self.combo
      self.combo = 0


    elif lines == 1:
      self.score += 40 * (self.level + 1)
      if self.combo > self.max_combo:
        self.max_combo = self.combo
      self.combo = 0


    if self.lines_cleared >= self.max_lines:
      self.level_up()






  def fastdrop(self):
    self.current_block.fastdrop(self.world)
    self.update_world()
    self.newblock()
    self.score += 5 * self.level
    self.fastdrop_safety = True


  def level_up(self):
    self.level += 1
    try:
      self.colorscheme = m.colors[self.level]
    except IndexError:
      self.colorscheme = m.colors[-1]
    self.max_lines += 10
    try:
      self.speed = int(1000 / m.FPS * m.SPEEDS[self.level])
    except IndexError:
      self.speed = int(1000 / m.FPS * m.SPEEDS[-1])

    print("level up: {}".format(self.speed))

    # self.particles.append(part.Level_Up()) # WIP




  def player_events(self, event: pg.event.Event):
    # if event.type == m.PARTICLE_UPDATE: # WIP
    #   for particle in self.particles:
    #     particle.update()


    if event.type == m.MOVEDOWN:
      if self.fastdrop_safety:
        self.fastdrop_safety = False
        pg.time.set_timer(m.MOVEDOWN, int(self.speed * 0.5), 1)
        return

      self.movedown()
      self.current_block.update_rects(self.world)

      if not self.alive:
        self.game_over()
        return

      # Checks if shift is pressed
      if pg.key.get_pressed()[pg.K_RSHIFT]:
        # It's halving the amount of time it takes to move down
        # (this might cause movedown events to happen too fast) <- possible breaking point
        # If the speed goes faster than a frame then the pieces could move twice per frame (causing things to happen)
        if self.speed < 100:
          pg.time.set_timer(m.MOVEDOWN, int(self.speed / 2), 1)
        else:
          pg.time.set_timer(m.MOVEDOWN, 100, 1)
      else:
        pg.time.set_timer(m.MOVEDOWN, self.speed, 1)


    if event.type == pg.KEYDOWN:

      # Block Movement
      if event.key == pg.K_RIGHT:
        self.current_block.right(self.world)
      if event.key == pg.K_LEFT:
        self.current_block.left(self.world)

      # Block Rotation
      if event.key == pg.K_UP:
        self.current_block.l_rotate(self.world)
      if event.key == pg.K_DOWN:
        self.current_block.r_rotate(self.world)

      # Harddrop
      if event.key == pg.K_SPACE:
        self.fastdrop()
      if event.key == pg.K_RETURN:
        self.hold()

      # Debug Menu
      if event.key == pg.K_d:
        self.alive = self.debug_menu()





  def debug_menu(self):

    get_player_button = Button(Rect(0, 0, 200, 100), "Player", m.base_button, m.base_button_hover, m.nums_font)
    get_player_button.center((300, 300))

    level_up_button = Button(Rect(0, 0, 50, 50), "+", m.base_button, m.base_button_hover, m.nums_font)
    level_up_button.center((550, 475))

    level_down_button = Button(Rect(0, 0, 50, 50), "-", m.base_button, m.base_button_hover, m.nums_font)
    level_down_button.center((550, 550))

    temp_clock = pg.time.Clock()

    running = True

    while running:

      for event in pg.event.get():
        if event.type == m.MOVEDOWN:
          pg.time.set_timer(m.MOVEDOWN, self.speed, 1)

        if event.type == pg.QUIT:
          return False

        if event.type == pg.KEYDOWN:
          if event.key == pg.K_ESCAPE:
            return True

        if event.type == pg.MOUSEBUTTONDOWN:
          if get_player_button.collidepoint(event.pos):
            for item in self.__dict__.items():
              print(item)
          if level_up_button.collidepoint(event.pos):
            self.level_up()

          if level_down_button.collidepoint(event.pos):
            self.level -= 2
            self.level_up()

        if event.type == pg.MOUSEMOTION:
          get_player_button.hover(event.pos)
          level_down_button.hover(event.pos)
          level_up_button.hover(event.pos)

      self.surface.fill(m.DARK_BLUE)

      get_player_button.display(self.surface)
      level_down_button.display(self.surface)
      level_up_button.display(self.surface)

      pg.display.flip()

      temp_clock.tick(m.FPS)

    return True