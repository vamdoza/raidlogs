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

    def test_get_raid_duration(self):
        resp = self.mocked_response
        report = reports.FightReport(resp)
        self.assertAlmostEqual(report.get_raid_duration(), 12576.555)

    def test_get_active_time(self):
        resp = self.mocked_response
        report = reports.FightReport(resp)
        self.assertAlmostEqual(report.get_active_time(), 7830.463)

    def test_get_inactive_time(self):
        resp = self.mocked_response
        report = reports.FightReport(resp)
        self.assertAlmostEqual(report.get_inactive_time(), 4746.092)

    def test_get_time_report_returns_report_with_keys(self):
        response = self.mocked_response
        report = reports.FightReport(response).get_time_report()
        self.assertIn("raid_duration", report)
        self.assertIn("active_time", report)
        self.assertIn("inactive_time", report)
