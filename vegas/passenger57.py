from .bet import Bet
from .player import Player


class Passenger57(Player):
  """A simple Player that always places a bet on Black."""

  def __init__(self, table, wheel, verbose=False):
    """Constructor."""
    super().__init__(table, verbose)
    self.black = wheel.getOutcome("Black")

  def placeBets(self):
    """Place bets according to the Passenger57 strategy."""
    bet = Bet(1, self.black)
    self._place_bet(bet)
