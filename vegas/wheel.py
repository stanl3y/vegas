import random
from .bin_builder import BinBuilder


class Wheel(object):
  """A roulette wheel: contains Bins and simulates the spin."""

  def __init__(self):
    """Initialize the Wheel and populate Bins with Outcomes.

    The correspondence between range(38) and Bins is as follows:
      0  ~ Bin 0
      37 ~ Bin 00
      i  ~ Bin i  for 1 <= i <= 36
    """
    bin_builder = BinBuilder()
    self.bins = bin_builder.buildBins()
    self.all_outcomes = bin_builder.temp_outcomes
    self.rng = random.Random()

  def get(self, bin_ind):
    """Accessor: return the requested Bin."""
    return self.bins[bin_ind]

  def next(self):
    """Roulette spin: choose a random Bin of the Wheel."""
    return self.rng.choice(self.bins)

  def getOutcome(self, name):
    """The string-to-Outcome mapping."""
    return self.all_outcomes[name]
