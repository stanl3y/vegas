from .bet import Bet


class Passenger57(object):
  """A simple Player (to be reworked later)."""

  def __init__(self, table, wheel):
    self.table = table
    self.black = wheel.getOutcome("Black")

  def placeBets(self):
    bet = Bet(1, self.black)
    self.table.placeBet(bet)

  def win(self, bet):
    print("Won ${} on {}".format(bet.amountBet, bet.outcome.__str__()))

  def lose(self, bet):
    print("Lost ${} on {}".format(bet.amountBet, bet.outcome.__str__()))
