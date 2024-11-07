import unittest
import os
from rw_json import write_to_file, read_from_file


class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_file.json'
        self.test_data = {
            'pk': 4,
            'title': 'Test Title',
            'author': 'Test Author',
            'published_date': '2024-06-23',
            'publisher': 6,
            'price': 9.99,
            'discounted_price': 3.56,
            'is_bestseller': True,
            'is_banned': False,
            'genres': [1, 2, 3]
        }

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_and_read_file(self):
        write_to_file(self.test_file, self.test_data)
        result = read_from_file(self.test_file)
        self.assertEqual(result, self.test_data)
        self.assertIsInstance(result['pk'], int)
        self.assertIsInstance(result['title'], str)
        self.assertIsInstance(result['author'], str)
        self.assertIsInstance(result['published_date'], str)
        self.assertIsInstance(result['publisher'], int)
        self.assertIsInstance(result['price'], float)
        self.assertIsInstance(result['discounted_price'], float)
        self.assertIsInstance(result['is_bestseller'], bool)
        self.assertIsInstance(result['is_banned'], bool)
        self.assertIsInstance(result['genres'], list)

    def test_write_and_read_empty_file(self):
        empty_data = {}
        write_to_file(self.test_file, empty_data)
        result = read_from_file(self.test_file)
        self.assertEqual(result, empty_data)

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file('nonexistent_file.json')

    def test_write_bad_data_into_file(self):
        bad_data = {'set_data': {1, 2, 3}}  # Sets are not JSON serializable
        with self.assertRaises(TypeError):
            write_to_file(self.test_file, bad_data)


if __name__ == '__main__':
    unittest.main()
