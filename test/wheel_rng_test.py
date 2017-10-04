import unittest

from context import vegas
from vegas.outcome import Outcome
from vegas.wheel import Wheel


class GIVEN_Wheel_WHEN_Next_THEN_random_choice(unittest.TestCase):
  def setUp(self):
    self.wheel = Wheel()
    # set the initial seed so that we have predictable 'random' Bins
    # with seed of 2, rng.randint(0,37) yields [3, 5, 5, 23, 10, 19..]
    self.wheel.rng.seed(2)

  def test_rng(self):
    """Check that Wheel.next() returns a 'random' Bin."""
    straight3 = Outcome("Straight 3", 35)
    straight5 = Outcome("Straight 5", 35)
    current_bin = self.wheel.next()  # Bin 3
    self.assertIn(straight3, current_bin)
    current_bin = self.wheel.next()  # Bin 5
    self.assertIn(straight5, current_bin)
    current_bin = self.wheel.next()  # Bin 5 again
    self.assertIn(straight5, current_bin)

if __name__ == '__main__':
  unittest.main()
