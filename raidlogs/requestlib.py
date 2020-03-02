import urllib.request
import urllib.error


def get(url):
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            encoding = response.headers.get_content_charset()
            return data.decode(encoding)

    except urllib.error.HTTPError as er:
        print(er)
