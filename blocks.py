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
      relative_x = cord[0] - self.center[0]
      relative_y = cord[1] - self.center[1]
      x = -relative_y
      y = relative_x
      self.cords[self.cords.index(cord)] = [x + self.center[0], y + self.center[1]]

    for cord in self.cords:
      try:
        if cord[0] < 0:
          raise IndexError
        if not world.get_block(cord)[0]:
          continue
      except IndexError:
        pass

      self.cords = old_cords

  def l_rotate(self, world: World):
    old_cords = []
    for cord in self.cords:
      old_cords.append(cord)
      relative_x = cord[0] - self.center[0]
      relative_y = cord[1] - self.center[1]
      x = relative_y
      y = -relative_x
      self.cords[self.cords.index(cord)] = [x + self.center[0], y + self.center[1]]

    for cord in self.cords:
      try:
        if cord[0] < 0:
          raise IndexError
        if not world.get_block(cord)[0]:
          continue
      except IndexError:
        pass

      self.cords = old_cords




class o_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[5, 0], [6, 0], [6, 1], [5, 1]],
      "o",
      [6, 1]
    )

  def reset_pos(self):
    self.__init__()
    return self


class i_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[3, 0], [4, 0], [5, 0], [6, 0]],
      "i",
      [4, 0]
    )

  def reset_pos(self):
    self.__init__()
    return self



class s_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[4, 1], [5, 1], [5, 0], [6, 0]],
      "s",
      [5, 0]
    )

  def reset_pos(self):
    self.__init__()
    return self



class z_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[4, 0], [5, 0], [5, 1], [6, 1]],
      "z",
      [5, 0]
    )

  def reset_pos(self):
    self.__init__()
    return self


class l_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[4, 1], [5, 1], [6, 1], [6, 0]],
      "l",
      [5, 1]
    )

  def reset_pos(self):
    self.__init__()
    return self


class j_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[4, 0], [4, 1], [5, 1], [6, 1]],
      "j",
      [5, 1]
    )

  def reset_pos(self):
    self.__init__()
    return self

class t_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[4, 1], [5, 0], [5, 1], [6, 1]],
      "t",
      [5, 1]
    )

  def reset_pos(self):
    self.__init__()
    return self