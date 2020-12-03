import re
data = open("data.txt")
array = data.read().split("\n")

class Step:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def trees(self):
    return travelWithStep(self.x, self.y)

def isTree(line, x):
  return line[x] == '#'

def travelWithStep(stepX, stepY):
  x = 0
  treeCount = 0
  for line in array[::stepY]:
    length = len(line)
    if isTree(line, x):
      treeCount += 1
    if x + stepX <= length - 1:
      x += stepX
    else:
      x = x + stepX - length
  return treeCount

def main():
  steps = []
  steps.append(Step(1, 1))
  steps.append(Step(3, 1))
  steps.append(Step(5, 1))
  steps.append(Step(7, 1))
  steps.append(Step(1, 2))

  treesMultiplied = 1
  for step in steps:
    treesMultiplied = treesMultiplied * step.trees()

  print(treesMultiplied)
main()