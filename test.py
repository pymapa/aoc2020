import unittest

from planeticket import convertToBindary, calculateSeatId
class PlaneticketTest(unittest.TestCase):

  def test_convertToBinary(self):
    """
    Test string to binary converter
    """
    self.assertEqual(convertToBindary('BFBBBFFRRL'), 0b1011100110)
    self.assertEqual(convertToBindary('BFBBBFF'), 0b1011100)
    self.assertEqual(convertToBindary('LLR'), 0b001)

  def test_calculateSeatId(self):
    self.assertEqual(calculateSeatId(102, 4), 820)

if __name__ == "__main__":
  unittest.main()