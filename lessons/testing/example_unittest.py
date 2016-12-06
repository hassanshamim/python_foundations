import unittest

from reindeer import Reindeer  # the reindeer.py file in the same directory


class ReindeerTest(unittest.TestCase):

    def test_can_create_reindeer(self):
        rd = Reindeer('Rudolph')

        self.assertIsInstance(rd, Reindeer)

    def test_reindeer_stores_attributes(self):
        """ Reindeer stores it's speed, run_time, and rest_time attributes """
        rd = Reindeer('Rudolph', speed=4, run_time=5, rest_time=6)

        self.assertEqual(rd.name, 'Rudolph')
        self.assertEqual(rd.speed, 4)
        self.assertEqual(rd.run_time, 5)
        self.assertEqual(rd.rest_time, 6)

    def test_reindeer_starts_at_position_zero(self):
        rd = Reindeer('Jim')

        self.assertEqual(rd.position, 0)

    def test_reindeer_starts_by_running(self):
        rd1 = Reindeer('Rudolph', speed=5, run_time=3, rest_time=2)
        rd2 = Reindeer('Rudolph', speed=10, run_time=4, rest_time=5)

        rd1.take_turn()
        rd2.take_turn()

        self.assertEqual(rd1.position, 5)
        self.assertEqual(rd2.position, 10)

    def test_reindeer_doesnt_move_when_resting(self):
        rd = Reindeer('Rudolph', speed=5, run_time=2, rest_time=3)
        rd.take_turn()
        rd.take_turn()

        previous_position = rd.position

        for i in range(3):
            rd.take_turn()
            self.assertEqual(rd.position, previous_position)

    def test_long_race(self):
        rd = Reindeer('Rudolph', speed=10, run_time=5, rest_time=3)

        for i in range(100):
            rd.take_turn()

        expected_position = 640

        self.assertEqual(rd.position, expected_position)



if __name__ == '__main__':
    unittest.main()
