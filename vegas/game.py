class Game(object):
  """A Game of roulette, allows Players to play rounds."""

  def __init__(self, table, wheel):
    """Constructor."""
    self.table = table
    self.wheel = wheel

  def cycle(self, player):
    """Play one round of roulette with the given Player."""

    def resolve_bets():
      """Resolve each Bet and notify the Player."""
      for bet in self.table.__iter__():
        if bet.outcome in winning_bin:
          player.win(bet)
        else:
          player.lose(bet)
      self.table.bets = []

    player.placeBets()
    self.table.isValid()
    winning_bin = self.wheel.next()
    resolve_bets()
