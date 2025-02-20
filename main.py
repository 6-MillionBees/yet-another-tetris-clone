# Arden Boettcher
# 1/28/25
# Tetris

import pygame as pg
import grid_class
import game_class
import misc as m

from buttons import Button

pg.init()


clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600))
pg.display.set_caption("Tetris")



def pause(player: game_class.Game):
  pause_text = m.nums_font.render("Paused", False, m.DEEP_BLUE)

  unpause_button = Button(pg.Rect(200, 325, 200, 50), "Unpause", m.base_button, m.base_button_hover, m.nums_font)
  quit_button = Button(pg.Rect(200, 400, 200, 50), "Quit", m.base_button, m.base_button_hover, m.nums_font)

  pause_text_rect = pause_text.get_rect()
  pause_text_rect.center = (300, 200)

  pg.time.set_timer(m.MOVEDOWN, 100)

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
        if unpause_button.collidepoint(event.pos):
          is_open = False
        elif quit_button.collidepoint(event.pos):
          pg.quit()
          quit()
      elif event.type == pg.MOUSEMOTION:
        unpause_button.hover(event.pos)
        quit_button.hover(event.pos)

    screen.fill(player.colorscheme["back"])

    screen.blit(pause_text, pause_text_rect)

    unpause_button.display(screen)
    quit_button.display(screen)


    pg.display.update()
    clock.tick(m.FPS)





def game_loop():
  grid = grid_class.Grid(10, 20, (30, 30), (100, -2))
  game = game_class.Game(grid, m.colors, screen)

  pg.time.set_timer(m.MOVEDOWN, game.speed, 1)
  pg.time.set_timer(m.PARTICLE_UPDATE, int(1000 / m.FPS))

  pause_rect = pg.Rect(550, 0, 50, 50)

  while game.alive:

    # Event Handling
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        quit()

      # Handles the player events (most of the events)
      # See player_class.py for more info
      game.player_events(event)

      if event.type == pg.MOUSEBUTTONDOWN:
        if pause_rect.collidepoint(event.pos):
          pause(game)

      if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
          pause(game)

    # Background
    screen.fill(game.colorscheme["back"])

    # Draw grid
    grid.display(screen)

    # Draw game
    game.draw_world()
    game.draw_blocks()

    # Pause rects <3
    m.outline(pause_rect, m.BLACK, 2, screen)
    pg.draw.rect(screen, game.colorscheme["back"], pause_rect)

    # Draw particles
    # for particle in player.particles:
    #   particle.display()

    pg.display.flip()

    clock.tick(m.FPS)


def main():
  running = True

  start_button = Button(pg.Rect(0, 0, 200, 50), "start", m.base_button, m.base_button_hover, m.small_title_font)
  start_button.center((300, 325))

  title_surfaces: list[pg.Surface] = [
    m.title_font.render("T", False, m.RED),
    m.title_font.render("E", False, m.ORANGE),
    m.title_font.render("T", False, m.YELLOW),
    m.title_font.render("R", False, m.GREEN),
    m.title_font.render("I", False, m.BLUE),
    m.title_font.render("S", False, m.PINK),
  ]

  title_pos: list[pg.Rect] = []
  title_offset = 99.5
  for surface in title_surfaces:
    surface_rect = surface.get_rect()
    surface_rect.center = (surface_rect.center[0] + title_offset, 150)
    title_offset += 66.8
    title_pos.append(surface_rect)

  title = list(zip(title_surfaces, title_pos))


  while running:

    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False
        break

      if event.type == pg.MOUSEBUTTONDOWN:
        if start_button.collidepoint(event.pos):
          game_loop()

      if event.type == pg.MOUSEMOTION:
        start_button.hover(event.pos)

    screen.fill(m.DARK_BLUE)


    for surface, pos in title:
      screen.blit(surface, pos)

    start_button.display(screen)

    pg.display.flip()

    clock.tick(m.FPS)


if __name__ == "__main__":
  main()
  pg.quit()