import unittest
from unittest.mock import Mock, MagicMock
from vegas.game import Game
from vegas.table import Table
from vegas.bet import Bet
from vegas.outcomes import EvenMoney


class GameTest(unittest.TestCase):
  """Unit test for the Game class."""

  def setUp(self):
    self.bet = Bet(1, EvenMoney("Black"))
    self.mock_player = Mock()
    self.table = Table(0, 1)
    self.mock_wheel = Mock()
    self.mock_wheel.next.return_value = set()
    self.game = Game(self.table, self.mock_wheel)

  def test_initialize(self):
    """The constructor should save all parameters correctly."""
    self.assertEqual(self.game.table, self.table)
    self.assertEqual(self.game.wheel, self.mock_wheel)

  def test_player_playing(self):
    """Game should not run, if Player not playing."""
    player = Mock()
    player.playing.return_value = False
    self.game.cycle(player)
    player.placeBets.assert_not_called()

  def test_game_cycle(self):
    """Each round of roulette should follow a given procedure."""
    # initialize
    mock_table = MagicMock()
    player = self.mock_player
    game = Game(mock_table, self.mock_wheel)
    # test
    game.cycle(player)
    player.playing.assert_called()
    player.placeBets.assert_called()
    game.table.isValid.assert_called()
    game.wheel.next.assert_called()

  def test_bets_are_emptied(self):
    """A Table should hold no Bets at the end of each round."""
    table = self.table
    table.bets = [self.bet]
    game = Game(table, self.mock_wheel)
    game.cycle(self.mock_player)
    self.assertEqual(len(table.bets), 0)

############## Bet Notifications to Player ######################

  def play_one_round(self, placed_bet, winning_bin, player):
    """Play one round of roulette, rolling the given bin."""
    self.table.bets = [placed_bet]
    self.mock_wheel.next.return_value = winning_bin
    game = Game(self.table, self.mock_wheel)
    game.cycle(player)

  def test_resolve_winning_bet(self):
    """The Game should notify a Player of any winning bets."""
    winning_bet = self.bet
    # winning_bin contains the Outcome of the winning_bet
    winning_bin = set([winning_bet.outcome])
    self.play_one_round(winning_bet, winning_bin, self.mock_player)
    self.mock_player.win.assert_called_with(winning_bet)

  def test_resolve_losing_bet(self):
    """The Game should notify a Player of any losing bets."""
    losing_bet = self.bet
    # winning_bin does not contain the Outcome of the losing_bet
    winning_bin = set()
    self.play_one_round(losing_bet, winning_bin, self.mock_player)
    self.mock_player.lose.assert_called_with(losing_bet)

if __name__ == '__main__':
  unittest.main()
