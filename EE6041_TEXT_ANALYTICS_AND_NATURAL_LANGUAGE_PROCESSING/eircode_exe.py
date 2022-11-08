#!wget https://gist.githubusercontent.com/ajoorabchi/eac194a79dd26de8864f9206b7842ff1/raw/8ea1d8d5f74b5b2724e378b43d4df6094990c7db/Eircode%2520Routing%2520Key%2520Boundaries.csv
#A65F4E2
class EircodeChecker:

    def __init__(self,TestString):
        self.TestString=TestString
        self.ShortTestString=TestString[:3]
        import pandas as pd
        self.df = pd.read_csv('Eircode Routing Key Boundaries.csv').values

    def IsEircode(self):
        import re
        pattern = re.compile(r'[A-Z][0-9][0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]')
        result = pattern.match(self.TestString)
        if (result == None):
            return False
        else:
            for i in self.df:
                if i[0] == self.ShortTestString:
                    return i[1]
            return False


if __name__=="__main__":
    Check=EircodeChecker('A63F4E2')
    LocationInfo=Check.IsEircode()
    if LocationInfo:
        print('Eircode geographical district is', LocationInfo)
    else:
        print('This is not an Eircode')





