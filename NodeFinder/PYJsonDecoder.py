
class pyDecoder(object):



     def formartString(self, queryString, paramasString, APIName, inputObject):
            formatString = """{query} ({paramas}) {{
            {APIName}({inputObject}) {{
                __typename
            }}
            }}""".format(query=queryString, paramas=paramasString, APIName=APIName, inputObject=inputObject)

            return formatString

     @classmethod
     def handleSingleString(self, paramaList):

        i = len(paramaList) - 1
        length = len(paramaList)
        signleParamsString = ""
        lastType = ""

        while i >= 0:
            if i == length - 1:
                lastType = paramaList[i]
                # print(lastType)
                pass
            elif i == length - 2:
                lastSec = paramaList[i]
                if lastSec == "SCALAR":
                    signleParamsString += lastType
                elif lastSec == "ENUM":
                    signleParamsString += "String"
                elif lastSec == "INPUT_OBJECT":
                    signleParamsString += "INPUT_OBJECT"
                pass
            else:
                lastType = paramaList[i]
                if lastType == "NON_NULL":
                    signleParamsString += "!"
                elif lastType == "LIST":
                    signleParamsString = "[" + signleParamsString + "]"
                    pass
                pass
            i = i - 1
        return signleParamsString

