from grid_class import Grid

class World:
  def __init__(self, size: tuple[int, int]):
    self.blocks = [[[None, None] for column in range(size[0])] for row in range(size[1] + 2)]

  def get_block(self, cords: tuple) -> list:
    return self.blocks[cords[1]][cords[0]]

  def change_block(self, cords: tuple, change: list) -> None:
    self.blocks[cords[1]][cords[0]] = change

  def check_lines(self, grid) -> int:

    # for row in self.blocks: # This is to print the world for debugging
    #   for block in row:
    #     if not block[0]:
    #       print(".", end="")
    #     else:
    #       print(block[1], end="")
    #   print()

    full_lines: list[int] = []
    for row in self.blocks:
      full = False
      for column in row:
        if column[0] == None:
          full = False
          break
        else:
          full = True
      if full:
        full_lines.append(self.blocks.index(row))

    self.clear_lines(full_lines, grid)
    return full_lines

  def clear_lines(self, lines: list, grid: Grid):
    for line in lines:
      for index in range(line, -1, -1):
        if index == 0:
          self.blocks[index] = [[None, None] for block in range(len(self.blocks[0]))]
          continue
        self.blocks[index] = self.blocks[index - 1]
        for block in self.blocks[index]:
          if block[0] == None:
            continue

          block[0].y += grid.sq_size[1]

