import pygame as pg
pg.init()

title_font = pg.font.Font("fonts/highway-encounter.ttf", 50)
small_title_font = pg.font.Font("fonts/highway-encounter.ttf", 25)
nums_font = pg.font.Font("fonts/ragnagard.ttf", 20)

GREY = (120, 120, 120)
BLACK = (0, 0, 0)
YELLOW = (254, 248, 76)
BLUE = (81, 225, 252)
RED = (233, 61, 30)
GREEN = (121, 174, 61)
ORANGE = (121, 174, 61)
DEEP_BLUE = (39, 85, 214)
PINK = (241, 110, 185)

colors = {
  "o": YELLOW,
  "i": BLUE,
  "s": RED,
  "z": GREEN,
  "l": ORANGE,
  "j": DEEP_BLUE,
  "t": PINK
}