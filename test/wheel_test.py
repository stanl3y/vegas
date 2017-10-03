import unittest

from context import vegas
from vegas.wheel import Wheel
from vegas.outcome import Outcome
from vegas.bin import Bin


class WheelTest(unittest.TestCase):
  """Tests for the Wheel class."""

  def setUp(self):
    self.wheel = Wheel()

  def test_constructor(self):
    """Check the Wheel is initialized with 38 (empty) Bins."""
    self.assertEqual(len(self.wheel.bins), 38)
    self.assertIsInstance(self.wheel.bins[0], Bin)
    self.assertIsInstance(self.wheel.bins[37], Bin)

  def test_addOutcome(self):
    """Check Outcomes can be added to Bins."""
    outcome = Outcome("Red", 1)
    self.assertNotIn(outcome, self.wheel.get(0))
    self.wheel.addOutcome(0, outcome)
    self.assertIn(outcome, self.wheel.get(0))

if __name__ == "__main__":
  unittest.main()
