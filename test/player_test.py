import unittest
from vegas.table import Table
from vegas.player import Player
from vegas.bet import Bet
from vegas.outcome import Outcome


##################### Shared Tests ##################################
"""The following 'test-methods' are called by subclasses of Player."""


def verify_winning_bets_update_stake(self, player):
  """Check a winning Bet increases Player's stake."""
  bet = Bet(5, Outcome("Jackpot", 7))
  old_stake = player.stake
  player.win(bet)
  self.assertEqual(player.stake - old_stake, bet.winAmount())


def verify_losing_bets_dont_change_stake(self, player):
  """Check a losing Bet does not change Player's stake."""
  # Note: the wagered money is deducted when the Bet is being placed.
  bet = Bet(5, Outcome("Smallpot", 3))
  old_stake = player.stake
  player.lose(bet)
  self.assertEqual(player.stake, old_stake)


def verify_stake_required_to_play(self, player):
  """A Player with stake below Table minimum should not be playing."""
  player.table = Table(10, 100)
  player.stake = 9
  self.assertFalse(self.player.playing())


def verify_player_should_save_table(self, player, table):
  """A Player should keep track of its Table upon initialization."""
  self.assertEqual(player.table, table)


class PlayerTest(unittest.TestCase):
  """A unit-test for the Player class."""

  def setUp(self):
    self.table = Table(0, 1)
    self.player = Player(self.table)

  def test_initialize(self):
    """The constructor should save all parameters correctly."""
    verify_player_should_save_table(self, self.player, self.table)

  def test_stake_required_to_play(self):
    """A player with stake less than table minimum should not be playing."""
    verify_stake_required_to_play(self, self.player)

  def test_winning_bets_update_stake(self):
    """A winning bet should increase Player's stake."""
    verify_winning_bets_update_stake(self, self.player)

  def test_losing_bets_dont_change_stake(self):
    """A losing Bet should not change Player's stake."""
    verify_losing_bets_dont_change_stake(self, self.player)


if __name__ == '__main__':
  unittest.main()
