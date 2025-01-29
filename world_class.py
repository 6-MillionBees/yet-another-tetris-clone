class World:
  def __init__(self, size: tuple):
    self.blocks = [[[None, None] for row in range(size[1])] for column in range(size[0])]

  def get_block(self, cords: tuple) -> list:
    return self.blocks[cords[0]][cords[1]]

  def change_block(self, cords: tuple, change: list) -> None:
    self.blocks[cords[0]][cords[1]] = change