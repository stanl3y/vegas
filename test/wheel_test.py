import unittest

from context import vegas
from vegas.wheel import Wheel
from vegas.outcomes import Straight, Split, Street


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
      Straight(23),
      Split(20, 23),
      Street(22)
    ]
    for outcome in bin23_sample_outcomes:
      self.assertIn(outcome, self.wheel.get(23))

if __name__ == "__main__":
  unittest.main()
