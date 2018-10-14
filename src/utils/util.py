import pathlib

import os
import tarfile


class Util:

    def __init__(self):
        pass

    @staticmethod
    def practice_link_splitter(link):
        return link.get("href").split(",")[0].split("/")[2]

    @staticmethod
    def get_solution_status(img_src):
        if "cross-icon" in img_src:
            return "WA"
        if "tick-icon" in img_src:
            return "AC"
        if "runtime-error" in img_src:
            return "RE"
        if "alert-icon" in img_src:
            return "CE"
        if "clock_error" in img_src:
            return "TLE"
        return None

    @staticmethod
    def get_file_extension_for_language(language):
        if "C++" in language:
            return "cpp"
        if "PY" in language:
            return "py"
        if "JAVA" in language:
            return "java"
        if "C" in language:
            return "c"
        if "PAS" in language:
            return "pas"
        if "JAR" in language:
            return "jar"
        return "txt"

    @staticmethod
    def write_in_file(solution, username):
        name = solution.sId + "." + solution.extension
        data = "\n".join(map(str, solution.text))
        if solution.contest == "practice":
            path = username + "/" + solution.contest.upper() + "/" + solution.problem.upper() + "/"
        else:
            path = username + "/CONTEST/" + solution.contest.upper() + "/" + solution.problem.upper() + "/"
        try:
            out = open("CC/" + path + name, "w")
            out.write(data)
            out.close()
        except IOError:
            pass

    @staticmethod
    def make_dir(username, contest, code):
        pathlib.Path("CC/" + username + "/" + contest.upper() + "/" + code.upper()).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def make_tar_ball(username):
        path = os.path.abspath(os.path.join("", "CC/" + username))
        print(path)
        with tarfile.open(path + "/" + username + ".tar.gz", "w:gz") as tar:
            tar.add(path, os.path.basename(path))

