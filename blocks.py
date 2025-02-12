# Arden Boettcher
# 1/29/25
# Block Classes

from pygame import Rect, Surface, rect, draw
from world_class import World
from grid_class import Grid

class Block:

  # The perameters are provided by the block type (see the child classes below)
  def __init__(self, cords: list, type: str, center: list[int], grid: Grid):

    # A list of (usually 4) cordnate values that define the pos of each pixel
    self.cords:list[list[int]] = cords

    # Block type for color
    self.type:str = type

    # The center of rotation
    self.center:list[int] = center

    # A safety net # WIP
    self.safe = False

    # Rectangles for
    self.rects = [Rect((grid.pos[0] + cordnate[0] * grid.sq_size[0] + 1, grid.pos[1] + (cordnate[1] - 2) * grid.sq_size[0] + 1), grid.sq_size) for cordnate in self.cords]
    self.grid = grid




  # Rotates clockwise
  def r_rotate(self, world: World):
    # See the notes for l_rotate()
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
    self.update_rects()





  # Rotates counter clockwise
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
        if not world.get_block(cord)[0]:
          continue # This skips the rest of the loop

      except IndexError:
        pass # If an index error is raised then it continues the rest of the code eventually reseting the cords

      print("invalid rotate")
      self.cords = old_cords
      self.safe = False
      break

    # Updates the display rectangles
    self.update_rects()


  # Redefines the rects
  def update_rects(self):
    self.rects = [Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + (cordnate[1] - 2) * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.cords]



  def movedown(self, world: World) -> bool:
    self.cords = [(cordnate[0], cordnate[1] + 1) for cordnate in self.cords]
    self.center[1] += 1
    self.update_rects()

    for cord in self.cords:

      # The try is for index errors which are raised if the block is outside the world
      try:
        # Checks if the cords is inside a block in the world
        if not world.get_block(cord)[0]:
          # Please note the NOT modifier

          # This repeats until the loop is over or the if statement above returns false
          continue

      # An IndexError is raised when the block is outside of the world
      except IndexError:
        pass # This continues the code to the part where it resets the blocks

      # This part of the code is for reseting the position
      self.cords = [(cordnate[0], cordnate[1] - 1) for cordnate in self.cords]
      self.center[1] -= 1
      self.update_rects()
      return False
    self.safe = False
    return True



  def fastdrop(self, world: World):
    going = True
    while going:
      going = self.movedown(world)




  def display(self, surface: Surface, colors: dict[str, int]):
    for rect in self.rects:
      draw.rect(surface, colors[self.type], rect)



  def right(self, world: World):
    self.cords = [[cordnate[0] + 1, cordnate[1]] for cordnate in self.cords]
    self.center[0] += 1

    for cord in self.cords:
      try:
        if not world.get_block(cord)[0]:
          continue
      except IndexError:
        pass
      self.cords = [[cordnate[0] - 1, cordnate[1]] for cordnate in self.cords]
      self.center[0] -= 1

      break

    self.update_rects()



  def left(self, world: World):
    self.cords = [[cordnate[0] - 1, cordnate[1]] for cordnate in self.cords]
    self.center[0] -= 1

    for cord in self.cords:
      try:
        if cord[0] < 0:
          raise IndexError
        if not world.get_block(cord)[0]:
          continue
      except IndexError:
        pass
      self.cords = [[cordnate[0] + 1, cordnate[1]] for cordnate in self.cords]
      self.center[0] += 1

      break

    self.update_rects()




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



class Hover_Block(Block):
  def __init__(self, block: Block):
    self.rects = block.rects
    self.cords = block.cords

    # The center doesn't matter as it's only used for rotation
    self.center = [0, 0]

  def update(self, world):
    self.fastdrop(world)