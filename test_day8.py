import unittest

from day8 import Program, runInstruction

class Day8Test(unittest.TestCase):

  def test_runInstruction(self):
    """
    Test running instructions
    """
    p = Program(0, 0)
    instructions = [
      'acc 12',
      'jmp 2',
      'nop 12',
      'acc -2',
      'nop 3',
    ]
    runInstruction(p, instructions[0])
    self.assertEqual(p.pointer, 1)
    self.assertEqual(p.accumulator, 12)

    runInstruction(p, instructions[p.pointer])
    self.assertEqual(p.pointer, 3)
    self.assertEqual(p.accumulator, 12)

    runInstruction(p, instructions[p.pointer])
    self.assertEqual(p.pointer, 4)
    self.assertEqual(p.accumulator, 10)

if __name__ == "__main__":
    unittest.main()