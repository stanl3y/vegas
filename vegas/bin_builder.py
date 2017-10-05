from .outcomes import \
  Straight, Split, Street, Corner, FiveNumbers, Line, Dozen, Column, EvenMoney
from .bin import Bin


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
    self.assign_outcome(0, Straight(0))
    self.assign_outcome(37, Straight("00"))
    for i in range(1, 37):
      self.assign_outcome(i, Straight(i))

  def prepare_split_outcomes(self):
    """Populate TempBins with SplitOutcomes."""

    def assign_split_outcome(num1, num2):
      """Create and assign a SplitOutcome based on the two split-Bins."""
      outcome = Split(num1, num2)
      for bin in [num1, num2]:
        self.assign_outcome(bin, outcome)

    # generate vertical splits
    for num in range(1, 34):
      assign_split_outcome(num, num+3)
    # generate horizontal splits
    for row in range(12):
      assign_split_outcome(3*row+1, 3*row+2)
      assign_split_outcome(3*row+2, 3*row+3)

  def prepare_street_outcomes(self):
    """Populate TempBins with StreetOutcomes."""
    for row in range(12):
      outcome = Street(3*row+1)
      for bin in [3*row+1, 3*row+2, 3*row+3]:
        self.assign_outcome(bin, outcome)

  def prepare_corner_outcomes(self):
    """Populate TempBins with CornerOutcomes."""

    def assign_corner_outcome(upper_left):
      """Create and assign a CornerOutcome based on its upper_left corner."""
      nums = [upper_left, upper_left+1, upper_left+3, upper_left+4]
      outcome = Corner(upper_left)
      for bin in nums:
        self.assign_outcome(bin, outcome)

    for row in range(11):
      assign_corner_outcome(3*row + 1)
      assign_corner_outcome(3*row + 2)

  def prepare_five_numbers(self):
    """Populate TempBins with the FiveNumbersOutcome."""
    five_numbers = FiveNumbers()
    for bin in [37, 0, 1, 2, 3]:
      self.assign_outcome(bin, five_numbers)

  def prepare_line_outcomes(self):
    """Populate TempBins with LineOutcomes."""
    for row in range(11):
      outcome = Line(3*row+1)
      for bin in range(3*row+1, 3*row+7):
        self.assign_outcome(bin, outcome)

  def prepare_dozen_outcomes(self):
    """Populate TempBins with DozenOutcomes."""
    dozen1_pairs = [range(1, 13), Dozen(1)]
    dozen2_pairs = [range(13, 25), Dozen(2)]
    dozen3_pairs = [range(25, 37), Dozen(3)]
    for bins, outcome in [dozen1_pairs, dozen2_pairs, dozen3_pairs]:
      for bin in bins:
        self.assign_outcome(bin, outcome)

  def prepare_column_outcomes(self):
    """Populate TempBins with ColumnOutcomes."""
    column1 = Column(1)
    column2 = Column(2)
    column3 = Column(3)
    for row in range(12):
      self.assign_outcome(3*row+1, column1)
      self.assign_outcome(3*row+2, column2)
      self.assign_outcome(3*row+3, column3)

  def prepare_range_outcomes(self):
    """Populate TempBins with Low/High Outcomes."""
    low = EvenMoney("Low")
    high = EvenMoney("High")
    for outcome, bins in [[low, range(1, 19)], [high, range(19, 37)]]:
      for bin in bins:
        self.assign_outcome(bin, outcome)

  def prepare_colour_outcomes(self):
    """Populate TempBins with Red/Black Outcomes."""
    red = EvenMoney("Red")
    black = EvenMoney("Black")
    red_bins = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black_bins = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    for outcome, bins in [[red, red_bins], [black, black_bins]]:
      for bin in bins:
        self.assign_outcome(bin, outcome)

  def prepare_parity_outcomes(self):
    """Populate TempBins with Even/Odd Outcomes."""
    even = EvenMoney("Even")
    odd = EvenMoney("Odd")
    for i in range(18):
      self.assign_outcome(2*i+1, odd)
      self.assign_outcome(2*i+2, even)
