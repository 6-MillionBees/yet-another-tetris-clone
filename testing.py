class Thingy:
  def __init__(self):
    self.num = 0

  def update(self):
    self.num += 1
    print(self.num)
    if self.num > 10:


thang = Thingy()

while True:
  thang.update()