# Arden Boettcher
# 1/28/25
# Tetris

import pygame as pg
import grid_class
import player_class
import misc as m

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600), pg.FULLSCREEN)
pg.display.set_caption("Tetris")

MOVEDOWN = pg.event.custom_type()
PARTICLE_UPDATE = pg.event.custom_type()



def pause(player: player_class.Player):
  unpause_rect = pg.Rect(200, 400, 200, 50)
  pause_text = m.nums_font.render("Paused", False, m.BLACK)
  pause_text_rect = pause_text.get_rect()
  pause_text_rect.center = (300, 250)
  pg.time.set_timer(MOVEDOWN, 100)

  is_open = True
  while is_open:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        quit()
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          is_open = False
      elif event.type == pg.MOUSEBUTTONDOWN:
        if unpause_rect.collidepoint(event.pos):
          is_open = False

    screen.fill(m.GREY)

    screen.blit(pause_text, pause_text_rect)

    m.outline(unpause_rect, m.BLACK, 2, screen)
    pg.draw.rect(screen, m.GREY, unpause_rect)

    pg.display.update()
    clock.tick(m.FPS)


def game_loop():
  grid = grid_class.Grid(10, 20, (30, 30), (100, -2))
  player = player_class.Player(grid, m.colors, screen)

  pg.time.set_timer(MOVEDOWN, player.speed, 1)
  pg.time.set_timer(PARTICLE_UPDATE, int(1000 / m.FPS))

  pause_rect = pg.Rect(550, 0, 50, 50)

  alive: bool = True
  while alive:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        quit()
      if event.type == PARTICLE_UPDATE:
        for particle in player.particles:
          particle.update()
      if event.type == MOVEDOWN:
        player.movedown()
        if not player.alive:
          player.game_over()
          alive = False

        if pg.key.get_pressed()[pg.K_RSHIFT]:
          pg.time.set_timer(MOVEDOWN, 100, 1)
        else:
          pg.time.set_timer(MOVEDOWN, player.speed, 1)

      if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          pause(player)
        if event.key == pg.K_RIGHT:
          player.right()
        if event.key == pg.K_LEFT:
          player.left()
        if event.key == pg.K_UP:
          player.l_rotate()
        if event.key == pg.K_DOWN:
          player.r_rotate()
        if event.key == pg.K_SPACE:
          player.fastdrop()
        if event.key == pg.K_RETURN:
          player.hold()
      if event.type == pg.MOUSEBUTTONDOWN:
        if pause_rect.collidepoint(event.pos):
          pause(player)

    # Background
    screen.fill(m.GREY)

    # Draw grid
    grid.display(screen)

    # Draw game
    player.draw_world()
    player.draw_blocks()

    # Pause rects <3
    m.outline(pause_rect, m.BLACK, 2, screen)
    pg.draw.rect(screen, m.GREY, pause_rect)

    # Draw particles
    # for particle in player.particles:
    #   particle.display()

    pg.display.flip()

    clock.tick(m.FPS)


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

    m.outline(start_button, m.BLACK, 2, screen)
    pg.draw.rect(screen, m.GREY, start_button)
    screen.blit(start_text, start_text_rect)

    pg.display.flip()

    clock.tick(m.FPS)


if __name__ == "__main__":
  main()
  pg.quit()