# Arden Boettcher
# 1/29/25
# Block Classes

from pygame import Rect, Surface, rect, draw
from world_class import World
from grid_class import Grid
import misc as m

class Block:

  # The perameters are provided by the block type (see the child classes below)
  def __init__(self, cords: list, type: str, center: list[int], grid: Grid, world: World):

    # A list of (usually 4) cordnate values that define the pos of each pixel
    self.cords:list[list[int]] = cords

    # Block type for color
    self.type:str = type

    # The center of rotation
    self.center:list[int] = center

    # A safety net # WIP
    self.safe = False

    # Rectangles for drawing
    self.rects = [Rect((grid.pos[0] + cordnate[0] * grid.sq_size[0] + 1, grid.pos[1] + (cordnate[1] - 2) * grid.sq_size[0] + 1), grid.sq_size) for cordnate in self.cords]

    # Grid to refference for math things
    self.grid = grid

    # hover_block <3
    self.hover_block = Hover_Block(self, world)




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
    self.update_rects(world)





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
    self.update_rects(world)


  # Redefines the rects
  def update_rects(self, world: World):
    self.rects = [Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + (cordnate[1] - 2) * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.cords]
    self.hover_block.update(self, world)
    self.world = world


  def movedown(self, world: World) -> bool:
    self.cords = [(cordnate[0], cordnate[1] + 1) for cordnate in self.cords]
    self.center[1] += 1
    self.update_rects(world)

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
      self.update_rects(self.world)

      if self.safe:
        self.safe = False
        return True
      return False

    self.safe = False
    return True



  def fastdrop(self, world: World):
    going = True
    while going:
      going = self.movedown(world)


  def getworld(self, world: World):
    self.world = world

  def display(self, surface: Surface, colors: dict[str, int]):
    for rect in self.rects:
      draw.rect(surface, colors[self.type], rect)



  def right(self, world: World):
    self.cords = [[cordnate[0] + 1, cordnate[1]] for cordnate in self.cords]
    self.center[0] += 1
    moved = True

    for cord in self.cords:
      try:
        if not world.get_block(cord)[0]:
          continue
      except IndexError:
        pass
      self.cords = [[cordnate[0] - 1, cordnate[1]] for cordnate in self.cords]
      self.center[0] -= 1
      moved = False
      break

    if moved:
      self.safe = True

    self.update_rects(world)



  def left(self, world: World):
    self.cords = [[cordnate[0] - 1, cordnate[1]] for cordnate in self.cords]
    self.center[0] -= 1
    moved = True

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
      moved = False
      break

    if moved:
      self.safe = True

    self.update_rects(world)




# |=========================| Individual Blocks |=========================|


class o_Block(Block):
  def __init__(self, grid: Grid, world: World):
    Block.__init__(
      self,
      [[5, 2], [6, 2], [6, 3], [5, 3]],
      "o",
      [6, 3],
      grid,
      world
    )

  def r_rotate(self, arg):
    pass

  def l_rotate(self, arg):
    pass

  def reset_pos(self, grid: Grid, world: World):
    self.__init__(grid, world)
    return self


class i_Block(Block):
  def __init__(self, grid: Grid, world: World):
    Block.__init__(
      self,
      [[3, 2], [4, 2], [5, 2], [6, 2]],
      "i",
      [4, 2],
      grid,
      world
    )

  def reset_pos(self, grid, world):
    self.__init__(grid, world)
    return self



class s_Block(Block):
  def __init__(self, grid: Grid, world: World):
    Block.__init__(
      self,
      [[4, 3], [5, 3], [5, 2], [6, 2]],
      "s",
      [5, 2],
      grid,
      world
    )


  def reset_pos(self, grid: Grid, world: World):
    self.__init__(grid, world)
    return self


class z_Block(Block):
  def __init__(self, grid: Grid, world: World):
    Block.__init__(
      self,
      [[4, 2], [5, 2], [5, 3], [6, 3]],
      "z",
      [5, 2],
      grid,
      world
    )

  def reset_pos(self, grid: Grid, world: World):
    self.__init__(grid, world)
    return self


class l_Block(Block):
  def __init__(self, grid: Grid, world: World):
    Block.__init__(
      self,
      [[4, 3], [5, 3], [6, 3], [6, 2]],
      "l",
      [5, 3],
      grid,
      world
    )

  def reset_pos(self, grid: Grid, world: World):
    self.__init__(grid, world)
    return self


class j_Block(Block):
  def __init__(self, grid: Grid, world: World):
    Block.__init__(
      self,
      [[4, 2], [4, 3], [5, 3], [6, 3]],
      "j",
      [5, 3],
      grid,
      world
    )

  def reset_pos(self, grid: Grid, world: World):
    self.__init__(grid, world)
    return self

class t_Block(Block):
  def __init__(self, grid: Grid, world: World):
    Block.__init__(
      self,
      [[4, 3], [5, 2], [5, 3], [6, 3]],
      "t",
      [5, 3],
      grid,
      world
    )

  def reset_pos(self, grid: Grid, world: World):
    self.__init__(grid, world)
    return self






# |======================================| Hover Block |======================================|


# This isn't a child of the Block class as it is used in the main Block class
class Hover_Block:
  def __init__(self, block: Block, world: World):
    self.rects = block.rects
    self.cords = block.cords
    self.grid = block.grid
    self.update(block, world)



  def update(self, block: Block, world: World):
    self.cords = block.cords
    self.fastdrop(world)



  def movedown(self, world: World) -> bool:
    self.cords = [(cordnate[0], cordnate[1] + 1) for cordnate in self.cords]
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
      return False
    return True



  def fastdrop(self, world: World):
    going = True
    while going:
      going = self.movedown(world)
    self.update_rects()


  def update_rects(self):
    self.rects = [Rect((self.grid.pos[0] + cordnate[0] * self.grid.sq_size[0] + 1, self.grid.pos[1] + (cordnate[1] - 2) * self.grid.sq_size[0] + 1), self.grid.sq_size) for cordnate in self.cords]
    self.surfaces: list[list[Surface, tuple]] = [[Surface(rectangle.size), rectangle.topleft] for rectangle in self.rects]


  def display(self, surface: Surface, colorscheme: dict[str, int]):
    for surf in self.surfaces:
      surf[0].set_alpha(100)
      surf[0].fill(colorscheme["main"])
      surface.blit(surf[0], surf[1])