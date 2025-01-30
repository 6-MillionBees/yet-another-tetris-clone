# Arden Boettcher
# 1/29/25
# Block Classes

class Block:
  def __init__(self):
    pass
  def rotate_wise():
    pass
  def rotate_counter():
    pass


class o_Block(Block):
  def __init__(self):
    self.cords = [(0, 0), (1, 0), (1, 1), (0, 1)]
    self.type = "o"
    self.rotation = 0
    self.center = (1, 1)

  def rotate_wise():
    pass
  def rotate_counter():
    pass


class i_Block(Block):
  def __init__(self):
    self.cords = [(0, 0), (0, 1), (0, 2), (0, 3)]
    self.type = "i"
    self.rotation = 0
    self.center = (1, 2)

#   def rotate_wise(self):

#   def rotate_counter(self):


# class s_Block:
#   def __init__(self):
#     self.cords =