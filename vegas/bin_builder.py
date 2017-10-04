from .outcome import Outcome
from .bin import Bin
from .roulette import Roulette


class BinBuilder(object):
  """Builder: populate Bins of a Wheel with Outcomes."""

  def __init__(self):
    """Constructor: assign Outcomes to a collection of TempBins."""
    self.temp_bins = tuple(set() for i in range(38))
    self.prepare_temp_bins()

  def buildBins(self):
    """Build a collection of (final) Bins with Outcomes."""
    return tuple(Bin(self.temp_bins[i]) for i in range(38))

  def prepare_temp_bins(self):
    """Populate TempBins with various types of Outcomes."""
    # inside bets
    self.prepare_straight_outcomes()
    self.prepare_split_outcomes()
    self.prepare_street_outcomes()
    self.prepare_corner_outcomes()
    self.prepare_five_numbers()
    self.prepare_line_outcomes()
    # outside bets
    self.prepare_dozen_outcomes()
    self.prepare_column_outcomes()
    self.prepare_range_outcomes()
    self.prepare_colour_outcomes()
    self.prepare_parity_outcomes()

  def assign_outcome(self, bin, outcome):
    """Assign a given Outcome to a given Bin."""
    self.temp_bins[bin].add(outcome)

  ################### Prepare Individual Bets ################################

  def prepare_straight_outcomes(self):
    """Populate TempBins with StraightOutcomes."""
    self.assign_outcome(0, Outcome("Straight 0", Roulette.StraightBet))
    self.assign_outcome(37, Outcome("Straight 00", Roulette.StraightBet))
    for i in range(1, 37):
      self.assign_outcome(i, Outcome("Straight {}".format(i), Roulette.StraightBet))

  def prepare_split_outcomes(self):
    """Populate TempBins with SplitOutcomes."""

    def create_split_outcome(num1, num2):
      """Create and assign a SplitOutcome based on the two split-Bins."""
      outcome = Outcome("Split {}-{}".format(num1, num2), Roulette.SplitBet)
      for bin in [num1, num2]:
        self.assign_outcome(bin, outcome)

    # generate vertical splits
    for num in range(1, 34):
      create_split_outcome(num, num+3)
    # generate horizontal splits
    for row in range(12):
      create_split_outcome(3*row+1, 3*row+2)
      create_split_outcome(3*row+2, 3*row+3)

  def prepare_street_outcomes(self):
    """Populate TempBins with StreetOutcomes."""
    for row in range(12):
      outcome = Outcome("Street {}".format(row+1), Roulette.StreetBet)
      for bin in [3*row+1, 3*row+2, 3*row+3]:
        self.assign_outcome(bin, outcome)

  def prepare_corner_outcomes(self):
    """Populate TempBins with CornerOutcomes."""

    def create_corner_outcome(upper_left):
      """Create and assign a CornerOutcome based on its upper_left corner."""
      nums = [upper_left, upper_left+1, upper_left+3, upper_left+4]
      outcome = Outcome("Corner {}-{}-{}-{}".format(*nums), Roulette.CornerBet)
      for bin in nums:
        self.assign_outcome(bin, outcome)

    for row in range(11):
      create_corner_outcome(3*row + 1)
      create_corner_outcome(3*row + 2)

  def prepare_five_numbers(self):
    """Populate TempBins with the FiveNumbersOutcome."""
    five_numbers = Outcome("Five numbers", Roulette.FiveNumbers)
    for bin in [37, 0, 1, 2, 3]:
      self.assign_outcome(bin, five_numbers)

  def prepare_line_outcomes(self):
    """Populate TempBins with LineOutcomes."""
    for row in range(11):
      outcome = Outcome("Line {}-{}".format(row+1, row+2), Roulette.LineBet)
      for bin in range(3*row+1, 3*row+7):
        self.assign_outcome(bin, outcome)

  def prepare_dozen_outcomes(self):
    """Populate TempBins with DozenOutcomes."""
    dozen1 = [Outcome("First 12", Roulette.EvenMoneyBet), range(1, 13)]
    dozen2 = [Outcome("Second 12", Roulette.EvenMoneyBet), range(13, 25)]
    dozen3 = [Outcome("Third 12", Roulette.EvenMoneyBet), range(25, 37)]
    for outcome, bins in [dozen1, dozen2, dozen3]:
      for bin in bins:
        self.assign_outcome(bin, outcome)

  def prepare_column_outcomes(self):
    """Populate TempBins with ColumnOutcomes."""
    column1 = Outcome("Column 1", Roulette.ColumnBet)
    column2 = Outcome("Column 2", Roulette.ColumnBet)
    column3 = Outcome("Column 3", Roulette.ColumnBet)
    for row in range(12):
      self.assign_outcome(3*row+1, column1)
      self.assign_outcome(3*row+2, column2)
      self.assign_outcome(3*row+3, column3)

  def prepare_range_outcomes(self):
    """Populate TempBins with Low/High Outcomes."""
    low = Outcome("Low", Roulette.EvenMoneyBet)
    high = Outcome("High", Roulette.EvenMoneyBet)
    for outcome, bins in [[low, range(1, 19)], [high, range(19, 37)]]:
      for bin in bins:
        self.assign_outcome(bin, outcome)

  def prepare_colour_outcomes(self):
    """Populate TempBins with Red/Black Outcomes."""
    red = Outcome("Red", Roulette.EvenMoneyBet)
    black = Outcome("Black", Roulette.EvenMoneyBet)
    red_bins = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black_bins = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    for outcome, bins in [[red, red_bins], [black, black_bins]]:
      for bin in bins:
        self.assign_outcome(bin, outcome)

  def prepare_parity_outcomes(self):
    """Populate TempBins with Even/Odd Outcomes."""
    even = Outcome("Even", Roulette.EvenMoneyBet)
    odd = Outcome("Odd", Roulette.EvenMoneyBet)
    for i in range(18):
      self.assign_outcome(2*i+1, odd)
      self.assign_outcome(2*i+2, even)
