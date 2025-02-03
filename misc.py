import pygame as pg
pg.init()

title_font = pg.font.Font("fonts/highway-encounter.ttf", 50)
small_title_font = pg.font.Font("fonts/highway-encounter.ttf", 25)
nums_font = pg.font.Font("fonts/ragnagard.ttf", 20)
big_nums_font = pg.font.Font("fonts/ragnagard.ttf", 40)

GREY = (120, 120, 120)
T_GREY = (120, 120, 120, 50)
BLACK = (0, 0, 0)
YELLOW = (254, 248, 76)
BLUE = (81, 225, 252)
RED = (233, 61, 30)
GREEN = (121, 174, 61)
ORANGE = (252, 123, 3)
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

def outline(rect: pg.Rect, color: tuple[int], weight: int, surface: pg.Surface):
  outrect = pg.Rect(rect.x - weight, rect.y - weight, rect.width + weight * 2, rect.height + weight * 2)
  pg.draw.rect(surface, color, outrect)
  return outrect