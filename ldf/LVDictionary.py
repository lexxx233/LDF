from ldf.DType import DType


class LVDictionary:
    lvdict = {}

    def __init__(self):
        return

    @staticmethod
    def insertvar(varname, vartype=DType.NUMERIC, varlist=None):
        if vartype == DType.NOMINAL:
            tempstring = str(varlist)
            tok = tempstring.replace("\n", "").split(";")
            LVDictionary.lvdict[varname] = [DType.NOMINAL, tok]
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
        try:
            return LVDictionary.lvdict[varname].index(varvalue)
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
        try:
            return LVDictionary.lvdict[varname][varvalue]
        except:
            return -1