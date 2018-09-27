class Util:

    def __init__(self):
        pass

    @staticmethod
    def practice_link_splitter(link):
        return link.get("href").split(",")[0].split("/")[2]
