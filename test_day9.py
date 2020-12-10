
import unittest

from day9 import parseData, findInvalidNumber, findCorrectNumbers

data1 = """145378
  151884
  157245
  171817
  186982
  198656
  171284
  237704
  180642
  202270
  194656
  195807
  243648
  240330
  305405
  209884
  276843"""

data2 = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
  ]
class Day9Test(unittest.TestCase):


  def test_parseData(self):
    dataList = parseData(data1)
    expect = [
      145378,
      151884,
      157245,
      171817,
      186982,
      198656,
      171284,
      237704,
      180642,
      202270,
      194656,
      195807,
      243648,
      240330,
      305405,
      209884,
      276843
    ]
    self.assertEqual(dataList, expect)

  def test__findInvalidNumber(self):
    preamble = 5
    number = findInvalidNumber(0, data2, preamble)
    self.assertEqual(number, 127)

  def test__findCorrectNumbers(self):
    expect = [15, 25, 40, 47]
    number = 127
    self.assertEqual(findCorrectNumbers(number, 0, data2), expect)

    

if __name__ == "__main__":
  unittest.main()