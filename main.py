# Arden Boettcher
# 1/28/25
# Tetris

import pygame as pg
import grid_class
import player_class
import misc as m

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600))

MOVEDOWN = pg.event.custom_type()





def outline(rect, color, weight):
  outrect = pg.Rect(rect.x - weight, rect.y - weight, rect.width + weight * 2, rect.height + weight * 2)
  pg.draw.rect(screen, color, outrect)
  return outrect


def pause(player: player_class.Player):
  get_blocks_rect = pg.Rect(250, 400, 100, 50)

  is_open = True
  while is_open:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        quit()
      elif event.type == pg.MOUSEBUTTONDOWN:
        if get_blocks_rect.collidepoint(event.pos):
          for row in player.world.blocks:
            print(row)
          continue
        is_open = False

    screen.blit(m.nums_font.render("Paused", False, m.BLACK), (250, 250))

    outline(get_blocks_rect, m.BLACK, 2)
    pg.draw.rect(screen, m.GREY, get_blocks_rect)

    pg.display.update()


def game_loop():
  grid = grid_class.Grid(10, 20, (30, 30), (100, -2))
  player = player_class.Player(grid, m.colors)

  pg.time.set_timer(MOVEDOWN, 100)

  pause_rect = pg.Rect(550, 0, 50, 50)

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
      if event.type == pg.MOUSEBUTTONDOWN:
        if pause_rect.collidepoint(event.pos):
          pause(player)
      if event.type == pg.K_UP:
        player.r_rotate()


    screen.fill(m.GREY)
    player.draw_world(screen)
    grid.display(screen)
    player.draw_blocks(screen)
    outline(pause_rect, m.BLACK, 2)
    pg.draw.rect(screen, m.GREY, pause_rect)

    pg.display.flip()


def main():
  running = True

  start_text = m.small_title_font.render("start", False, m.DEEP_BLUE)
  start_text_rect = start_text.get_rect()
  start_button = pg.Rect(0, 0, 200, 50)
  start_button.center = (300, 325)
  start_text_rect.center = (300, 325)

  title = m.title_font.render("Tetris", False, m.DEEP_BLUE)
  title_rect: pg.Rect = title.get_rect()
  title_rect.center = (300, 150)

  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False
        break
      if event.type == pg.MOUSEBUTTONDOWN:
        game_loop()

    screen.fill(m.GREY)
    screen.blit(title, title_rect)

    outline(start_button, m.BLACK, 2)
    pg.draw.rect(screen, m.GREY, start_button)
    screen.blit(start_text, start_text_rect)

    pg.display.flip()

    clock.tick(60)


if __name__ == "__main__":
  main()