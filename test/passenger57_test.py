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
    test.player_test.test_player_should_save_table(self, self.player, self.table)

  def test_stake_setter(self):
    """It should be possible to set Passenger57's stake."""
    test.player_test.test_stake_setter(self, self.player)

  def test_rounds_setter(self):
    """It should be possible to set Passenger57's roundsToGo."""
    test.player_test.test_roundsToGo_setter(self, self.player)

  #################### Passenger57.playing ###############################

  def test_stake_required_to_play(self):
    """A Passenger57 below the Table minimum should not be playing."""
    test.player_test.test_stake_required_to_play(self, self.player)

  def test_not_playing_if_no_rounds_left(self):
    """A Passenger57 should not be playing if there are no roundsToGo left."""
    test.player_test.test_not_playing_if_no_rounds_left(self, self.player)

  #################### Stake Handling  ###################################

  def test_stake_to_place_bet(self):
    """Passenger57 needs enough stake to place a Bet."""
    test.player_test.test_stake_to_place_bet(self, self.player)

  def test_placing_bet_reduces_stake(self):
    """Placing a Bet reduces Passenger57's stake."""
    test.player_test.test_placing_bet_reduces_stake(self, self.player)

  def test_winning_bets_update_stake(self):
    """A winning bet should update Passenger57's stake."""
    test.player_test.test_winning_bets_update_stake(self, self.player)

  def test_losing_bets_dont_change_stake(self):
    """A losing Bet should not change Passenger57's stake."""
    test.player_test.test_losing_bets_dont_change_stake(self, self.player)

  ###################### Betting System ###################################

  def test_always_place_on_black(self):
    """A Passenger57 should always bet on Black."""
    self.player.placeBets()
    placed_bet = self.table.placeBet.call_args[0][0]
    self.assertEqual(placed_bet.outcome, self.black)
    self.assertTrue(placed_bet.amountBet > 0)


if __name__ == '__main__':
    unittest.main()
