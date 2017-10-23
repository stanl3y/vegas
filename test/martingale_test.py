import unittest
from unittest.mock import Mock
from vegas.martingale import Martingale
from vegas.outcome import Outcome
import test.player_test


class MartingaleTest(unittest.TestCase):
  """A unit-test for the Martingale class."""

  def setUp(self):
    self.table = Mock()
    self.wheel = Mock()
    self.wheel.getOutcome = lambda outcome: Outcome(outcome, 1)
    self.player = Martingale(self.table, self.wheel)

  def test_initialize(self):
    """The constructor should save all parameters correctly."""
    test.player_test.test_player_should_save_table(self, self.player, self.table)

  def test_stake_setter(self):
    """It should be possible to set Martingale's stake."""
    test.player_test.test_stake_setter(self, self.player)

  def test_rounds_setter(self):
    """It should be possible to set Martingale's roundsToGo."""
    test.player_test.test_roundsToGo_setter(self, self.player)

  ########### Martingale.playing ################################

  def test_stake_required_to_play(self):
    """A Martingale-player below the Table minimum should not be playing."""
    test.player_test.test_stake_required_to_play(self, self.player)

  def test_not_playing_if_no_rounds_left(self):
    """A Martingale should not be playing if there are no roundsToGo left."""
    test.player_test.test_not_playing_if_no_rounds_left(self, self.player)

  ########### Stake Handling #####################################

  def test_stake_to_place_bet(self):
    """A Martingale needs enough stake to place a Bet."""
    test.player_test.test_stake_to_place_bet(self, self.player)

  def test_placing_bet_reduces_stake(self):
    """Placing a Bet reduces Martingale's stake."""
    test.player_test.test_placing_bet_reduces_stake(self, self.player)

  def test_winning_bets_update_stake(self):
    """A winning bet should update Martingale-player's stake."""
    test.player_test.test_winning_bets_update_stake(self, self.player)

  def test_losing_bets_dont_change_stake(self):
    """A losing Bet should not change Martingale-player's stake."""
    test.player_test.test_losing_bets_dont_change_stake(self, self.player)

  ######################## Betting System #################################

  def place_bet(self, player):
    """Let the given Player place a Bet."""
    self.player.placeBets()
    placed_bet = player.table.placeBet.call_args[0][0]
    return placed_bet

  def win_a_bet(self, player):
    """Let the given Player win a Bet."""
    placed_bet = self.place_bet(player)
    player.win(placed_bet)
    return placed_bet

  def lose_a_bet(self, player):
    """Let the given Player lose a bet."""
    placed_bet = self.place_bet(player)
    player.lose(placed_bet)
    return placed_bet

  def test_base_amount(self):
    """A Martingale-player should start betting at their base level."""
    placed_bet = self.place_bet(self.player)
    self.assertEqual(placed_bet.amountBet, self.player.base_amount)

  def test_reset_amount_after_each_win(self):
    """A Martingale-player should reset the amount-bet after each win."""
    for i in range(7):
      self.win_a_bet(self.player)
    new_bet = self.place_bet(self.player)
    self.assertEqual(new_bet.amountBet, self.player.base_amount)

  def test_double_amount_after_each_loss(self):
    """A Martingale-player should double the amount-bet after each loss."""
    for i in range(3):
      self.lose_a_bet(self.player)
    new_bet = self.place_bet(self.player)
    self.assertEqual(new_bet.amountBet, 8*self.player.base_amount)

  def test_reset_amount_after_each_win2(self):
    """A Martingale-player should reset the amount-bet after each win."""
    for i in range(4):
      self.lose_a_bet(self.player)
    fifth_bet = self.win_a_bet(self.player)
    self.assertEqual(fifth_bet.amountBet, 16)  # sanity check
    new_bet = self.place_bet(self.player)
    self.assertEqual(new_bet.amountBet, self.player.base_amount)


if __name__ == "__main__":
  unittest.main()
