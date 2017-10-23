import unittest
from vegas.table import Table
from vegas.player import Player
from vegas.bet import Bet
from vegas.outcome import Outcome
from vegas.invalid_bet import InvalidBet


#####################################################################
##################### Shared Tests ##################################
#####################################################################
"""The following 'test-methods' are called by subclasses of Player."""


################# Stake Handling ###################################


def test_stake_to_place_bet(self, player):
  """A Player needs enough stake to place a Bet."""
  player.stake = 0
  bet = Bet(1, Outcome("Black", 1))
  self.assertRaises(InvalidBet, player._place_bet, bet)


def test_placing_bet_reduces_stake(self, player):
  """Placing a Bet should reduce Player's stake."""
  old_stake = player.stake
  player.placeBets()
  placed_bet = self.player.table.placeBet.call_args[0][0]
  self.assertTrue(placed_bet.amountBet > 0)
  self.assertEqual(old_stake - self.player.stake, placed_bet.amountBet)


def test_winning_bets_update_stake(self, player):
  """Check a winning Bet increases Player's stake."""
  bet = Bet(5, Outcome("Jackpot", 7))
  old_stake = player.stake
  player.win(bet)
  self.assertEqual(player.stake - old_stake, bet.winAmount())


def test_losing_bets_dont_change_stake(self, player):
  """Check a losing Bet does not change Player's stake."""
  # Note: the wagered money is deducted when the Bet is being placed.
  bet = Bet(5, Outcome("Smallpot", 3))
  old_stake = player.stake
  player.lose(bet)
  self.assertEqual(player.stake, old_stake)


################# Player.playing() #################################


def test_stake_required_to_play(self, player):
  """A Player with stake below Table minimum should not be playing."""
  player.table = Table(10, 100)
  player.stake = 9
  self.assertFalse(player.playing())


def test_not_playing_if_no_rounds_left(self, player):
  """A Player should not be playing if there are no roundsToGo left."""
  player.table = Table(0, 1)
  player.roundsToGo = 0
  self.assertFalse(player.playing())


############### Initilization & Setters ############################


def test_player_should_save_table(self, player, table):
  """A Player should keep track of its Table upon initialization."""
  self.assertEqual(player.table, table)


def test_stake_setter(self, player):
  """It should be possible to set Player's stake."""
  player.setStake(42)
  self.assertEqual(player.stake, 42)


def test_roundsToGo_setter(self, player):
  """It should be possible to set Player's roundsToGo."""
  player.setRounds(73)
  self.assertEqual(player.roundsToGo, 73)


#####################################################################
##################### Player Test ###################################
#####################################################################

class PlayerTest(unittest.TestCase):
  """A unit-test for the Player class."""

  def setUp(self):
    self.table = Table(0, 1)
    self.player = Player(self.table)

  def test_initialize(self):
    """The constructor should save all parameters correctly."""
    test_player_should_save_table(self, self.player, self.table)

  def test_stake_setter(self):
    """It should be possible to set Player's stake."""
    test_stake_setter(self, self.player)

  def test_rounds_setter(self):
    """It should be possible to set Player's roundsToGo."""
    test_roundsToGo_setter(self, self.player)

  #################### Player.playing #################################

  def test_stake_required_to_play(self):
    """A player with stake less than table minimum should not be playing."""
    test_stake_required_to_play(self, self.player)

  def test_not_playing_if_no_rounds_left(self):
    """A Player should not be playing if there are no roundsToGo left."""
    test_not_playing_if_no_rounds_left(self, self.player)

  ##################### Stake Handling #################################

  def stake_to_place_bet(self):
    """Player needs enough stake to place a Bet."""
    test_stake_to_place_bet(self, self.player)

  def test_winning_bets_update_stake(self):
    """A winning bet should increase Player's stake."""
    test_winning_bets_update_stake(self, self.player)

  def test_losing_bets_dont_change_stake(self):
    """A losing Bet should not change Player's stake."""
    test_losing_bets_dont_change_stake(self, self.player)


if __name__ == '__main__':
  unittest.main()
