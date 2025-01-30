# Arden Boettcher
# 1/29/25
# Block Classes

class Block:
  def __init__(self):
    self.cords = []
    self.type = ""
    self.rotation = 0
    self.center = []


class o_Block(Block):
  def __init__(self):
    self.cords = [(0, 0), (1, 0), (1, 1), (0, 1)]
    self.type = "o"
    self.rotation = 0
    self.center = [1, 1]

class i_Block(Block):
  def __init__(self):
    self.cords = [(0, 0), (0, 1), (0, 2), (0, 3)]
    self.type = "i"
    self.rotation = 0
    self.center = [1, 2]


class s_Block(Block):
  def __init__(self):
    self.cords = [(0, 1), (1, 1), (1, 0), (2, 0)]
    self.type = "s"
    self.rotation = 0
    self.center = []


class z_Block(Block):
  def __init__(self):
    self.cords = [(0, 0), (1, 0), (1, 1), (2, 1)]
    self.type = "z"
    self.rotation = 0
    self.center = []


class l_Block(Block):
  def __init__(self):
    self.cords = [(0, 1), (1, 1), (1, 2), (0, 2)]
    self.type = "l"
    self.rotation = 0
    self.center = [1, 1]

class j_Block(Block):
  def __init__(self):
    self.cords = [(0, 0), (0, 1), (1, 1), (2, 1)]
    self.type = "j"
    self.rotation = 0
    self.center = [1, 1]

class t_Block(Block):
  def __init__(self):
    self.cords = [(0, 1), (1, 0), (1, 1), (2, 1)]
    self.type = "t"
    self.rotation = 0
    self.center = [1, 1]