import random
from .bin import Bin


class Wheel(object):
  """A roulette wheel: contains Bins and simulates the spin."""

  def __init__(self):
    """Constructor (to be fully implemented later).

    The correspondence between range(38) and Bins is as follows:
      0  ~ Bin 0
      37 ~ Bin 00
      i  ~ Bin i  for 1 <= i <= 36
    """
    self.bins = tuple(Bin() for i in range(38))
    self.rng = random.Random()

  def get(self, bin_ind):
    """Accessor: return the requested Bin."""
    return self.bins[bin_ind]

  def addOutcome(self, bin_ind, outcome):
    """Add a given Outcome to a given Bin."""
    self.bins[bin_ind].add(outcome)

  def next(self):
    """Roulette spin: choose a random Bin of the Wheel."""
    return self.rng.choice(self.bins)
