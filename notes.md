

## Tetris To-Do

### 1. ) Line Clear effects / General Particle things

<<<<<<< HEAD
There are multiple youtube videos on this topic
=======
#### Needs to:

- change size (over time)
- disapear


<!-- ### 2. Particles!!!

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
 -->
>>>>>>> 23690493aadc719cdafab72f97f44ad93b9b29d9
