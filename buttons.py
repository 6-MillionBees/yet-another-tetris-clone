# Arden Boettcher
# 2/18/25
# Buttons class

import pygame as pg

class Button:
  def __init__(self, rect, text, ):
    self.rect = rect

  def collidepoint(self, pos):
    return self.rect.collidepoint(pos)