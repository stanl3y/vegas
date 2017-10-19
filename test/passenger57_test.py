import unittest
from unittest.mock import Mock
from vegas.passenger57 import Passenger57
import test.player_test


class Passenger57Test(unittest.TestCase):
  """A unit-test for the Passenger57 class."""

  def setUp(self):
    self.black = "the-black-outcome"
    self.table = Mock()
    self.wheel = Mock()
    self.wheel.getOutcome.return_value = self.black
    self.player = Passenger57(self.table, self.wheel)

  def test_initialize(self):
    """The constructor should save all parameters correctly."""
    test.player_test.verify_player_should_save_table(self, self.player, self.table)

  def test_stake_required_to_play(self):
    """A Passenger57 below the Table minimum should not be playing."""
    test.player_test.verify_stake_required_to_play(self, self.player)

  def test_winning_bets_update_stake(self):
    """A winning bet should update Passenger57's stake."""
    test.player_test.verify_winning_bets_update_stake(self, self.player)

  def test_losing_bets_dont_change_stake(self):
    """A losing Bet should not change Passenger57's stake."""
    test.player_test.verify_losing_bets_dont_change_stake(self, self.player)

  ###################### Betting System ###################################
  def test_always_place_on_black(self):
    """A Passenger57 should always bet on Black."""
    self.player.placeBets()
    placed_bet = self.table.placeBet.call_args[0][0]
    self.assertEqual(placed_bet.outcome, self.black)
    self.assertTrue(placed_bet.amountBet > 0)


if __name__ == '__main__':
    unittest.main()
