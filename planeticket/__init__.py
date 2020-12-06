import re
file = open("data.txt")

def getPositiveAnswers(group):
  rows = group.split("\n")
  answers = rows[0]
  for row in rows:
    answers = [value for value in row if value in answers]
  return sorted(set(answers))

def main():
  groups = file.read().split("\n\n")
  sum = 0
  for group in groups:
    sum += len(getPositiveAnswers(group))

  print(sum)

if __name__ == "__main__":
  main()