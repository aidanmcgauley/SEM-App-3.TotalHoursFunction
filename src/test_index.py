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

    def test_total_hours_invalid_negative_attendance(self):
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

    def test_total_hours_invalid_negative_totalhours(self):
        response = self.client.get('/', query_string={
            'item_1': 'Lecture sessions',
            'item_2': 'Lab sessions',
            'item_3': 'Support session',
            'item_4': 'Canvas',
            'attendance_1': '5', 
            'attendance_2': '1',
            'attendance_3': '2',
            'attendance_4': '2',
            'total_hours_1': '-33', #Invalid negative number
            'total_hours_2': '22',
            'total_hours_3': '44',
            'total_hours_4': '55'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": True, "message": "Total hours cannot be negative."})

    def test_total_hours_invalid_attendance_not_integer(self):
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

    def test_total_hours_invalid_totalhours_not_integer(self):
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
            'total_hours_2': 'invalid', #Invalid string
            'total_hours_3': '44',
            'total_hours_4': '55'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": True, "message": "A valid number for total hours has not been entered in the frontend code."})

    def test_total_hours_invalid_attendance_greatherthan_totalhours(self):
        response = self.client.get('/', query_string={
            'item_1': 'Lecture sessions',
            'item_2': 'Lab sessions',
            'item_3': 'Support session',
            'item_4': 'Canvas',
            'attendance_1': '400', #Invalid number: Greater than total available hours
            'attendance_2': '2200',
            'attendance_3': '4400',
            'attendance_4': '5500',
            'total_hours_1': '33',
            'total_hours_2': '22',
            'total_hours_3': '44',
            'total_hours_4': '55'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": True, "message": "Attendance hours cannot exceed total assigned hours."})

    

if __name__ == '__main__':
    unittest.main()
