import unittest

from context import vegas
from vegas.bin_builder import BinBuilder
from vegas.outcome import Outcome
from vegas.roulette import Roulette


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
    expectations = [
      (0, Outcome("Straight 0", Roulette.StraightBet)),
      (37, Outcome("Straight 00", Roulette.StraightBet)),
      (1, Outcome("Straight 1", Roulette.StraightBet)),
      (2, Outcome("Straight 2", Roulette.StraightBet)),
      (36, Outcome("Straight 36", Roulette.StraightBet))]
    self.check_bins(expectations)

  def test_split_outcomes(self):
    """Check that SplitOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_split_outcomes()
    expectations = [
      # Bin 1: start corner
      (1, Outcome("Split 1-2", Roulette.StraightBet)),
      (1, Outcome("Split 1-4", Roulette.StraightBet)),
      # Bin 2: start side
      (2, Outcome("Split 1-2", Roulette.StraightBet)),
      (2, Outcome("Split 2-5", Roulette.StraightBet)),
      (2, Outcome("Split 2-3", Roulette.StraightBet)),
      # Bin 3: start corner
      (3, Outcome("Split 2-3", Roulette.StraightBet)),
      (3, Outcome("Split 3-6", Roulette.StraightBet)),
      # Bin 19: middle side
      (19, Outcome("Split 16-19", Roulette.StraightBet)),
      (19, Outcome("Split 19-20", Roulette.StraightBet)),
      (19, Outcome("Split 19-22", Roulette.StraightBet)),
      # Bin 29: middle
      (29, Outcome("Split 26-29", Roulette.StraightBet)),
      (29, Outcome("Split 28-29", Roulette.StraightBet)),
      (29, Outcome("Split 29-30", Roulette.StraightBet)),
      (29, Outcome("Split 29-32", Roulette.StraightBet)),
      # Bin 36: end
      (36, Outcome("Split 33-36", Roulette.StraightBet)),
      (36, Outcome("Split 35-36", Roulette.StraightBet)),
    ]
    self.check_bins(expectations)

  def test_street_outcomes(self):
    """Check that StreetOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_street_outcomes()
    street1 = Outcome("Street 1", Roulette.StreetBet)
    street2 = Outcome("Street 2", Roulette.StreetBet)
    street12 = Outcome("Street 12", Roulette.StreetBet)
    expectations = []
    expectations.extend([(i, street1) for i in [1, 2, 3]])
    expectations.extend([(i, street2) for i in [4, 5, 6]])
    expectations.extend([(i, street12) for i in [34, 35, 36]])
    self.check_bins(expectations)

  def test_corner_outcomes(self):
    """Check that CornerOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_corner_outcomes()
    corner1245 = Outcome("Corner 1-2-4-5", Roulette.CornerBet)
    corner2356 = Outcome("Corner 2-3-5-6", Roulette.CornerBet)
    corner19202223 = Outcome("Corner 19-20-22-23", Roulette.CornerBet)
    corner32333536 = Outcome("Corner 32-33-35-36", Roulette.CornerBet)
    expectations = []
    expectations.extend([i, corner1245] for i in [1, 2, 4, 5])
    expectations.extend([i, corner2356] for i in [2, 3, 5, 6])
    expectations.extend([i, corner19202223] for i in [19, 20, 22, 23])
    expectations.extend([i, corner32333536] for i in [32, 33, 35, 36])
    self.check_bins(expectations)

  def test_five_numbers(self):
    """Check that FiveNumbersOutcome is assigned correctly to TempBins."""
    self.bin_builder.prepare_five_numbers()
    five_numbers = Outcome("Five numbers", Roulette.FiveNumbers)
    expectations = [[i, five_numbers] for i in [37, 0, 1, 2, 3]]
    self.check_bins(expectations)

  def test_line_outcomes(self):
    """Check that LineOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_line_outcomes()
    line12 = Outcome("Line 1-2", Roulette.LineBet)
    line23 = Outcome("Line 2-3", Roulette.LineBet)
    line1112 = Outcome("Line 11-12", Roulette.LineBet)
    expectations = []
    expectations.extend([[i, line12] for i in range(1, 7)])
    expectations.extend([[i, line23] for i in range(4, 10)])
    expectations.extend([[i, line1112] for i in range(31, 37)])
    self.check_bins(expectations)

  def test_dozen_outcomes(self):
    """Check that DozenOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_dozen_outcomes()
    first12 = Outcome("First 12", Roulette.DozenBet)
    third12 = Outcome("Third 12", Roulette.DozenBet)
    expectations = []
    expectations.extend([[i, first12] for i in [1, 2, 8, 12]])
    expectations.extend([[i, third12] for i in [25, 34, 36]])
    self.check_bins(expectations)

  def test_column_outcomes(self):
    """Check that ColumnOutcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_column_outcomes()
    column1 = Outcome("Column 1", Roulette.ColumnBet)
    column2 = Outcome("Column 2", Roulette.ColumnBet)
    column3 = Outcome("Column 3", Roulette.ColumnBet)
    expectations = []
    expectations.extend([[i, column1] for i in [1, 7, 34]])
    expectations.extend([[i, column2] for i in [2, 17, 35]])
    expectations.extend([[i, column3] for i in [3, 24, 36]])
    self.check_bins(expectations)

  def test_range_outcomes(self):
    """Check that Low/High Outcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_range_outcomes()
    low = Outcome("Low", Roulette.EvenMoneyBet)
    high = Outcome("High", Roulette.EvenMoneyBet)
    expectations = []
    expectations.extend([(i, low) for i in (1, 2, 7, 11, 15, 18)])
    expectations.extend([(j, high) for j in (19, 20, 25, 32, 33, 36)])
    self.check_bins(expectations)

  def test_colour_outcomes(self):
    """Check that Red/Black Outcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_colour_outcomes()
    red = Outcome("Red", 1)
    black = Outcome("Black", 1)
    expectations = []
    expectations.extend([[i, red] for i in [1, 7, 14, 19, 27, 36]])
    expectations.extend([[j, black] for j in [2, 4, 11, 15, 22, 29, 35]])
    self.check_bins(expectations)

  def test_parity_outcomes(self):
    """Check that Even/Odd Outcomes are assigned correctly to TempBins."""
    self.bin_builder.prepare_parity_outcomes()
    even = Outcome("Even", 1)
    odd = Outcome("Odd", 1)
    expectations = []
    expectations.extend([[i, even] for i in [2, 4, 10, 20, 24, 36]])
    expectations.extend([[i, odd] for i in [1, 3, 13, 15, 29, 35]])
    self.check_bins(expectations)

if __name__ == '__main__':
  unittest.main()
