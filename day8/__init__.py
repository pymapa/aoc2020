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
  if program.pointer == 15:
    print(instruction)
  operations = {
    'acc' : acc,
    'jmp' : jmp,
    'nop' : nop
  }
  operations[op](program, arg)

def runProgram(instructions):
  p = Program()
  history = []
  p = Program()
  looping = False
  while p.pointer < len(instructions):
    if p.pointer in history:
      looping = True
      break
    history.append(p.pointer)
    runInstruction(p, instructions[p.pointer])
  if not looping:
    print(p.accumulator)
  return looping

def changeJmpToNop(instruction):
  return instruction.replace('jmp', 'nop')

def changeNopToJmp(instruction):
  return instruction.replace('nop', 'jmp')

def main():
  print('running program...')
  instructions = file.read().split("\n")

  for index, instruction in enumerate(instructions):
    op = re.findall(r'^\w+', instruction)[0]
    if op == 'nop':
      instructions[index] = changeNopToJmp(instruction)
      looping = runProgram(instructions)
      if looping:
        print('looping')
        instructions[index] = changeJmpToNop(instruction)
      else:
        print('index ', index)
        print('not looping')
        break
    if op == 'jmp':
      instructions[index] = changeJmpToNop(instruction)
      looping = runProgram(instructions)
      if looping:
        print('looping')
        instructions[index] = changeNopToJmp(instruction)
      else:
        print('index ', index)
        print('not looping')
        break


if __name__ == "__main__":
  main()