import pandas as pd


class LongitudinalVariable:
    def __init__(self, ivar=None):
        self.data = pd.DataFrame(ivar, columns=list('td'))

    def append(self, ivar):
        self.data = self.data.append(pd.DataFrame(ivar, columns=list('td')))

    def remove_t(self, tvars):
        '''
        :param tvars: array of time t
        :return:
        '''
        self.data = self.data.drop(self.findarray(self.data.loc[:, 't'].tolist(), tvars))

    def select_range(self, tstart, tend):
        return self.data[(self.data[:, 't'] >= tstart) & (self.data[:, 't'] <= tend)]

    def t(self):
        return self.data.loc[:, 't'].tolist()

    def d(self):
        return self.data.loc[:, 'd'].tolist()

    @staticmethod
    def find(ilist, ivar):
        try:
            return ilist.index(ivar)
        except ValueError:
            return -1

    @staticmethod
    def findarray(ilist, ivars):
        res = []
        for i in ivars:
            j = LongitudinalVariable.find(ilist, i)
            if j != -1:
                res.append(j)
        return res
