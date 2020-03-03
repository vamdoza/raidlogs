import json

from raidlogs import requestlib


class Api(object):

    def __init__(self, key=None):
        self.base_url = "https://www.fflogs.com:443/v1"
        self.key = key

    def get_reports(self, report_id):
        url = '%s/report/fights/%s' % (self.base_url, report_id)
        resp = requestlib.get(self.__add_auth_key(url))
        return json.loads(resp, encoding='utf-8')

    def __add_auth_key(self, url):
        params = {'api_key': self.key}
        return requestlib.encode_url_with_params(url, params)


