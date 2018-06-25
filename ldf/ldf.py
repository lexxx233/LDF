from enum import Enum
import numpy as np
import datetime
import pandas as pd
import cPickle as pickle
import sys


class TType(Enum):
    FORMATED = 0  # Default 2016-09-19:18:00:00
    REAL = 1  # Start at 0 - 0.2 - 1 - 3.2 - 3.03 - and so on


class LDF:
    def __init__(self):
        self.format = 'ldf'
        self.temporalType = TType.FORMATED
        self.metaData = None
        self.data = None

    def read(self, ifile):
        data = pickle.load(open(ifile, 'rb'))
        if hasattr(data, 'format'):
            if data.format != 'ldf':
                sys.exit('Invalid format')
        else:
            sys.exit('Invalid format')

        self.format = 'ldf'
        self.temporalType = data.temporalType
        self.metaData = data.metaData
        self.data = data.data
        return True

    def write(self, ofile):
        pickle.dump(self, open(ofile, 'wb'))
        return True

    def describe(self):
        return self.temporalType, self.metaData

    def converttype(self, ttype=TType.FORMATED):
        if self.temporalType == ttype:
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

    def merge(self, ildf):
        pass

    def join(self, ildf):
        pass

    def split(self, idlist):
        pass

    def _convertTime(self, itime):
        pass
