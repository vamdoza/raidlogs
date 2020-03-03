from raidlogs import config
from raidlogs import fflogs


def get_fight_report(report_id):
    api = fflogs.Api(config.API_KEY)
    report_data = api.get_fight_report(report_id)
    return report_data


get_fight_report("WxadmGXqDRNCBvZf")
