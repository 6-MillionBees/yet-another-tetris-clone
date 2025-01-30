from grid_class import Grid

class World:
  def __init__(self, size: tuple):
    self.blocks = [[[None, None] for column in range(size[0])] for row in range(size[1])]

  def get_block(self, cords: tuple) -> list:
    return self.blocks[cords[1]][cords[0]]

  def change_block(self, cords: tuple, change: list) -> None:
    self.blocks[cords[1]][cords[0]] = change

  def check_lines(self, grid) -> int:
    full_lines = []
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
    return len(full_lines)

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


    # for row in self.blocks:
    #   for square in row:
    #     if square[0] == None:
    #       print(".", end="")
    #     else:
    #       print("#", end="")

    #   print()

    # print()