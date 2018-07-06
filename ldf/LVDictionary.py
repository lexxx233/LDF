from ldf.DType import DType


class LVDictionary:
    lvdict = {}

    def __init__(self):
        return

    @staticmethod
    def insertvar(varname, vartype=DType.NUMERIC, varlist=None):
        if vartype == DType.NOMINAL:
            LVDictionary.lvdict[varname] = [DType.NOMINAL, varlist]
        else:
            LVDictionary.lvdict[varname] = [DType.NUMERIC]

    @staticmethod
    def keys():
        return LVDictionary.lvdict.keys()

    @staticmethod
    def keyidx(varname):
        return LVDictionary.lvdict.keys().index(varname)

    @staticmethod
    def vartype(varname):
        return LVDictionary.lvdict[varname][0]

    @staticmethod
    def values():
        return LVDictionary.lvdict.values()

    @staticmethod
    def getnomval(varname, varvalue):
        """
        Get nominal variable value based on nominal value

        :param varname:
        :param varvalue:
        :return:
        """
        LVDictionary._nomcheck(varname)

        try:
            return LVDictionary.lvdict[varname][1].index(varvalue)
        except:
            return -1

    @staticmethod
    def getnomvar(varname, varvalue):
        """
        Get nominal variable name based on index value

        :param varname:
        :param varvalue:
        :return:
        """
        LVDictionary._nomcheck(varname)

        try:
            if not(varvalue >= 0 & varvalue < len(LVDictionary.lvdict[varname][1])):
                exit("out of range for nominal variable array")
            return LVDictionary.lvdict[varname][1][varvalue]
        except:
            return -1

    @staticmethod
    def _nomcheck(varname):
        if varname not in LVDictionary.lvdict.keys():
            exit(varname + " does not exist")

        if LVDictionary.lvdict[varname][0] != DType.NOMINAL:
            exit(varname + " is not of Nominal Type")