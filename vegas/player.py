import vegas.invalid_bet


class Player(object):
  """A roulette Player (abstract class)."""

  def __init__(self, table, verbose=False):
    """Constructor."""
    self.table = table
    self.stake = 100
    self.roundsToGo = 1
    self.verbose = verbose

  def setStake(self, stake):
    """Set Player's stake to be the given amount."""
    self.stake = stake

  def setRounds(self, rounds):
    """Set Player's stake to be the given number."""
    self.roundsToGo = rounds

  def playing(self):
    """Assert whether the Player is still playing in the Game."""
    halts = [
      self.stake < self.table.minimum,
      self.roundsToGo == 0
    ]
    return (False if any(halts) else True)

  def placeBets(self):
    """Place Bets on the Table (to be implemented in subclasses)."""
    pass

  def _place_bet(self, bet):
    """Process placing a Bet (checks and stake updates)."""
    if (self.stake - bet.amountBet) < 0:
      raise vegas.invalid_bet.InvalidBet
    self.stake -= bet.amountBet
    self.table.placeBet(bet)

  def win(self, bet):
    """Process a Bet that was won."""
    self.stake += bet.winAmount()
    if self.verbose:
      print("Won ${} on {}".format(bet.amountBet, bet.outcome.__str__()))

  def lose(self, bet):
    """Process a Bet that was lost."""
    if self.verbose:
      print("Lost ${} on {}".format(bet.amountBet, bet.outcome.__str__()))
