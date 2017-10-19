import unittest
import math

from vegas.outcome import Outcome


class OutcomeTest(unittest.TestCase):

  def setUp(self):
    self.outcome = Outcome("Red", 1)
    self.same_outcome = Outcome("Red", 1)
    self.diff_outcome = Outcome("Black", 1)

  def test_constructor(self):
    """Check that the constructor works."""
    self.assertEqual(self.outcome.name, "Red")
    self.assertEqual(self.outcome.odds, 1)

  def test_winAmount(self):
    """Check that winnings are calculated correctly."""
    outcome = Outcome("Sample outcome", 6)
    self.assertTrue(math.isclose(outcome.winAmount(3.2), 19.2))

  def test_equality(self):
    """Check comparisons of two Outcomes."""
    self.assertTrue(self.outcome.__eq__(self.outcome))
    self.assertTrue(self.outcome.__eq__(self.same_outcome))
    self.assertFalse(self.outcome.__eq__(self.diff_outcome))

    self.assertFalse(self.outcome.__ne__(self.outcome))
    self.assertFalse(self.outcome.__ne__(self.same_outcome))
    self.assertTrue(self.outcome.__ne__(self.diff_outcome))

  def test_hash(self):
    """Check hash-code generation."""
    self.assertEqual(self.outcome.__hash__(), self.outcome.__hash__())
    self.assertEqual(self.outcome.__hash__(), self.same_outcome.__hash__())
    self.assertNotEqual(self.outcome.__hash__(), self.diff_outcome.__hash__())

  def test_str(self):
    """Check the human-readable representation."""
    self.assertEqual(self.outcome.__str__(), "Red (1:1)")

  def test_repr(self):
    """ Check the machine-readable representation."""
    self.assertEqual(self.outcome.__repr__(), "Outcome('Red', 1)")

if __name__ == '__main__':
  unittest.main()
