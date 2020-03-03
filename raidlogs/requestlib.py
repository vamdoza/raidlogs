import urllib.response
import urllib.request
import urllib.error
import urllib.parse


def get(url, api_key):
    try:
        params = {'api_key': api_key}
        encoded_query = urllib.parse.urlencode(params)

        full_url = url + "?%s" % encoded_query

        with urllib.request.urlopen(full_url) as response:
            data = response.read()
            encoding = response.headers.get_content_charset()
            return data.decode(encoding)

    except urllib.error.HTTPError as er:
        print(er)
