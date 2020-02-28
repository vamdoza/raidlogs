import unittest
from raidlogs import raidmetrics


class TestRequest(unittest.TestCase):
    def setUp(self):
        # set up test data.
        pass

    def test_pass(self):
        # arrange
        # act
        # assert
        pass

    def test_getFightReport(self):
        fight_id = ''
        response = raidmetrics.getFightReport(fight_id)
        self.assertIsNotNone(response)

    def tearDown(self):
        # dispose test data.
        pass


if __name__ == '__main__':
    unittest.main()
