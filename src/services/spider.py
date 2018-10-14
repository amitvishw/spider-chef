from collections import OrderedDict

from src.bs.soap import Soap
from src.models.solution import Solution
from src.utils.util import Util

BASE_URL = "https://www.codechef.com"
PROFILE_URL = BASE_URL + "/users/"
PRACTICE_SUB_URL = BASE_URL + "/status/{0},{2}"
CONTEST_SUB_URL = BASE_URL + "/{0}/status/{1},{2}"
SOLUTION_URL = BASE_URL + "/viewsolution/"


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

    @staticmethod
    def get_solutions_ids(username, contest, problem):
        if contest.upper() == "PRACTICE":
            url = PRACTICE_SUB_URL.format(problem, username)
        else:
            url = CONTEST_SUB_URL.format(contest, problem, username)
        soup = Soap.get_soap(url)
        if soup is None:
            return None
        trs = soup.findAll("tbody")[0].findAll("tr")
        solutions = []
        for row in trs:
            partial = None
            x = row.findAll("td")
            s_id = x[0].text
            src = x[3].findAll("img")[0].get("src")
            status = Util.get_solution_status(src)
            if status == "AC":
                try:
                    pts = x[3].text.split("[")[1][:-1]
                except IndexError:
                    pts = "1pts"
                if "100" in pts or "." in pts or (pts == "1pts" and status == "AC"):
                    partial = False
                else:
                    partial = True
            ext = Util.get_file_extension_for_language(x[6].text)
            solution = Solution(contest, problem, s_id, status, ext, partial, "")
            solutions.append(solution)
        return solutions

    @staticmethod
    def download_code(solution, username):
        try:
            soup = Soap.get_soap(SOLUTION_URL + solution.sId)
            if soup is None:
                return None
            code_text = []
            lis = soup.findAll("ol")[0].findAll("li")
            for li in lis:
                code_text.append(li.text)
            solution.text = code_text
            Util.write_in_file(solution, username)
        except IndexError:
            print("ERROR FOR:", solution.contest, solution.problem, solution.sId)
        except AttributeError:
            print("ERROR FOR:", solution.contest, solution.problem, solution.sId)

