import unittest
from index import app

class TestTotalHours(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_total_hours_valid(self):
        response = self.client.get('/', query_string={
            'item_1': 'Lecture sessions',
            'item_2': 'Lab sessions',
            'item_3': 'Support session',
            'item_4': 'Canvas',
            'attendance_1': '2',
            'attendance_2': '1',
            'attendance_3': '2',
            'attendance_4': '2',
            'total_hours_1': '33',
            'total_hours_2': '22',
            'total_hours_3': '44',
            'total_hours_4': '55'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'total_hours': 7})

    def test_total_hours_invalid_negative_number(self):
        response = self.client.get('/', query_string={
            'item_1': 'Lecture sessions',
            'item_2': 'Lab sessions',
            'item_3': 'Support session',
            'item_4': 'Canvas',
            'attendance_1': '-5', #Invalid negative number
            'attendance_2': '1',
            'attendance_3': '2',
            'attendance_4': '2',
            'total_hours_1': '33',
            'total_hours_2': '22',
            'total_hours_3': '44',
            'total_hours_4': '55'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": True, "message": "Attendance hours cannot be negative."})

    def test_total_hours_invalid_not_integer(self):
        response = self.client.get('/', query_string={
            'item_1': 'Lecture sessions',
            'item_2': 'Lab sessions',
            'item_3': 'Support session',
            'item_4': 'Canvas',
            'attendance_1': 'invalid', #Invalid string
            'attendance_2': '1',
            'attendance_3': '2',
            'attendance_4': '2',
            'total_hours_1': '33',
            'total_hours_2': '22',
            'total_hours_3': '44',
            'total_hours_4': '55'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": True, "message": "Attendance hours must be integers."})

    # You can add more tests to cover other error cases...

if __name__ == '__main__':
    unittest.main()
