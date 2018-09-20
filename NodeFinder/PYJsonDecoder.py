
class pyDecoder(object):



     def formartString(self, queryString, paramasString, APIName, inputObject):
            formatString = """{query} ({paramas}) {{
            {APIName}({inputObject}) {{
                __typename
            }}
            }}""".format(query=queryString, paramas=paramasString, APIName=APIName, inputObject=inputObject)

            return formatString


     @classmethod #args = args + argName + ","
     def funcFormalParaList(cls,fieldDic):
         funcFormalParaList = ""
         for param in fieldDic.paramsList:
            funcFormalParaList = funcFormalParaList + ", " + param.name
         return funcFormalParaList
         pass

     #eg: after: $after,before: $before,first: $first,last: $last,marketUuid: $marketUuid
     @classmethod
     def testParamsList(cls,field):
         inputObject = ""
         for param in field.paramsList :
            inputObject = inputObject + param.name + ": $" + param.name + ", "

         if len(inputObject) > 0:
             inputObject = inputObject[0:len(inputObject)-2]
             inputObject = "\"" + inputObject + "\""
         return inputObject

    #eg: "$after: String, $before: String, $first: Int, $last: Int, $marketUuid: String!"
     @classmethod
     def queryParamList(cls,field):
         queryParamList = ""
         for param in field.paramsList :
             queryParamList += "$" + param.name + ": " + param.paramaType + ", "
         if len(queryParamList) > 0:
             queryParamList = queryParamList[0:len(queryParamList)-2]
             queryParamList = "\"%s\""%queryParamList
         return queryParamList


     @classmethod
     def variablesList(cls,field):
         variablesListString = ""
         for param in field.paramsList:
             singleParam = ""
             if param.paramasTypeTree[0] == "SCALAR":
                 if param.paramasTypeTree[1] == "Int":
                     singleParam = "\t\t\t\"%s\":int(%s),\n"%(param.name,param.name)
             else:
                 singleParam = "\t\t\t\"%s\":%s,\n"%((param.name,param.name))

             variablesListString += singleParam
         if len(variablesListString) > 0:
             variablesListString = variablesListString[0:len(variablesListString)-2] #去最后的逗号
         return variablesListString

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

