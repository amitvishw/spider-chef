from collections import OrderedDict

from src.bs.soap import Soap
from src.utils.util import Util

BASE_URL = "https://www.codechef.com"
PROFILE_URL = BASE_URL + "/users/"


class Spider:

    def __init__(self):
        pass

    @staticmethod
    def get_problems_codes(username):
        soup = Soap.get_soap(PROFILE_URL + username)
        if soup is None:
            return None
        articles = soup.findAll("div", {"class": "content"})[3].findAll("article")
        if len(articles) > 0:
            problems = OrderedDict()
            ps = articles[0].findAll("p")
            problems["practice"] = list(map(Util.practice_link_splitter, ps[0].findAll("a")))
            for p in ps[1:]:
                contest_name = p.findAll("strong")[0].text.replace(":", "")
                problems[contest_name] = [x.text for x in p.findAll("a")]
            return problems
        else:
            print("No problem codes found")
