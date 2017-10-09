class Bet(object):
  """An instance of a particular bet (money on Outcome)."""

  def __init__(self, amount, outcome):
    """Constructor."""
    if amount < 0:
      raise ValueError
    self.amountBet = amount
    self.outcome = outcome

  def __str__(self):
    """Human-readable representation of the Bet."""
    return "{} on {}".format(self.amountBet, self.outcome.__str__())

  def __repr__(self):
    """Machine-readable representation of the Bet."""
    return "Bet({}, {})".format(self.amountBet, self.outcome.__repr__())

  def winAmount(self):
    """Amount of money won if Bet successful."""
    return self.amountBet + self.outcome.winAmount(self.amountBet)

  def loseAmount(self):
    """Amount of money lost (positive) if Bet unsuccessful."""
    return self.amountBet
