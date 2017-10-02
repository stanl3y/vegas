import unittest

from context import vegas
from vegas.bin import Bin
from vegas.outcome import Outcome


class BinTest(unittest.TestCase):
  """Tests for the Bin class."""

  def setUp(self):
    self.straight1 = Outcome("Straight 1", 35)
    self.straight2 = Outcome("Straight 2", 35)
    self.red = Outcome("Red", 1)
    self.black = Outcome("Black", 1)
    self.corner_bet = Outcome("Corner 1245", 8)

    self.bin1 = Bin({self.straight1, self.red, self.corner_bet})
    self.bin2 = Bin({self.straight2, self.black, self.corner_bet})

  def test_bin_membership(self):
    """Check Bins can hold Outcomes."""
    self.assertIn(self.straight1, self.bin1)
    self.assertIn(self.red, self.bin1)
    self.assertNotIn(self.straight2, self.bin1)

  def test_bins_can_share_outcomes(self):
    """Check a single Outcome can appear in multiple Bins."""
    self.assertIn(self.corner_bet, self.bin1)
    self.assertIn(self.corner_bet, self.bin2)

if __name__ == '__main__':
  unittest.main()
