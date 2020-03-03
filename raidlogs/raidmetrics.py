from raidlogs import config
from raidlogs import fflogs


def get_fight_report(report_id):
    api = fflogs.Api(config.API_KEY)
    report = api.get_reports(report_id)
    print(report)


get_fight_report("WxadmGXqDRNCBvZf")
