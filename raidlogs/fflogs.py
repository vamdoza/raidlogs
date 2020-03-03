from raidlogs import requestlib


class Api(object):

    def __init__(self, key=None):
        self.base_url = "https://www.fflogs.com:443/v1"
        self.key = key

    def get_fight_report(self, report_id):
        url = '%s/report/fights/%s' % (self.base_url, report_id)
        return self.__request_with_auth(url)

    def get_classes(self):
        url = '%s/classes' % self.base_url
        return self.__request_with_auth(url)

    def __request_with_auth(self, url):
        resp = requestlib.get(self.__add_auth_key(url))
        return requestlib.response_to_dict(resp)

    def __add_auth_key(self, url):
        params = {'api_key': self.key}
        return requestlib.encode_url_with_params(url, params)
