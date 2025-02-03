## Tetris To-Do

### 1. Be able to see the next piece

This is a bit more complicated than the hold piece cube (but not by much).\
You need to change the rectangles to be relative to the cube
which will probably look like this:
```Python
rects = [pg.Rect(num, num, 12, 12), pg.Rect(num, num, 12, 12)]

for rect in rects:
  rect.x += box.x
  rect.y += box.y
```

You then have to change how Player.newblock() works.\
Instead of grabing a block directly from the blocks list you need a nextblock variable that it will take from.

```Python
self.current_block = self.nextblock

self.nextblock = random_block
```

To let this work nextblock has to already have a block we can do this by creating a block_setup() method to define nextblock before newblock() is used.\
This is what the Player.block_setup() method would look like:

```Python
def block_setup(self):
  x = randint()
  self.nextblock = self.blocks[x]
  del self.blocks[x]
  return
```

### 2. Particles!!!

I can actually work on this now bc it has nothing to do with the changes made on the 1/31/25 (yesterday at the moment) but I'd like to make some sudo code before getting into this complicated of a topic

#### Goals For Particles:

- Change over time
  - pos
  - size
  - color
  - rotation
  - the rate of change
  - ect.

#### Changes dict formatting notes:

```Python
# Variables

"width": list[int]      # rect width
"height": list[int]     # rect height
"x": list[int]          # rect x pos
"y": list[int]          # rect y pos
"rotation": list[int]   # rect/surface rotation
"color": list[int]      # display color

# each is a list that contains multiple ints
# for example

"width": [15, 0, 0.5]
# index 0 is the current rate of change
# index 1 is the rate
# index 2 is the mult
```

__Please note:__\
Color is going to be weird as it is the only list please format it like
```Python
"{color channel} {modifier}": int
```
color channel being either r, g, b, or t, "rgb" is self explanitory but "t" is transparency

#### Sudocode For Particles:

I want to make a parent particle class that works something like this:

```Python
class Particle:
  def __init__(self):
    pass
# It's all passing because each individual particle will be very different from eachother
  def update(self):
    pass
  def display(self):
    pass
```

And an example of a Rect particle:

```Python
class Rect_Part(Particle):
  def __init__(self, pos: tuple, size: tuple, color: tuple, changes: dict):
    self.rect = pg.Rect(pos, size)
    if len(color) = 3
      self.color = list(color)
      self.color.append(255)
    else:
      self.color = color
    self.changes = changes

  def update(self):  # use pygame.time.set_timer for calling the update method
    self.rect.width += self.changes["width"][0]
    self.rect.height += self.changes["height"][0]

    self.rect.x += self.changes["x"][0]
    self.rect.y += self.changes["y"][0]

    # rotating things is complicated so make a method for it
    self.rotate(self.changes["rotation"][0])

    self.color[0] += self.changes["r"][0]
    self.color[1] += self.changes["g"][0]
    self.color[2] += self.changes["b"][0]
    self.color[3] += self.changes["t"][0]

    # this does all the rate/mult changes
    for key in self.changes["key"]:
      self.changes[key][0] *= self.changes[key][2]
      self.changes[key][0] += self.changes[key][1]

  def display(self, surface):
    pg.draw.rect(surface, tuple(self.color), self.rect)
```

I dont really know about the changes dict currently. It seems kinda slow to do this for EVERY particle on EVERY frame.\
Of course the code is already doing a lot for everything on every frame so a bit of addition should be fine.\
Y'know as long as it isn't an if  statement

### 3. High scores

#### Writing

This is pretty simple as it's it should simply use the json.dump() function to dump a dictionary with "name" and "score" keys.\
I'll append the highscore.json file with the dictionary thus saving the score.

like so:
```Python
highscore = {
  "name", "ASS",
  "score", 1234
}


file = open("filename.json", "a")

json_object = json.dump(highscore)
file.write(json_object)
```

#### Reading

