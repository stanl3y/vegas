from unittest.mock import Mock
import unittest

from context import vegas
from vegas.outcomes import Straight
from vegas.wheel import Wheel


class GIVEN_Wheel_WHEN_Next_THEN_random_choice(unittest.TestCase):
  def setUp(self):
    self.wheel = Wheel()

  def test_rng(self):
    """Check that Wheel.next() returns a 'random' Bin."""
    next_bins = [1, 2, 5]
    # prepare a mock random-number generator
    self.wheel.rng = mock_rng = Mock()
    mock_rng.next_bins = next_bins[:]
    mock_rng.choice = lambda bins: bins[mock_rng.next_bins.pop(0)]
    # test the bins from spin (determined uniquely by their Straight Outcome)
    for num in next_bins:
      self.assertIn(Straight(num), self.wheel.next())

if __name__ == '__main__':
  unittest.main()
