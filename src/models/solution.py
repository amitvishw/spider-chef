class Solution:

    def __init__(self, contest, problem, s_id, status, extension, partial, text):
        self.contest = contest
        self.problem = problem
        self.sId = s_id
        self.status = status
        self.extension = extension
        self.partial = partial
        self.text = text

    def __repr__(self):
        return self.contest+" "+self.problem+" "+self.sId
