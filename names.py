import urllib3
import certifi
import lxml.etree
import io

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

url = 'https://www.ssa.gov/cgi-bin/popularnames.cgi'
xpath = '//table//table'
parser = lxml.etree.HTMLParser()

def get_year(year):
    r = http.request('POST', url, fields={'year': year, 'number': 'p', 'top': 10})
    tree = lxml.etree.parse(io.StringIO(r.data.decode('utf8')), parser)
    table, = tree.xpath(xpath)
    data = {'m': [], 'f': []}
    for tr in table.findall('tr')[1:-1]:
        _, mn, mp, fn, fp = map(lambda x: x.text, tr.findall('td'))
        data['m'].append(mn)
        data['f'].append(fn)
    return data
