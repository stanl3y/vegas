from functools import reduce
from .invalid_bet import InvalidBet


class Table(object):
  """A roulette table: a collection of Bets placed by a Player."""

  def __init__(self, minimum, limit):
    """Constructor."""
    self.bets = []
    self.minimum = minimum
    self.limit = limit

  def placeBet(self, bet):
    """Add the given Bet to the collection."""
    self.bets.append(bet)

  def __iter__(self):
    """Return an iterable of the Bets on the Table."""
    return self.bets.__iter__()

  def __str__(self):
    """A human-readable representation of the Table."""
    return ", ".join(map(lambda bet: bet.__str__(), self.bets))

  def __repr__(self):
    """A machine-readable representation of the Table."""
    return "Table({})".format(", ".join(map(lambda bet: bet.__repr__(), self.bets)))

  def isValid(self):
    """Check whether the Table isValid (see conditions below)."""
    if not self.bets:
      return True
    # each Bet must be greater or equal to the minimal bet
    for bet in self.bets:
      if bet.amountBet < self.minimum:
        raise InvalidBet
    # the sum of all Bets must be less or equal to the Table limit
    bet_amounts = map(lambda bet: bet.amountBet, self.bets)
    sum_of_bets = reduce(lambda x, y: x+y, bet_amounts)
    if sum_of_bets > self.limit:
      raise InvalidBet
    # all conditions met
    return True
