# Arden Boettcher
# 1/29/25
# Block Classes

from pygame import Rect, rect
from world_class import World
from grid_class import Grid

class Block:
  def __init__(self, cords: list, type: str, center: list[int], grid: Grid):
    self.cords:list[list[int]] = cords
    self.type:str = type
    self.rotation = 0
    self.center:list[int] = center
    self.safe = False
    self.rects = [Rect((grid.pos[0] + cordnate[0] * grid.sq_size[0] + 1, grid.pos[1] + (cordnate[1] - 2) * grid.sq_size[0] + 1), grid.sq_size) for cordnate in self.cords]
    self.grid = grid


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

      print("invalid rotate")
      self.cords = old_cords
      self.safe = False



  def l_rotate(self, world: World):
    old_cords = []

    for cord in self.cords:
      # Saves the cords
      old_cords.append(cord)

      # Makes each axis relative to the center
      relative_x = cord[0] - self.center[0]
      relative_y = cord[1] - self.center[1]

      # Rotates it 90 degrees counterclockwise
      x = relative_y
      y = -relative_x

      # Updates the cordnates
      self.cords[self.cords.index(cord)] = [x + self.center[0], y + self.center[1]]
    self.safe = True

    # Checks if any of the cords intersect with the world
    for cord in self.cords:
      try:
        # Checks if the index is out of range
        if cord[0] < 0:
          raise IndexError
        # Checks the worlds at the cords
        if world.get_block(cord)[0] != None:
          continue # This skips the rest of the loop

      except IndexError:
        pass # If an index error is raised then it continues the rest of the code eventually reseting the cords

      print("invalid rotate")
      self.cords = old_cords
      self.safe = False
      break



  def update_rects(self):
    self.rects = [Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + (cordnate[1] - 2) * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.cords]



  def movedown(self, world) -> bool:
    self.cords = [(cordnate[0], cordnate[1] + 1) for cordnate in self.cords]
    self.center[1] += 1
    self.update_rects()

    for cord in self.cords:
      try:
        if not world.get_block(cord)[0]:
          continue
      except IndexError:
        pass
      self.cords = [(cordnate[0], cordnate[1] - 1) for cordnate in self.cords]
      self.center[1] -= 1
      return False
    self.safe = False
    return True


  def fastdrop(self, world):
    going = True
    while going:
      going = self.movedown(world)






class o_Block(Block):
  def __init__(self, grid):
    Block.__init__(
      self,
      [[5, 2], [6, 2], [6, 3], [5, 3]],
      "o",
      [6, 3],
      grid
    )

  def r_rotate(self, arg):
    self.safe = True

  def l_rotate(self, arg):
    self.safe = True

  def reset_pos(self, grid):
    self.__init__(grid)
    self.update_rects()
    return self


class i_Block(Block):
  def __init__(self, grid):
    Block.__init__(
      self,
      [[3, 2], [4, 2], [5, 2], [6, 2]],
      "i",
      [4, 2],
      grid
    )

  def reset_pos(self, grid):
    self.__init__(grid)
    self.update_rects()
    return self



class s_Block(Block):
  def __init__(self, grid):
    Block.__init__(
      self,
      [[4, 3], [5, 3], [5, 2], [6, 2]],
      "s",
      [5, 2],
      grid
    )


  def reset_pos(self, grid):
    self.__init__(grid)
    self.update_rects()
    return self


class z_Block(Block):
  def __init__(self, grid):
    Block.__init__(
      self,
      [[4, 2], [5, 2], [5, 3], [6, 3]],
      "z",
      [5, 2],
      grid
    )

  def reset_pos(self, grid):
    self.__init__(grid)
    self.update_rects()
    return self


class l_Block(Block):
  def __init__(self, grid):
    Block.__init__(
      self,
      [[4, 3], [5, 3], [6, 3], [6, 2]],
      "l",
      [5, 3],
      grid
    )

  def reset_pos(self, grid):
    self.__init__(grid)
    self.update_rects()
    return self


class j_Block(Block):
  def __init__(self, grid):
    Block.__init__(
      self,
      [[4, 2], [4, 3], [5, 3], [6, 3]],
      "j",
      [5, 3],
      grid
    )

  def reset_pos(self, grid):
    self.__init__(grid)
    self.update_rects()
    return self

class t_Block(Block):
  def __init__(self, grid):
    Block.__init__(
      self,
      [[4, 3], [5, 2], [5, 3], [6, 3]],
      "t",
      [5, 3],
      grid
    )

  def reset_pos(self, grid):
    self.__init__(grid)
    self.update_rects()
    return self