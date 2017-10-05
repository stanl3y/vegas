import unittest
from context import vegas
from vegas.outcomes import \
  Straight, Split, Street, Corner, FiveNumbers, Line, Dozen, Column, EvenMoney


class OutcomesTest(unittest.TestCase):
  """Constructor tests for various types of Outcome."""

  def test_straight_init(self):
    """Check the constructor of Straight-bet Outcome."""
    straight = Straight(17)
    self.assertEqual(straight.name, "Straight 17")
    self.assertEqual(straight.odds, 35)

  def test_split_init(self):
    """Check the constructor of Split-bet Outcome."""
    split = Split(11, 12)
    self.assertEqual(split.name, "Split 11-12")
    self.assertEqual(split.odds, 17)

  def test_street_init(self):
    """Check the constructor of Street-bet Outcome."""
    street = Street(16)
    self.assertEqual(street.name, "Street 16-17-18")
    self.assertEqual(street.odds, 11)

  def test_corner_init(self):
    """Check the constructor of Corner-bet Outcome."""
    corner = Corner(7)
    self.assertEqual(corner.name, "Corner 7-8-10-11")
    self.assertEqual(corner.odds, 8)

  def test_five_numbers_init(self):
    """Check the constructor of FiveNumbers-bet Outcome."""
    five_numbers = FiveNumbers()
    self.assertEqual(five_numbers.name, "Five Numbers")
    self.assertEqual(five_numbers.odds, 6)

  def test_line_init(self):
    """Check the constructor of Line-bet Outcome."""
    line = Line(19)
    self.assertEqual(line.name, "Line 19-20-21-22-23-24")
    self.assertEqual(line.odds, 5)

  def test_dozen_init(self):
    """Check the constructor of Dozen-bet Outcome."""
    dozen = Dozen(1)
    self.assertEqual(dozen.name, "Dozen 1")
    self.assertEqual(dozen.odds, 2)

  def test_column_init(self):
    """Check the constructor of Column-bet Outcome."""
    column = Column(3)
    self.assertEqual(column.name, "Column 3")
    self.assertEqual(column.odds, 2)

  def test_even_money_init(self):
    """Check the constructor of EvenMoney-bet Outcome."""
    even_money = EvenMoney("Red")
    self.assertEqual(even_money.name, "Red")
    self.assertEqual(even_money.odds, 1)

if __name__ == "__main__":
  unittest.main()
