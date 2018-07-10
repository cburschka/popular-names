import urllib3
import certifi
import lxml.etree
import io

# Set up a HTTP client with HTTPS support.
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

url = 'https://www.ssa.gov/cgi-bin/popularnames.cgi'
parser = lxml.etree.HTMLParser()

def get_year(year):
    # Load the page:
    r = http.request('POST', url,
        headers={'Content-Type': 'x-www-form-urlencoded'},
        body='year={}&number=&top=10'.format(year)
    )

    # Parse the HTML document.
    tree = lxml.etree.parse(io.StringIO(r.data.decode('utf8')), parser)

    # Look for a table inside a table (very non-semantic markup unfortunately).
    try:
        table, = tree.xpath('//table//table')
    except:
        print(r.data.decode('utf8'))
        raise ValueError("No data for {}".format(year))

    # The table consists of three columns: Rank number (redundant), male name, female name.
    data = {'m': [], 'f': []}
    for tr in table.findall('tr')[1:-1]:
        _, mn, fn = map(lambda x: x.text, tr.findall('td'))
        data['m'].append(mn)
        data['f'].append(fn)

    return data
