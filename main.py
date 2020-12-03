import re
data = open("data.txt")
array = data.read().split("\n")

def isTree(line, x):
  return line[x] == '#'

def main():
  x = 0
  treeCount = 0
  step = 3

  for line in array:
    length = len(line)
    if isTree(line, x):
      treeCount += 1
    if x + step <= length - 1:
      x += step
    else:
      x = x + step - length
      

  print(treeCount)
main()