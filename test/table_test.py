import unittest
from vegas.table import Table
from vegas.outcomes import EvenMoney, Split
from vegas.bet import Bet
from vegas.invalid_bet import InvalidBet


class TableTest(unittest.TestCase):
  """Unit test for the Table class."""

  def setUp(self):
    self.outcome = EvenMoney("Red")
    self.table = Table(0, 10)

  def test_initialization(self):
    """The constructor should save all parameters correctly."""
    self.assertEqual(len(self.table.bets), 0)
    self.assertEqual(self.table.minimum, 0)
    self.assertEqual(self.table.limit, 10)

  def test_placeBet(self):
    """It should be possible to place a Bet on a Table."""
    bet = Bet(12, self.outcome)
    self.table.placeBet(bet)
    self.assertEqual(self.table.__iter__().__next__(), bet)

  def test_iter(self):
    """The __iter__ method should return an iterable of the Bets."""
    bets = [Bet(i+1, self.outcome) for i in range(3)]
    for bet in bets:
      self.table.placeBet(bet)
    iter_bets = self.table.__iter__()
    for bet in bets:
      self.assertEqual(iter_bets.__next__(), bet)

  #################### Table to string ###############################

  def table_with_bets(self):
    """Prepare a Table a with some Bets on it."""
    self.table.placeBet(Bet(4, Split(1, 4)))
    self.table.placeBet(Bet(6, EvenMoney("High")))
    return self.table

  def test_str(self):
    """Test the __str__ method."""
    self.assertEqual(
      self.table_with_bets().__str__(), "4 on Split 1-4 (17:1), 6 on High (1:1)")

  def test_repr(self):
    """Test the __repr__ method."""
    self.assertEqual(
      self.table_with_bets().__repr__(),
      "Table(Bet(4, Outcome('Split 1-4', 17)), Bet(6, Outcome('High', 1)))")

  ##################### Table isValid()? ##############################

  def test_table_isValid_empty_table(self):
    """An empty Table should be valid."""
    table = Table(0, 1)
    self.assertTrue(table.isValid())

  def test_table_isValid_valid_table(self):
    """A valid Table should be a valid."""
    table = Table(1, 10)
    table.placeBet(Bet(1, EvenMoney("Red")))
    table.placeBet(Bet(2, EvenMoney("Black")))
    self.assertTrue(table.isValid())

  def test_table_isValid_minimum_bet_amount(self):
    """Each Bet should be greater or equal to the Table minimum."""
    table = Table(10, 1000)
    # invalid Bet (amountBet less than Table minimum)
    table.placeBet(Bet(1, EvenMoney("Black")))
    self.assertRaises(InvalidBet, table.isValid)

  def test_table_isValid_total_table_limit(self):
    """Sum of all Bets should be less or equal to the Table limit."""
    table = Table(0, 10)
    # invalid Bet (total table bets more than limit)
    table.placeBet(Bet(11, EvenMoney("High")))
    self.assertRaises(InvalidBet, table.isValid)

if __name__ == '__main__':
  unittest.main()
