from .outcome import Outcome


class Straight(Outcome):
  """An Outcome of a Straight bet (determined by the Bin number)."""
  def __init__(self, bin_num):
    self.name = "Straight {}".format(bin_num)
    self.odds = 35


class Split(Outcome):
  """An Outcome of a Split bet (determined by the two Bin numbers)."""
  def __init__(self, bin_num1, bin_num2):
    self.name = "Split {}-{}".format(*sorted([bin_num1, bin_num2]))
    self.odds = 17


class Street(Outcome):
  """An Outcome of a Street bet (determined by the left-most Bin number)."""
  def __init__(self, upper_left):
    bins = [upper_left, upper_left+1, upper_left+2]
    self.name = "Street {}-{}-{}".format(*bins)
    self.odds = 11


class Corner(Outcome):
  """An Outcome of a Corner bet (determined by the upper-left corner)."""
  def __init__(self, upper_left):
    bins = [upper_left, upper_left+1, upper_left+3, upper_left+4]
    self.name = "Corner {}-{}-{}-{}".format(*bins)
    self.odds = 8


class FiveNumbers(Outcome):
  """The FiveNumbers Outcome."""
  def __init__(self):
    self.name = "Five Numbers"
    self.odds = 6


class Line(Outcome):
  """An Outcome of a Line bet (determined by the upper-left corner)."""
  def __init__(self, upper_left):
    bins = list(range(upper_left, upper_left+6))
    self.name = "Line {}-{}-{}-{}-{}-{}".format(*bins)
    self.odds = 5


class Dozen(Outcome):
  """An Outcome of a Dozen bet (determined by its number (1, 2 or 3))."""
  def __init__(self, dozen_num):
    self.name = "Dozen {}".format(dozen_num)
    self.odds = 2


class Column(Outcome):
  """An Outcome of a Column bet (determined by its number (1, 2 or 3))."""
  def __init__(self, column_num):
    self.name = "Column {}".format(column_num)
    self.odds = 2


class EvenMoney(Outcome):
  """An Outcome of an EvenMoney bet (determined by its name)."""
  def __init__(self, name):
    self.name = name
    self.odds = 1
