from enum import Enum
from datetime import datetime


class TType(Enum):
    FORMATTED = 0  # Default 0001-01-01
    REAL = 1

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

    @staticmethod
    def daybetweenstr(d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2-d1).days)

    @staticmethod
    def daybetween(d1, d2):
        return abs((d2-d1).days)