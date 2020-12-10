file = open("data_day9.txt")


def parseData(data):
  result = []
  dataList = data.split("\n")
  for item in dataList:
    result.append(int(item.strip()))
  return result


def findInvalidNumber(begin, data, preamble):
  subset = data[begin:preamble]
  number = data[preamble]
  for x1 in subset:
    for x2 in subset[1::]:
      if x1 + x2 == number:
        number = findInvalidNumber(begin + 1, data, preamble + 1)
        break
  return number

def findCorrectNumbers(number, start, data):
  counter = 0
  result = []
  for x in data[start::]:
    counter += x
    result.append(x)
    if counter == number:
      break
    elif counter > number:
      result = findCorrectNumbers(number, start + 1, data)
      break
  return sorted(result)


def main():
  dataList = parseData(file.read())
  number = findInvalidNumber(0, dataList, 25)
  print(number)
  sumList = findCorrectNumbers(number, 0, dataList)
  print(sumList)
  print(sumList[0] + sumList[len(sumList)-1])

if __name__ == "__main__":
  main()