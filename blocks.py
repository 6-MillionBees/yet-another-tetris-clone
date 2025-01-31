# Arden Boettcher
# 1/29/25
# Block Classes

from world_class import World

class Block:
  def __init__(self, cords, type, center):
    self.cords:list[list[int]] = cords
    self.type:str = type
    self.rotation = 0
    self.center:list[int] = center

  def r_rotate(self, world: World):
    old_cords = []
    for cord in self.cords:
      old_cords.append(cord)
      x = cord[1]
      y = -cord[0]
      self.cords[self.cords.index(cord)] = [x, y]

    for cord in self.cords:
      try:
        if not world.get_block(cord)[0]:
          continue
      except IndexError:
        pass

      self.cords = old_cords



class o_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[0, 0], [1, 0], [1, 1], [0, 1]],
      "o",
      [1, 1]
    )


class i_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[0, 0], [0, 1], [0, 2], [0, 3]],
      "i",
      [1, 2]
    )


class s_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[0, 1], [1, 1], [1, 0], [2, 0]],
      "s",
      [1, 0]
    )



class z_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[0, 0], [1, 0], [1, 1], [2, 1]],
      "z",
      [1, 0]
    )


class l_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[0, 1], [1, 1], [2, 1], [2, 0]],
      "l",
      [1, 1]
    )


class j_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[0, 0], [0, 1], [1, 1], [2, 1]],
      "j",
      [1, 1]
    )

class t_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[0, 1], [1, 0], [1, 1], [2, 1]],
      "t",
      [1, 1]
    )