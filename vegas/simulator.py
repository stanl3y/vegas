import sys
from vegas.table import Table
from vegas.wheel import Wheel
from vegas.game import Game
from vegas.martingale import Martingale
from vegas.invalid_bet import InvalidBet


class Simulator(object):

  def __init__(self, game, player):
    """Constructor."""
    self.game = game
    self.player = player
    self.initDuration = 250
    self.initStake = 100
    self.samples = 12

  def gather(self):
    """Run Sessions, collect durations & maxima in each."""
    self.durations = []
    self.maxima = []
    for _ in range(self.samples):
      stakes = self.session()
      self.durations.append(len(stakes))
      self.maxima.append(max(stakes) if stakes else None)

  def session(self):
    """Run a Game-Session with the given Player and init-values."""
    stakes = []
    self.player.reset()
    self.player.setRounds(self.initDuration)
    self.player.stake = self.initStake
    while self.player.playing():
      try:
        self.game.cycle(self.player)
        stakes.append(self.player.stake)
        self.player.setRounds(self.player.roundsToGo - 1)
      except InvalidBet:
        return stakes
    return stakes


def main(argv=None):
  """Application main function: setup a simulation, print results."""
  table = Table(1, 100)
  wheel = Wheel()
  game = Game(table, wheel)
  player = Martingale(table, wheel)
  sim = Simulator(game, player)
  sim.gather()
  print("durations", sim.durations, "\n", "maxima", sim.maxima)


if __name__ == '__main__':
  main(sys.argv)
