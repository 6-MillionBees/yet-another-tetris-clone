# Arden Boettcher
# 1/28/25
# Tetris

import pygame as pg
import grid_class
import player_class

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600))

MOVEDOWN = pg.event.custom_type()

title_font = pg.font.Font("fonts/highway-encounter.ttf", 50)
small_title_font = pg.font.Font("fonts/highway-encounter.ttf", 25)
nums_font = pg.font.Font("fonts/ragnagard.ttf", 50)

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

def outline(rect, color, weight):
  outrect = pg.Rect(rect.x - weight, rect.y - weight, rect.width + weight * 2, rect.height + weight * 2)
  pg.draw.rect(screen, color, outrect)
  return outrect



def game_loop():
  grid = grid_class.Grid(10, 20, (30, 30), (100, -2))
  player = player_class.Player(grid, colors)

  pg.time.set_timer(MOVEDOWN, 200)

  alive = True
  while alive:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        quit()
      if event.type == MOVEDOWN:
        player.movedown()
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
          player.right()
        if event.key == pg.K_LEFT:
          player.left()


    screen.fill(GREY)
    player.draw_world(screen)
    grid.display(screen)
    player.draw_blocks(screen)

    pg.display.flip()


def main():
  running = True

  start_text = small_title_font.render("start", False, DEEP_BLUE)
  start_text_rect = start_text.get_rect()
  start_button = pg.Rect(0, 0, 200, 50)
  start_button.center = (300, 325)
  start_text_rect.center = (300, 325)

  title = title_font.render("Tetris", False, DEEP_BLUE)
  title_rect = title.get_rect()
  title_rect.center = (300, 150)

  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False
        break
      if event.type == pg.MOUSEBUTTONDOWN:
        game_loop()

    screen.fill(GREY)
    screen.blit(title, title_rect)

    outline(start_button, BLACK, 2)
    pg.draw.rect(screen, GREY, start_button)
    screen.blit(start_text, start_text_rect)

    pg.display.flip()

    clock.tick(60)


if __name__ == "__main__":
  main()