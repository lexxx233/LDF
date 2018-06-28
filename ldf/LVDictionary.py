from ldf.DType import  DType

class LVDictionary:
    lvdict = {}

    @staticmethod
    def insertVar(varName, varType=DType.NUMERIC, varList=None):
        if varType == DType.NOMINAL:
            templist = {}
            tempstring = str(varList)
            tok = tempstring.replace("\n", "").split(";")
            i = 0
            for item in tok:
                templist[item] = i
                i += 1
            LVDictionary.lvdict[varName] = [DType.NOMINAL, templist]
        else:
            LVDictionary.lvdict[varName] = [DType.NUMERIC]

    @staticmethod
    def vars():
        return LVDictionary.lvdict.keys()