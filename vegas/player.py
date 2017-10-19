class Player(object):
  """A roulette Player (abstract class)."""

  def __init__(self, table, verbose=False):
    """Constructor."""
    self.table = table
    self.stake = 100
    self.verbose = verbose

  def playing(self):
    """Assert whether the Player is still playing in the Game."""
    return (False if self.stake < self.table.minimum else True)

  def placeBets(self):
    """Place Bets on the Table (to be implemented in subclasses)."""
    pass

  def win(self, bet):
    """Process a Bet that was won."""
    self.stake += bet.winAmount()
    if self.verbose:
      print("Won ${} on {}".format(bet.amountBet, bet.outcome.__str__()))

  def lose(self, bet):
    """Process a Bet that was lost."""
    if self.verbose:
      print("Lost ${} on {}".format(bet.amountBet, bet.outcome.__str__()))
