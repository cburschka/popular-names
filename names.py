import urllib3
import certifi
import lxml.etree
import io

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

url = 'https://www.ssa.gov/cgi-bin/popularnames.cgi'
xpath = '//table//table'
parser = lxml.etree.HTMLParser()

def get_year(year):
    r = http.request('POST', url, body='year={}&number=&top=10'.format(year), headers={'Content-Type': 'x-www-form-urlencoded'})
    tree = lxml.etree.parse(io.StringIO(r.data.decode('utf8')), parser)
    try:
        table, = tree.xpath(xpath)
    except:
        print(r.data.decode('utf8'))
        raise ValueError("No data for {}".format(year))
    data = {'m': [], 'f': []}
    for tr in table.findall('tr')[1:-1]:
        _, mn, fn = map(lambda x: x.text, tr.findall('td'))
        data['m'].append(mn)
        data['f'].append(fn)
    return data
