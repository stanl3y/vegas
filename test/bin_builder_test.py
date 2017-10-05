import unittest

from context import vegas
from vegas.bin_builder import BinBuilder
from vegas.outcome import Outcome
from vegas.outcomes import \
  Straight, Split, Street, Corner, FiveNumbers, Line, Dozen, Column, EvenMoney


class BinBuilderTest(unittest.TestCase):
  """Tests for the BinBuilder class."""

  def setUp(self):
    self.bin_builder = BinBuilder()

  def check_bins(self, expect_pairings):
    """Check the given Bin-Outcome pairings.

    Given a list of expected pairings [ (Bin_ind, Outcome), ... ],
    check that each Outcome is in the Bin numbered by Bin_ind.
    """
    for bin, outcome in expect_pairings:
      self.assertIn(outcome, self.bin_builder.temp_bins[bin])

  #################### Test Individual Bets ###################################

  def test_straight_outcomes(self):
    """Check that the StraightOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_straight_outcomes()
    expectations = [(37, Straight("00"))]
    expectations.extend([(i, Straight(i)) for i in [0, 1, 2, 36]])
    self.check_bins(expectations)

  def test_split_outcomes(self):
    """Check that SplitOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_split_outcomes()
    expectations = [
      # Bin1 1: start corner
      (1, Split(1, 2)),
      (1, Split(1, 4)),
      # Bin 2: start side
      (2, Split(1, 2)),
      (2, Split(2, 5)),
      (2, Split(2, 3)),
      # Bin 3: start corner right
      (3, Split(2, 3)),
      (3, Split(3, 6)),
      # Bin 19: middle side
      (19, Split(16, 19)),
      (19, Split(19, 20)),
      (19, Split(19, 22)),
      # Bin 29: middle
      (29, Split(26, 29)),
      (29, Split(28, 29)),
      (29, Split(29, 30)),
      (29, Split(29, 32)),
      # Bin 36: end
      (36, Split(33, 36)),
      (36, Split(35, 36)),
    ]
    self.check_bins(expectations)

  def test_street_outcomes(self):
    """Check that StreetOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_street_outcomes()
    street1 = Street(1)
    street4 = Street(4)
    street34 = Street(34)
    expectations = []
    expectations.extend([(i, street1) for i in [1, 2, 3]])
    expectations.extend([(i, street4) for i in [4, 5, 6]])
    expectations.extend([(i, street34) for i in [34, 35, 36]])
    self.check_bins(expectations)

  def test_corner_outcomes(self):
    """Check that CornerOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_corner_outcomes()
    corner1 = Corner(1)
    corner2 = Corner(2)
    corner19 = Corner(19)
    corner32 = Corner(32)
    expectations = []
    expectations.extend([i, corner1] for i in [1, 2, 4, 5])
    expectations.extend([i, corner2] for i in [2, 3, 5, 6])
    expectations.extend([i, corner19] for i in [19, 20, 22, 23])
    expectations.extend([i, corner32] for i in [32, 33, 35, 36])
    self.check_bins(expectations)

  def test_five_numbers(self):
    """Check that FiveNumbersOutcome is assigned correctly to TempBins."""
    self.bin_builder.prepare_five_numbers()
    five_numbers = FiveNumbers()
    expectations = [[i, five_numbers] for i in [37, 0, 1, 2, 3]]
    self.check_bins(expectations)

  def test_line_outcomes(self):
    """Check that LineOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_line_outcomes()
    line1 = Line(1)
    line4 = Line(4)
    line31 = Line(31)
    expectations = []
    expectations.extend([[i, line1] for i in range(1, 7)])
    expectations.extend([[i, line4] for i in range(4, 10)])
    expectations.extend([[i, line31] for i in range(31, 37)])
    self.check_bins(expectations)

  def test_dozen_outcomes(self):
    """Check that DozenOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_dozen_outcomes()
    first12 = Dozen(1)
    third12 = Dozen(3)
    expectations = []
    expectations.extend([[i, first12] for i in [1, 2, 8, 12]])
    expectations.extend([[i, third12] for i in [25, 34, 36]])
    self.check_bins(expectations)

  def test_column_outcomes(self):
    """Check that ColumnOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_column_outcomes()
    column1 = Column(1)
    column2 = Column(2)
    column3 = Column(3)
    expectations = []
    expectations.extend([[i, column1] for i in [1, 7, 34]])
    expectations.extend([[i, column2] for i in [2, 17, 35]])
    expectations.extend([[i, column3] for i in [3, 24, 36]])
    self.check_bins(expectations)

  def test_range_outcomes(self):
    """Check that Low/High Outcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_range_outcomes()
    low = EvenMoney("Low")
    high = EvenMoney("High")
    expectations = []
    expectations.extend([(i, low) for i in (1, 2, 7, 11, 15, 18)])
    expectations.extend([(j, high) for j in (19, 20, 25, 32, 33, 36)])
    self.check_bins(expectations)

  def test_colour_outcomes(self):
    """Check that Red/Black Outcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_colour_outcomes()
    red = EvenMoney("Red")
    black = EvenMoney("Black")
    expectations = []
    expectations.extend([[i, red] for i in [1, 7, 14, 19, 27, 36]])
    expectations.extend([[j, black] for j in [2, 4, 11, 15, 22, 29, 35]])
    self.check_bins(expectations)

  def test_parity_outcomes(self):
    """Check that Even/Odd Outcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_parity_outcomes()
    even = EvenMoney("Even")
    odd = EvenMoney("Odd")
    expectations = []
    expectations.extend([[i, even] for i in [2, 4, 10, 20, 24, 36]])
    expectations.extend([[i, odd] for i in [1, 3, 13, 15, 29, 35]])
    self.check_bins(expectations)

if __name__ == '__main__':
  unittest.main()
