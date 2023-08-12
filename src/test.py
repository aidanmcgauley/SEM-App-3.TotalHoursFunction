import unittest
import addHours

class TestAddHours(unittest.TestCase):
    def test_add_hours(self):
        attendances = [2,1,2,2]
        self.assertEqual(addHours.add_hours(attendances),7)

if __name__ == '__main__':
    unittest.main()