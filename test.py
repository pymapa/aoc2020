import unittest

from planeticket import createBag, findParentBags, countChildBags, Bag
class PlaneticketTest(unittest.TestCase):

  def test_createBag(self):
    """
    Test creating bag
    """
    rule = 'faded plum bags contain 2 wavy cyan bags, 1 navy turquoise bag.'
    bag = Bag('faded plum', [(2, 'wavy cyan'), (1, 'navy turquoise')])
    self.assertEqual(createBag(rule), bag)

  def test_hasChild(self):
    """
    Test finding by child
    """
    bag = Bag('faded plum', [(2, 'wavy cyan'), (1, 'navy turquoise')])
    res = bag.hasChild('wavy cyan')
    self.assertTrue(res)
    bag1 = Bag('gaded plum', [(2, 'wavy cyan'), (1, 'navy turquoise')])
    res1 = bag1.hasChild('gaded plum')
    self.assertFalse(res1)

  def test__findParentBags(self):
    """
    Test finding parent bags
    """
    file = """light red bags contain 1 bright white bag, 2 muted yellow bags.
      dark orange bags contain 3 bright white bags, 4 muted yellow bags.
      bright white bags contain 1 shiny gold bag.
      muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
      shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
      dark olive bags contain 3 faded blue bags, 4 dotted black bags.
      vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
      faded blue bags contain no other bags.
      dotted black bags contain no other bags."""
    

    rules = file.split("\n")
    bags = []
    for rule in rules:
      bag = createBag(rule)
      bags.append(bag)
    parentBags = findParentBags(bags, 'shiny gold', 0)
    self.assertEqual(len(parentBags), 4)

  def test__findChildBags(self):
    """
    Test finding child bags
    """
    file = """
    shiny gold bags contain 2 dark red bags.
    dark red bags contain 2 dark orange bags.
    dark orange bags contain 2 dark yellow bags.
    dark yellow bags contain 2 dark green bags.
    dark green bags contain 2 dark blue bags.
    dark blue bags contain 2 dark violet bags.
    dark violet bags contain no other bags."""

    rules = file.split("\n")
    bags = []
    for rule in rules:
      bag = createBag(rule)
      bags.append(bag)

    childBagsCount = countChildBags(bags, 'shiny gold', 1)
    self.assertEqual(childBagsCount, 126)

if __name__ == "__main__":
  unittest.main()