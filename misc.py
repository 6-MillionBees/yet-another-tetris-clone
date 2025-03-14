import pygame as pg
pg.init()

FPS = 60

title_font = pg.font.Font("fonts/highway-encounter.ttf", 50)
small_title_font = pg.font.Font("fonts/highway-encounter.ttf", 25)
nums_font = pg.font.Font("fonts/ragnagard.ttf", 20)
big_nums_font = pg.font.Font("fonts/ragnagard.ttf", 40)

T_WHITE = (255, 255, 255, 128)
WHITE = (255, 255, 255)
T_GREY = (120, 120, 120, 50)
GREY = (120, 120, 120)
BLACK = (0, 0, 0)

RED = (233, 61, 30)

ORANGE = (252, 123, 3)

YELLOW = (254, 248, 76)

LIME = (168, 214, 56)
GREEN = (100, 174, 61)
LIGHT_GREEN = (143, 247, 109)
DARK_GREEN = (67, 122, 0)

BLUE = (81, 225, 252)
DEEP_BLUE = (39, 85, 214)
DARK_BLUE = (0, 22, 131)

LIGHT_PINK = (248, 175, 245)
PALE_PINK = (250, 120, 249)
PINK = (241, 110, 185)
BRIGHT_PURPLE = (217, 0, 202)

SPEEDS = [
  48, 43, 38, 33, 28, 23, 18, 13,
  8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3,
  2, 2, 2, 1
]

MAIN_COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PINK]

base_button = {
  "main": DARK_BLUE,
  "out": DEEP_BLUE,
  "text": DEEP_BLUE
}

base_button_hover = {
  "main": DEEP_BLUE,
  "out": WHITE,
  "text": WHITE
}


colors = [
  {
    "o": YELLOW,
    "i": BLUE,
    "s": RED,
    "z": GREEN,
    "l": ORANGE,
    "j": DEEP_BLUE,
    "t": PINK,
    "h": T_WHITE,
    "main": BLUE,
    "back": DARK_BLUE,
    "highlight": DEEP_BLUE
  }
  # {
  #   "o": LIGHT_GREEN,
  #   "i": LIGHT_GREEN,
  #   "s": LIME,
  #   "z": GREEN,
  #   "l": LIME,
  #   "j": GREEN,
  #   "t": LIGHT_GREEN,
  #   "h": T_WHITE,
  #   "main": GREEN,
  #   "back": DARK_GREEN
  # }
]

def outline(rect: pg.Rect, color: tuple[int], weight: int, surface: pg.Surface):
  outrect = pg.Rect(rect.x - weight, rect.y - weight, rect.width + weight * 2, rect.height + weight * 2)
  pg.draw.rect(surface, color, outrect)
  return outrect


# Centers text
def center_text(text: pg.Surface, rect: pg.Rect, offsets: tuple[int, int] = (0, 0)) -> pg.Rect:
  text_rect = text.get_rect()
  text_rect.center = (rect.center[0] + offsets[0], rect.center[1] + offsets[1])

  return text_rect

# def shadow_text(text: pg.Surface, direction, distance):

MINI_BLOCKS: dict[str, list[pg.Rect]] = {
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

# Events

MOVEDOWN = pg.event.custom_type()
PARTICLE_UPDATE = pg.event.custom_type()