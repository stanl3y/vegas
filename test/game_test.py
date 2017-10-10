import unittest
import unittest.mock
from context import vegas
from vegas.game import Game
from vegas.table import Table
from vegas.wheel import Wheel


class GameTest(unittest.TestCase):
  """Unit test for the Game class."""

  def setUp(self):
    self.table = Table(0, 1)
    self.wheel = Wheel()
    self.game = Game(self.table, self.wheel)

  def test_initialize(self):
    """The constructor should save all parameters correctly."""
    self.assertEqual(self.game.table, self.table)
    self.assertEqual(self.game.wheel, self.wheel)

  def test_cycle(self):
    """The cycle method should invite the Player to placeBets."""
    mock_player = unittest.mock.Mock()
    self.game.cycle(mock_player)
    mock_player.placeBets.assert_called()


if __name__ == '__main__':
  unittest.main()
