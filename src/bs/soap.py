from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

hdr = {'User-Agent': 'Mozilla/5.0'}


class Soap:

    def __init__(self):
        pass

    @staticmethod
    def get_soap(url):
        try:
            req = Request(url, headers=hdr)
            page = urlopen(req)
            soap = BeautifulSoup(page, "lxml")
            return soap
        except Exception as e:
            print('Soap error for: '+url+": ", e)
