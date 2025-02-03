# import pygame as pg

# pg.init()

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# test_rects = [
#     pg.Rect(50, 87, 12, 36),
#     pg.Rect(38, 111, 12, 12)
#   ]

# main_rect = pg.Rect(25, 80, 50, 50)

# screen = pg.display.set_mode((100, 260))
# clock = pg.time.Clock()

# running = True
# while running:
#   for event in pg.event.get():
#     if event.type == pg.QUIT:
#       running = False

#   screen.fill(BLACK)
#   pg.draw.rect(screen, WHITE, main_rect)
#   for rect in test_rects:
#     pg.draw.rect(screen, BLACK, rect)

#   pg.display.update()
#   clock.tick(60)