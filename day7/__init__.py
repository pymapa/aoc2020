import re
file = open("data_day7.txt")

class Bag:
  def __init__(self, name='root', bags=None):
    self.name = name.strip()
    self.bags = []
    if bags is not None:
      for bag in bags:
        self.add_child(bag)
  
  def __hash__(self):
    return hash(self.name)

  def add_child(self, node):
    self.bags.append(node)

  def hasChild(self, bagName):
    if len(self.bags) == 0:
      return False
    res = [item for item in self.bags
      if item[1] == bagName]
    return len(res) > 0

  def __repr__(self):
    return '{}, {}'.format(self.name, self.bags)

  def __eq__(self, other):
    return self.name == other.name and \
      self.bags == other.bags

def createBag(rule):
  parts = re.split(' bags |contain | bags| bag| bags|, ', rule)
  bag = Bag(parts.pop(0), [])
  if 'no other bags' in rule:
    return bag
  for part in parts:
    if part != '' and part != '.':
      number = int(re.findall(r'\d+', part)[0])
      text = ''.join(i for i in part if not i.isdigit())
      bag.add_child((number, text.strip()))
  return bag

def findParentBags(bags, name, acc):
  acc += 1
  parentBags = []
  for bag in bags:
    if bag.hasChild(name):
      # print('bag {} contains bag {}'.format(bag, name) )
      parentBags.append(bag)
      parentBags.extend(findParentBags(bags, bag.name, acc))
  return set(parentBags)

def countChildBags(bags, name, factor):
  bag = [x for x in bags if x.name == name][0]
  count = 0
  for child in bag.bags:
    amount = child[0]
    bagName = child[1]
    count += amount * factor
    count += countChildBags(bags, bagName, amount * factor)
  return count

def main():
  rules = file.read().split("\n")
  bags = []
  for rule in rules:
    bags.append(createBag(rule))
  
  parentBags = findParentBags(bags, 'shiny gold', 0)
  print('Parent bags: ', len(parentBags))

  childBagsCount = countChildBags(bags, 'shiny gold', 1)
  print('Child bags: ', childBagsCount)

if __name__ == "__main__":
  main()