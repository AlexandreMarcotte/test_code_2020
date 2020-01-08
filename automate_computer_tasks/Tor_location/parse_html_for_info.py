from bs4 import BeautifulSoup


def find_ip_address():
    html_path = '/home/record/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/Downloads/IP Location Finder - Geolocation.html'
    with open(html_path) as f:
        soup = BeautifulSoup(f, 'html.parser')
    # result = soup.find_all('span')
    # ip_address = result[13].string
    table = soup.find_all('table')[0]
    table_val = table.find_all('td')
    ip = table_val[0].string
    print(ip)
    lat = float(table_val[-2].string)
    print(lat)
    long = float(table_val[-1].string)
    print(long)

if __name__ == '__main__':
    find_ip_address()

