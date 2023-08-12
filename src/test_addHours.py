import unittest
import addHours

class TestAddHours(unittest.TestCase):

    def test_add_hours_normal(self):
        attendances = [2, 1, 2, 2]
        self.assertEqual(addHours.add_hours(attendances), 7)

    def test_add_hours_empty(self):
        attendances = []
        self.assertEqual(addHours.add_hours(attendances), 0)

    def test_add_hours_negative(self):
        attendances = [2, -1, 2, 2]
        self.assertEqual(addHours.add_hours(attendances), 5)

    def test_add_hours_large_numbers(self):
        attendances = [99999, 100000, 100000, 100001]
        self.assertEqual(addHours.add_hours(attendances), 400000)

if __name__ == '__main__':
    unittest.main()