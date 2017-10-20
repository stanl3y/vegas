import unittest

from vegas.bet import Bet
from vegas.outcome import Outcome
from vegas.outcomes import EvenMoney


class BetTest(unittest.TestCase):
  """Unit test for the Bet class."""

  def setUp(self):
    self.outcome = EvenMoney("Red")
    self.amount = 5
    self.bet = Bet(self.amount, self.outcome)

  def test_initialization(self):
    """Check the constructor works correctly."""
    self.assertEqual(self.bet.amountBet, self.amount)
    self.assertEqual(self.bet.outcome, self.outcome)

  def test_amount_bet(self):
    """Check that the amountBet is positive."""
    self.assertRaises(ValueError, Bet, *(-1, self.outcome))
    self.assertRaises(ValueError, Bet, *(0, self.outcome))

  def test_str(self):
    """Check the human-readable representation."""
    bet = Bet(12, Outcome("Jackpot", 42))
    self.assertEqual(bet.__str__(), "12 on Jackpot (42:1)")

  def test_repr(self):
    """Check the machine-readable representation."""
    bet = Bet(12, Outcome("Jackpot", 42))
    self.assertEqual(bet.__repr__(), "Bet(12, Outcome('Jackpot', 42))")

  def test_amount_won_lost_no_odds(self):
    """Check the amount of money won is calculated correctly."""
    bet = Bet(4, Outcome("No odds", 0))
    self.assertEqual(bet.winAmount(), 4)
    self.assertEqual(bet.loseAmount(), 4)

  def test_amount_won_lost_with_odds(self):
    """Check the amount of money lost is calculated correctly."""
    bet = Bet(6, Outcome("Some odds", 2))
    self.assertEqual(bet.winAmount(), 18)
    self.assertEqual(bet.loseAmount(), 6)


if __name__ == '__main__':
  unittest.main()
