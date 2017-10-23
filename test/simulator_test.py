from unittest.mock import Mock
import unittest
from vegas.simulator import Simulator
from vegas.game import Game
from vegas.table import Table
from vegas.wheel import Wheel
from vegas.martingale import Martingale


class SimulatorTest(unittest.TestCase):
  """A unit-test for the Simulator class."""

  def setUp(self):
    """Setup a basic Simulator with the Martingale Player."""
    self.table = Table(0, 100)
    self.wheel = Wheel()
    self.game = Game(self.table, self.wheel)
    self.player = Martingale(self.table, self.wheel)
    self.simulator = Simulator(self.game, self.player)

  def test_setup_objects(self):
    """Regression test for the setup: objects should have the correct type."""
    self.assertIsInstance(self.table, Table)
    self.assertIsInstance(self.wheel, Wheel)
    self.assertIsInstance(self.game, Game)
    self.assertIsInstance(self.player, Martingale)
    self.assertIsInstance(self.simulator, Simulator)

  def test_setup_relations(self):
    """Regression test for the setup: objects should have correct relations. """
    self.assertEqual(self.game.table, self.table)
    self.assertEqual(self.game.wheel, self.wheel)
    self.assertEqual(self.player.table, self.table)
    self.assertEqual(self.simulator.game, self.game)
    self.assertEqual(self.simulator.player, self.player)

  def test_has_initializing_values(self):
    """A Simulator should have attributes required for Simulation."""
    self.assertIsInstance(self.simulator.initDuration, int)
    self.assertIsInstance(self.simulator.initStake, int)
    self.assertIsInstance(self.simulator.samples, int)

  ############### Test Gather ################################

  def simulator_with_session_values(self):
    """Setup a simple Simulator with mock Session-values."""
    simulator = self.simulator
    simulator.samples = 4
    simulator.session = Mock()
    simulator.session.side_effect = [
      [6, 8, 1, 4, 5], [4, 1, 4, 7], [2], [6, 5, 9], [0], [0], [0], [0], [1, 2]]
    return simulator

  def test_gathers_durations_and_maxima_correctly(self):
    """A Simulator should gather the duration and maximum of each Session."""
    simulator = self.simulator_with_session_values()
    simulator.gather()
    self.assertEqual(simulator.durations, [5, 4, 1, 3])
    self.assertEqual(simulator.maxima, [8, 7, 2, 9])

  def test_duration_and_maxima_are_emptied(self):
    """Previously gathered data should not interfere with the current values."""
    simulator = self.simulator_with_session_values()
    simulator.gather()  # create unwanted data
    simulator.gather()  # data should be emptied in between
    self.assertEqual(simulator.durations, [1, 1, 1, 1])
    self.assertEqual(simulator.maxima, [0, 0, 0, 0])

  ################## Test Session ############################

  def prepare_wheel_spin(self, wheel, select_bin_nums):
    """Setup the given Wheel to Spin the Bins with the given numbers."""
    select_bins = map(lambda i: wheel.get(i), select_bin_nums)
    wheel.next = Mock()
    wheel.next.side_effect = select_bins

  def test_session(self):
    """A Session can end by running out of the available Rounds."""
    simulator = self.simulator
    self.prepare_wheel_spin(simulator.game.wheel, [2, 1, 1, 1, 2, 1, 0, 0])
    simulator.initDuration = 6
    simulator.initStake = 100
    self.assertEqual(simulator.session(), [101, 100, 98, 94, 102, 101])

  def test_session2(self):
    """A Session can end when a Player runs out of their Stake."""
    simulator = self.simulator
    simulator.initDuration = 6
    self.prepare_wheel_spin(simulator.game.wheel, [1, 1, 1, 2, 2, 2, 0])
    simulator.initStake = 7
    simulator.game.table.minimum = 1
    self.assertEqual(simulator.session(), [6, 4, 0])

  def test_session3(self):
    """A Session can end when a Player has too little Stake to place a Bet."""
    simulator = self.simulator
    simulator.initDuration = 6
    self.prepare_wheel_spin(simulator.game.wheel, [1, 1, 1, 1, 2, 0])
    simulator.initStake = 10
    simulator.game.table.minimum = 1
    self.assertEqual(simulator.session(), [9, 7, 3])

  def test_session4(self):
    """Data from a previous Session should not mix with the current values."""
    simulator = self.simulator
    simulator.initDuration = 2
    self.prepare_wheel_spin(simulator.game.wheel, [2, 2, 2, 2, 0])
    simulator.initStake = 10
    simulator.session()  # create unwanted stakes
    self.assertEqual(simulator.session(), [11, 12])


if __name__ == '__main__':
  unittest.main()
