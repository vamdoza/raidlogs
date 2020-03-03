import io
import unittest.mock

from raidlogs import requestlib


class TestRequestLib(unittest.TestCase):

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

    def test_EncodeURLWithParamsReturnEncodedURL(self):
        url = "www.google.com"
        params = {'user_id': 12345678910}
        encoded_url = requestlib.encode_url_with_params(url, params)
        self.assertEqual(encoded_url, "www.google.com?user_id=12345678910")


if __name__ == '__main__':
    unittest.main()
