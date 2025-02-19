# Arden Boettcher
# 2/18/25
# Buttons class

import pygame as pg
import misc as m

class Button:
  def __init__(self, rect, text: str, colors: dict, hover_colors: dict, font: pg.font.Font):
    self.rect = rect
    self.font = font
    self.text_str = text
    self.text = font.render(text, False, colors["text"])
    self.colors = colors
    self.hover_colors = hover_colors
    self.active_colors = colors
    self.text_pos = m.center_text(self.text, self.rect)

  def collidepoint(self, pos):
    return self.rect.collidepoint(pos)

  def center(self, pos):
    og_size = (self.rect.width, self.rect.height)
    self.rect = pg.Rect((pos[0] - (og_size[0] / 2), pos[1] - (og_size[1] / 2)), og_size)
    self.center_text()

  def hover(self, pos):
    if self.collidepoint(pos):
      self.active_colors = self.hover_colors
      self.text = self.font.render(self.text_str, False, self.hover_colors["text"])
    else:
      self.active_colors = self.colors
      self.text = self.font.render(self.text_str, False, self.colors["text"])


  def update_rect(self, rect: pg.Rect):
    self.rect = rect
    self.center_text()


  def update_text(self, text: str, color, font: pg.font.Font = None):
    if font != None:
      self.font = font

    self.text_str = text
    self.text = self.font.render(text, False, color)
    self.center_text()


  def center_text(self, offsets = (0, 0)):
    self.text_pos = m.center_text(self.text, self.rect, offsets)

  def display(self, surface: pg.Surface):
    m.outline(self.rect, self.active_colors["out"], 2, surface)
    pg.draw.rect(surface, self.active_colors["main"], self.rect)

    surface.blit(self.text, self.text_pos)
