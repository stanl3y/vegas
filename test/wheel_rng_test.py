import unittest

from context import vegas
from vegas.outcome import Outcome
from vegas.wheel import Wheel


class GIVEN_Wheel_WHEN_Next_THEN_random_choice(unittest.TestCase):
  def setUp(self):
    self.wheel = Wheel()
    self.wheel.rng.seed(2)  # [3, 5, 5, 23, 10, 19, 16, 13, 2, 37]

  def test_rng(self):
    red = Outcome("Red", 1)
    straight3 = Outcome("Straight 3", 35)
    straight5 = Outcome("Straight 5", 35)
    corner_bet = Outcome("Corner 1245", 8)
    self.wheel.addOutcome(3, straight3)
    self.wheel.addOutcome(3, red)
    self.wheel.addOutcome(5, straight5)
    self.wheel.addOutcome(5, red)
    self.wheel.addOutcome(5, corner_bet)

    current_bin = self.wheel.next()  # Bin 3
    self.assertIn(straight3, current_bin)
    current_bin = self.wheel.next()  # Bin 5
    self.assertIn(straight5, current_bin)
    current_bin = self.wheel.next()  # Bin 5 again
    self.assertEqual(len(current_bin), 3)

if __name__ == '__main__':
  unittest.main()
