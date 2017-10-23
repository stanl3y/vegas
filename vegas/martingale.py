from .player import Player
from .bet import Bet


class Martingale(Player):
  """A roulette Player using the Martingale strategy."""

  def __init__(self, table, wheel, verbose=False):
    """Constructor."""
    super().__init__(table, verbose)
    self.base_amount = 1
    self.black = wheel.getOutcome("Black")
    self.lossCount = 0
    self.betMultiple = 1

  def current_bet_amount(self):
    """Current amount to bet, based on recent wins and losses."""
    return self.betMultiple * self.base_amount

  def placeBets(self):
    """Place bets according to the Martingale strategy."""
    bet = Bet(self.current_bet_amount(), self.black)
    self._place_bet(bet)

  def win(self, bet):
    """Process a Bet that was won."""
    super().win(bet)
    self.lossCount = 0
    self.betMultiple = 1

  def lose(self, bet):
    """Process a Bet that was lost."""
    super().lose(bet)
    self.lossCount += 1
    self.betMultiple *= 2

  def reset(self):
    """Reset the Player for the next Session in Simulation."""
    self.lossCount = 0
    self.betMultiple = 1
