from raidlogs import requestlib


class Api(object):

    def __init__(self, key=None):
        self.base_url = "https://www.fflogs.com:443/v1"
        self.key = key

    def get_reports(self, report_id):
        url = '%s/report/fights/%s' % (self.base_url, report_id)
        resp = requestlib.get(url)
        return resp

    def __encode_api_key(self, url):
        params = {'api_key': self.key}
        return requestlib.encode_url_with_params(url, params)


