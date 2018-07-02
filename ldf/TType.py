from enum import Enum
from datetime import datetime


class TType(Enum):
    FORMATTED = 0  # Default 2016-09-19
    REAL = 1  # Start at 0 - 0.2 - 1 - 3.2 - 3.03 - and so on

    @staticmethod
    def formated2real(itime):
        pass

    @staticmethod
    def real2formated(itime):
        pass

    @staticmethod
    def toStr(ttype):
        if ttype == TType.REAL:
            return "REAL"
        elif ttype == TType.FORMATTED:
            return "FORMATTED"