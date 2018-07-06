from ldf.LongitudinalVariable import LongitudinalVariable as lv
from ldf.LVDictionary import LVDictionary as lvd
from ldf.TType import TType
from ldf.DType import DType

try:
    import cPickle as pickle
except:
    import pickle


class LDF:
    def __init__(self):
        self.format = 'ldf'
        self.temporalType = TType.FORMATTED
        self.refTime = None
        self.metaData = {}
        self.metaHeader = []
        self.data = {}

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
        self.metaHeader = data.metaHeader
        self.refTime = data.refTime
        self.data = data.data

    def write(self, ofile):
        pickle.dump(self, open(ofile, 'wb'))

    def describe(self):
        return self.temporalType, self.metaData

    def converttype(self, ttype=TType.FORMATTED):
        if self.temporalType == ttype:
            pass

    def read_csvmeta(self, csvmeta):
        def scrub(istring):
            return istring.replace("\n", "")

        f = open(csvmeta, 'r')
        lines = f.readlines()
        f.close()

        #Check file type
        self.format = scrub(lines[0])

        if self.format != "ldf":
            exit("Invalid format")

        #Get Data Format
        ttype = scrub(lines[1])
        if ttype == "FORMATTED":
            self.temporalType = TType.FORMATTED
        elif ttype == "REAL":
            self.temporalType = TType.REAL
        else:
            exit("Invalid Temporal Type")

        #Get Reference Time
        self.refTime = scrub(lines[2])

        #Get header for metadata
        header = scrub(lines[3]).split("\t")
        self.metaHeader = header[1:]

        self.metaData = {}
        tempidx = 0
        for i in range(4, len(lines)):
            line = scrub(lines[i])
            if line == "__________":
                tempidx = i
                break
            else:
                tok = line.split("\t")
                self.metaData[tok[0]] = tok[1:]

        #Get a list of longitudinal variables and their datatypes
        for i in range(tempidx+1, len(lines)):
            line = scrub(lines[i])
            tok = line.split("\t")
            if tok[1] == "nominal":
                lvd.insertvar(tok[0], DType.NOMINAL, tok[2].split(";"))
            elif tok[1] == 'numeric':
                lvd.insertvar(tok[0])

    def write_csvmeta(self, csvfile):
        def formatcsv(ilist, delim="\t"):
            return delim.join(str(x) for x in ilist)

        def writeln(string):
            return string + "\n"

        f = open(csvfile, 'w+')

        f.write(writeln("ldf"))
        f.write(writeln(TType.toStr(self.temporalType)))
        # Reference Date
        if self.temporalType == TType.REAL:
            f.write(writeln(""))
        elif self.temporalType == TType.FORMATTED:
            f.write(writeln("0001-01-01"))

        f.write(writeln("ID" + "\t" + formatcsv(self.metaHeader)))
        for ik in self.metaData:
            f.write(writeln(ik + "\t" + formatcsv(self.metaData[ik])))

        f.write(writeln("__________"))

        for ik in lvd.keys():
            if lvd.vartype(ik) == DType.NOMINAL:
                f.write(writeln(ik + "\t" + "nominal" + "\t" + formatcsv(lvd.lvdict[ik][1], ";")))
            elif lvd.vartype(ik) == DType.NUMERIC:
                f.write(writeln(ik + "\t" + "numeric"))

    def read_csvdata(self, ifile):
        def scrub(istring):
            return istring.replace("\n", "")

        self.data = {}
        for i in self.metaData.keys():
            pass
        f = open(ifile, 'r')

        lines = f.readlines()
        for line in lines:
            l = scrub(line).split("\t")
            if l[0] not in self.metaData.keys():
                exit("Sample ID <" + l[0] + "> was not declared in metadata")
            if l[1] not in lvd.keys():
                exit("Variable was not declared in metadata")


        f.close()

    def write_csvdata(self, ofile):
        pass

    def import_from_row_data(self, ifile, imeta, delim=','):
        pass

    def merge(self, ildf):
        '''
        Take Union of dataset
        :param ildf: the input ldf to merge with this dataset
        :return:
        '''
        pass

    def join(self, ildf):
        '''
        Take intersection of dataset
        :param ildf:
        :return:
        '''
        pass

    def split(self, idlist):
        '''
        Return dataset using a list of ids
        :param idlist:
        :return:
        '''
        pass
