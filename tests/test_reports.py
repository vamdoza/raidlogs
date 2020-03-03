import json
import unittest

from raidlogs import reports


class TestReports(unittest.TestCase):
    def setUp(self):
        self.mocked_response = {}
        with open("data/test-response.json") as f:
            self.mocked_response = json.load(f)

    def test_get_time_report_should_pass(self):
        response = self.mocked_response
        report = reports.FightReport(response)
        self.assertIsNotNone(report)

    def test_get_time_report_returns_time_report(self):
        response = self.mocked_response
        report = reports.FightReport(response)
        with self.assertRaises(KeyError):
            report.get("raid_duration")
            report.get("active_time")
            report.get("inactive_time")

    def test_get_raid_duration(self):
        resp = self.mocked_response
        report = reports.FightReport(resp)
        self.assertEqual(report.get_raid_duration(), 10000)
