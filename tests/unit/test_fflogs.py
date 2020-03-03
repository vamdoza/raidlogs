import unittest
from raidlogs import fflogs


# TODO mock request lib to get a canned response.
class TestFFLogs(unittest.TestCase):
    def setUp(self):
        from raidlogs import config
        self.api = fflogs.Api(config.API_KEY)

    def test_fflogs_incorrect_api_key_returns_401_unauthorized(self):
        api = fflogs.Api("12345678910")
        resp = api.get_classes()
        self.assertEqual(resp.get("error"), "Unauthorized")

    def test_fflogs_correct_api_key_returns_response(self):
        api = self.api
        resp = api.get_classes()
        self.assertDictIsNotEmpty(resp)

    def test_get_fight_report_returns_report(self):
        public_report_id = "WxadmGXqDRNCBvZf"
        resp = self.api.get_fight_report(public_report_id)
        self.assertDictIsNotEmpty(resp)

    def assertDictIsNotEmpty(self, dictionary):
        self.assertFalse(not dictionary, "Dictionary is Empty")


if __name__ == '__main__':
    unittest.main()
