import io
import unittest.mock

from raidlogs import requestlib


class TestRequest(unittest.TestCase):

    def test_getWithNoValidURLRaisesValueError(self):
        with self.assertRaises(ValueError):
            requestlib.get("")

    def test_getWithNoValidURLRaisesValueError(self):
        with self.assertRaises(ValueError):
            requestlib.get("python.com")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_getWithNonExistingURLReturns404(self, mock_print):
        requestlib.get("https://www.google.com/non-existing-path")
        self.assertEqual(mock_print.getvalue(), 'HTTP Error 404: Not Found\n')

    def test_getReturnDataWhenCorrectURL(self):
        response = requestlib.get("https://www.google.com/")
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
