import datetime
import pandas as pd
try:
    import cPickle as pickle
except:
    import pickle

from LongitudinalVariable import LongitudinalVariable as lv
from TType import TType

class LDF:
    def __init__(self):
        self.format = 'ldf'
        self.temporalType = TType.FORMATED
        self.metaData = None #metaData will be stored in a regular python 2d array first column being
        self.data = None

    def read(self, ifile):
        data = pickle.load(open(ifile, 'rb'))
        if hasattr(data, 'format'):
            if data.format != 'ldf':
                exit('Invalid format')
        else:
            exit('Invalid format')

        self.format = 'ldf'
        self.temporalType = data.temporalType
        self.metaData = data.metaData
        self.data = data.data

    def write(self, ofile):
        pickle.dump(self, open(ofile, 'wb'))

    def describe(self):
        return self.temporalType, self.metaData

    def converttype(self, ttype=TType.FORMATED):
        if self.temporalType == ttype:
            pass

    def add_metadata(self, imeta):
        pass

    def add_entry(self, idx, varname, idata):
        pass

    def remove_entry(self, idx, varname, itime):
        pass

    def add_row(self, idx, varname, idata):
        pass

    def remove_row(self, idx, varname):
        pass

    def add_sample(self, idx, idata):
        pass

    def remove_sample(self, idx):
        pass

    def transform_from_sparse(self, ifile):
        pass

    def transform_from_dense(self, ifile):
        pass

    def transform_to_sparse(self, ofile):
        pass

    def transform_to_dense(self, ofile):
        pass

    def import_sparse(self, ifile, imeta):
        pass

    def import_dense(self, ifile, imeta):
        pass

    def merge(self, ildf):
        pass

    def join(self, ildf):
        pass

    def split(self, idlist):
        pass

    def _converttime(self, itime):
        pass
