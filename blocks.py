# Arden Boettcher
# 1/29/25
# Block Classes

from world_class import World

class Block:
  def __init__(self, cords, type, center):
    self.rects = # WIP
    self.cords:list[list[int]] = cords
    self.type:str = type
    self.rotation = 0
    self.center:list[int] = center
    self.safe = False

  def r_rotate(self, world: World):
    old_cords = []
    for cord in self.cords:
      old_cords.append(cord)
      relative_x = cord[0] - self.center[0]
      relative_y = cord[1] - self.center[1]
      x = -relative_y
      y = relative_x
      self.cords[self.cords.index(cord)] = [x + self.center[0], y + self.center[1]]
    self.safe = True

    for cord in self.cords:
      try:
        if cord[0] < 0:
          raise IndexError
        if not world.get_block(cord)[0]:
          continue
      except IndexError:
        pass

      self.cords = old_cords
      self.safe = False

  def l_rotate(self, world: World):
    old_cords = []
    for cord in self.cords:
      old_cords.append(cord)
      relative_x = cord[0] - self.center[0]
      relative_y = cord[1] - self.center[1]
      x = relative_y
      y = -relative_x
      self.cords[self.cords.index(cord)] = [x + self.center[0], y + self.center[1]]
    self.safe = True

    for cord in self.cords:
      try:
        if cord[0] < 0:
          raise IndexError
        if not world.get_block(cord)[0]:
          continue
      except IndexError:
        pass

      self.cords = old_cords
      self.safe = False




class o_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[5, 2], [6, 2], [6, 3], [5, 3]],
      "o",
      [6, 3]
    )

  def r_rotate(self, arg):
    self.safe = True

  def l_rotate(self, arg):
    self.safe = True

  def reset_pos(self):
    self.__init__()
    return self


class i_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[3, 2], [4, 2], [5, 2], [6, 2]],
      "i",
      [4, 2]
    )

  def reset_pos(self):
    self.__init__()
    return self



class s_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[4, 3], [5, 3], [5, 2], [6, 2]],
      "s",
      [5, 2]
    )

  def reset_pos(self):
    self.__init__()
    return self



class z_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[4, 2], [5, 2], [5, 3], [6, 3]],
      "z",
      [5, 2]
    )

  def reset_pos(self):
    self.__init__()
    return self


class l_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[4, 3], [5, 3], [6, 3], [6, 2]],
      "l",
      [5, 3]
    )

  def reset_pos(self):
    self.__init__()
    return self


class j_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[4, 2], [4, 3], [5, 3], [6, 3]],
      "j",
      [5, 3]
    )

  def reset_pos(self):
    self.__init__()
    return self

class t_Block(Block):
  def __init__(self):
    Block.__init__(
      self,
      [[4, 3], [5, 2], [5, 3], [6, 3]],
      "t",
      [5, 3]
    )

  def reset_pos(self):
    self.__init__()
    return self