import io
import unittest.mock

from raidlogs import requestlib


# TODO mock request lib to get a canned response.
class TestRequestLib(unittest.TestCase):

    def test_get_with_no_valid_URL_raises_value_error(self):
        with self.assertRaises(ValueError):
            requestlib.get("")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_get_with_non_existing_path_prints_http_error(self, mock_print):
        requestlib.get("https://www.google.com/non-existing-path")
        self.assertEqual(mock_print.getvalue(), 'HTTP Error 404: Not Found\n')

    def test_encode_url_with_params_return_encoded_URL(self):
        url = "https://www.fflogs.com:443/v1"
        params = {'api_key': 12345678910}
        encoded_url = requestlib.encode_url_with_params(url, params)
        self.assertEqual(encoded_url, "https://www.fflogs.com:443/v1?api_key=12345678910")

    def test_response_to_dict_returns_dict_from_json(self):
        json = "{}"
        dictionary = requestlib.response_to_dict(json)
        self.assertIsNotNone(dictionary)


if __name__ == '__main__':
    unittest.main()
