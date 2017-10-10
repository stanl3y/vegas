import unittest
from context import vegas
from vegas.invalid_bet import InvalidBet


class InvalidBetTest(unittest.TestCase):
  """Unit test for the InvalidBet class."""

  def test_exception(self):
    """InvalidBet should be an Exception."""
    with self.assertRaises(InvalidBet):
      raise InvalidBet


if __name__ == '__main__':
  unittest.main()
