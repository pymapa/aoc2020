import re
file = open("data.txt")

def convertToBindary(word):
  binaryWord = ''
  for c in word:
    if c == 'F':
      binaryWord += '0'
    elif c == 'B':
      binaryWord += '1'
    elif c == 'L':
      binaryWord += '0'
    elif c == 'R':
      binaryWord += '1'
  return int(binaryWord, 2)

def calculateSeatId(row, column):
  return row * 8 + column

def nextSeatEmpty(passportIds, index):
  return passportIds[index] + 1 != passportIds[index + 1]

def main():
  passports = file.read().split("\n")
  passportIds = []
  passportsDecoded = []
  for passport in passports:
    row = passport[:7]
    column = passport[7:]
    rowBinary = convertToBindary(row)
    columnBinary = convertToBindary(column)
    passportsDecoded.append((rowBinary, columnBinary))
    passportIds.append(calculateSeatId(rowBinary, columnBinary))

  sortedIds = sorted(passportIds)
  for i in range(len(sortedIds)):
    if nextSeatEmpty(sortedIds, i):
      print(sortedIds[i])

if __name__ == "__main__":
  main()