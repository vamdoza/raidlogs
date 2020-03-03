import unittest
from raidlogs import fflogs


class TestFFLogs(unittest.TestCase):
    def setUp(self):
        from raidlogs import config
        self.api = fflogs.Api(config.API_KEY)

    def test_fflogsReturnsApiObject(self):
        api = fflogs.Api()
        self.assertIsNotNone(api)

    def test_fflogsReturnsApiWithKey(self):
        api = fflogs.Api("12345678910")
        self.assertIsNotNone(api)

    def test_getReportsReturnsJSONData(self):
        public_report_id = "WxadmGXqDRNCBvZf"
        response = self.api.get_reports(public_report_id)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
