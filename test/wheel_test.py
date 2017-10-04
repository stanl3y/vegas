import unittest

from context import vegas
from vegas.wheel import Wheel
from vegas.outcome import Outcome
from vegas.roulette import Roulette


class WheelTest(unittest.TestCase):
  """Tests for the Wheel class."""

  def setUp(self):
    self.wheel = Wheel()

  def test_wheel_initialization(self):
    """Integration test for BinBuilder."""
    # the Wheel should have 38 bins
    self.assertEqual(len(self.wheel.bins), 38)
    # Bin 23 should hold 17 Outcomes, in particular..
    self.assertEqual(len(self.wheel.get(23)), 17)
    bin23_sample_outcomes = [
      Outcome("Straight 23", Roulette.StraightBet),
      Outcome("Split 20-23", Roulette.SplitBet),
      Outcome("Street 8", Roulette.StreetBet)
    ]
    for outcome in bin23_sample_outcomes:
      self.assertIn(outcome, self.wheel.get(23))

if __name__ == "__main__":
  unittest.main()
