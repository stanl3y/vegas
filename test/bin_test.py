import unittest

from vegas.bin import Bin
from vegas.outcome import Outcome
from vegas.outcomes import Straight, Corner, EvenMoney


class BinTest(unittest.TestCase):
  """Tests for the Bin class."""

  def setUp(self):
    self.straight1 = Straight(1)
    self.straight2 = Straight(2)
    self.red = EvenMoney("Red")
    self.black = EvenMoney("Black")
    self.corner_bet = Corner(1)

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
