import re
import sys
from urllib import request

URL = 'https://www.google.com/search?q=dolar'
AGENT = 'Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/61.0'.encode('utf-8')
PATTERN = r'<span\s.+id=\"knowledge-currency__tgt-amount[^>]+>([\d,]+)<\/span>'


def _define_headers(user_agent=None):
    user_agent = user_agent or AGENT
    return {'User-Agent': AGENT}


def _get_body(req):
    res = request.urlopen(req)
    body = res.read()
    return body.decode('utf-8')


def _format_output(value):
    return value.replace(',', '.')


def get_dolar_value():
    headers = _define_headers()
    req = request.Request(URL, headers=headers)
    body = _get_body(req)
    match = re.search(PATTERN, body)
    if match:
        return _format_output(match.group(1))


sys.stdout.write(get_dolar_value())
