from raidlogs import config
from raidlogs import fflogs
from raidlogs import reports


def get_fight_report(report_id):
    api = fflogs.Api(config.API_KEY)
    report_data = api.get_fight_report(report_id)
    report = reports.FightReport(report_data)
    return report.get_time_report()


print(get_fight_report("WxadmGXqDRNCBvZf"))
