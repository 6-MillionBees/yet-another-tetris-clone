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
pg.display.set_caption("Tetris")



def pause(player: player_class.Player):
  unpause_rect = pg.Rect(200, 325, 200, 50)
  pause_text = m.nums_font.render("Paused", False, m.DEEP_BLUE)

  pause_text_rect = pause_text.get_rect()
  pause_text_rect.center = (300, 200)

  unpause_text = m.nums_font.render("Unpause", False, m.DEEP_BLUE)
  unpause_text_pos = m.center_text(unpause_text, unpause_rect)

  quit_rect = pg.Rect(200, 400, 200, 50)
  quit_text = m.nums_font.render("Quit", False, m.DEEP_BLUE)
  quit_text_pos = m.center_text(quit_text, quit_rect)


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
        if unpause_rect.collidepoint(event.pos):
          is_open = False
        elif quit_rect.collidepoint(event.pos):
          pg.quit()
          quit()

    screen.fill(m.GREY)

    screen.blit(pause_text, pause_text_rect)

    m.outline(unpause_rect, m.BLACK, 2, screen)
    pg.draw.rect(screen, m.GREY, unpause_rect)

    m.outline(quit_rect, m.BLACK, 2, screen)
    pg.draw.rect(screen, m.GREY, quit_rect)

    screen.blit(unpause_text, unpause_text_pos)
    screen.blit(quit_text, quit_text_pos)


    pg.display.update()
    clock.tick(m.FPS)





def game_loop():
  grid = grid_class.Grid(10, 20, (30, 30), (100, -2))
  player = player_class.Player(grid, m.colors, screen)

  pg.time.set_timer(m.MOVEDOWN, player.speed, 1)
  pg.time.set_timer(m.PARTICLE_UPDATE, int(1000 / m.FPS))

  pause_rect = pg.Rect(550, 0, 50, 50)

  while player.alive:

    # Event Handling
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        quit()

      # Handles the player events (most of the events)
      # See player_class.py for more info
      player.player_events(event)

      if event.type == pg.MOUSEBUTTONDOWN:
        if pause_rect.collidepoint(event.pos):
          pause(player)

      if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
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