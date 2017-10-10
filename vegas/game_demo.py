from .passenger57 import Passenger57
from .wheel import Wheel
from .table import Table
from .game import Game


class GameDemo(object):
  """A demonstration of the roulette Game."""

  def main(self):
    """Play four rounds of roulette with a simple Player."""
    # initialize
    wheel = Wheel()
    table = Table(1, 10)
    game = Game(table, wheel)
    player = Passenger57(table, wheel)
    # simulate play
    spins_count = 4
    for i in range(spins_count):
      game.cycle(player)

if __name__ == '__main__':
  GameDemo.main()
