import re
data = open("data.txt")
lines = data.read().split("\n")

def main():
  validCount = 0

  def isValidEntry(x):
    passwordLineParts = re.split('-| |:', x)
    min = int(passwordLineParts[0])
    max = int(passwordLineParts[1])
    requiredChar = passwordLineParts[2]
    password = passwordLineParts[4]
    occurrence = password.count(requiredChar)
    if min <= occurrence <= max:
      return True
    return False

  for x in lines:
    if isValidEntry(x):
      validCount += 1

  print(validCount)

main()