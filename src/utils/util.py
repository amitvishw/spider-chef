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
