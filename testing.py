import json

highscores = [
  {
    "name": "BAD",
    "score": 1004
  },
  {
    "name": "GOO",
    "score": 2000
  },
  {
    "name": "ASS",
    "score": 2
  }
]

highscores.sort(key= lambda dic: dic["score"], reverse= True)
file = open("highscores.json", "a")

file.write("{\n\"scores\": [\n")

for score in highscores:
  json_object = json.dumps(score, indent= 2)
  file.write(json_object)

file.write("\n]\n}")