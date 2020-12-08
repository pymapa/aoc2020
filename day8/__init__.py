file = open("data_day8.txt")
import re

class Program:
  def __init__(self, pointer=0, accumulator=0):
    self.pointer = pointer
    self.accumulator = accumulator

  def movePointer(self, move):
    self.pointer += move

  def addAccumulator(self, sum):
    self.accumulator += sum

def acc(program, arg):
  program.addAccumulator(arg)
  program.movePointer(1)

def jmp(program, arg):
  program.movePointer(arg)

def nop(program, arg):
  program.movePointer(1)

def runInstruction(program, instruction):
  op = re.findall(r'^\w+', instruction)[0]
  arg = int(re.findall(r'-?\d+', instruction)[0])
  operations = {
    'acc' : acc,
    'jmp' : jmp,
    'nop' : nop
  }
  operations[op](program, arg)

def main():
  print('running program...')
  instructions = file.read().split("\n")

  history = []
  p = Program()
  while p.pointer < len(instructions):
    if p.pointer in history:
      break
    history.append(p.pointer)
    runInstruction(p, instructions[p.pointer])

  print(p.accumulator)

if __name__ == "__main__":
  main()