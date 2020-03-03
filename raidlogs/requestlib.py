import urllib.request
import urllib.error
import urllib.parse
import json


def get(url):
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            encoding = response.headers.get_content_charset()
            return data.decode(encoding)

    except urllib.error.HTTPError as er:
        print(er)
        return json.dumps({"status": er.code, "error": er.reason})


def encode_url_with_params(url, params):
    encoded_query = urllib.parse.urlencode(params)
    return url + "?%s" % encoded_query


def response_to_dict(resp):
    if resp is None:
        return {}
    return json.loads(resp, encoding='utf-8')
