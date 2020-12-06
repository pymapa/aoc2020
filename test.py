import unittest

from planeticket import getPositiveAnswers
class PlaneticketTest(unittest.TestCase):

  def test_getPositiveAnswers(self):
    """
    Test counting positive answers
    """
    group = 'abc\naabcd\nfgbc'
    self.assertEqual(getPositiveAnswers(group), ['b', 'c'])


if __name__ == "__main__":
  unittest.main()