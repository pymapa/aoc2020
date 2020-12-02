data = open("data.txt")
lines = data.read().split("\n")

def checkDoubleEntry(x, y):
  for z in lines:
    if(int(x) + int(y) + int(z) == 2020):
      print(int(x) * int(y) * int(z))


def checkEntry(x):
  for y in lines:
    checkDoubleEntry(x, y)

for x in lines:
  checkEntry(x)

  