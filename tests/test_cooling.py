import unittest

from cooling import minutes_to_cool


class TestMinutesToCool(unittest.TestCase):
    def test_default_mug(self):
        self.assertAlmostEqual(minutes_to_cool(85, 60), 11.23, places=2)

    def test_warmer_room_is_slower(self):
        self.assertGreater(minutes_to_cool(85, 60, t_room=30), minutes_to_cool(85, 60))

    def test_never_below_room(self):
        with self.assertRaises(ValueError):
            minutes_to_cool(85, 20)


if __name__ == "__main__":
    unittest.main()
