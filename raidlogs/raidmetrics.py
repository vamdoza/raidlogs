from raidlogs import requestLib
from . import config

FFLogsReportsURL = "https://www.fflogs.com:443/v1/report/fights/"


def getFightReport(report_id):
    resp = requestLib.get(FFLogsReportsURL + "%s" % report_id, config.API_KEY)
    return resp
