
class pyDecoder(object):

     #形参列表
     @classmethod
     def funcFormalParaList(cls,fieldDic):
         funcFormalParaList = ""
         for param in fieldDic.paramsList:
            funcFormalParaList = funcFormalParaList + ", " + param.name
         return funcFormalParaList


     #eg: after: $after,before: $before,first: $first,last: $last,marketUuid: $marketUuid
     @classmethod
     def verifyParamsList(cls,field):
         verifyParamsList = ""
# input: {marketUuid: $marketId, side: $side, price: $price, amount: $amount}
         if field.input_object != None:
             for arg in field.input_object.paramsList:
                 verifyParamsList = verifyParamsList + arg.name + ": $" + arg.name + ", "

             if len(verifyParamsList) > 0:
                 verifyParamsList = verifyParamsList[0:len(verifyParamsList) - 2]
                 verifyParamsList = "%s: {%s}"%(field.input_object.name,verifyParamsList)
             print(verifyParamsList)
         else:
             for param in field.paramsList :
                 verifyParamsList = verifyParamsList + param.name + ": $" + param.name + ", "

             if len(verifyParamsList) > 0:
                 verifyParamsList = verifyParamsList[0:len(verifyParamsList)-2]
                 verifyParamsList = "\"" + verifyParamsList + "\""
         return verifyParamsList

    #eg: "$after: String, $before: String, $first: Int, $last: Int, $marketUuid: String!"
     @classmethod
     def paramTypeMap(cls,field):
         paramTypeMap = ""
         for param in field.paramsList :
             paramTypeMap += "$" + param.name + ": " + param.paramaType + ", "
         if len(paramTypeMap) > 0:
             paramTypeMap = paramTypeMap[0:len(paramTypeMap)-2]
             paramTypeMap = "\"%s\""%paramTypeMap
         return paramTypeMap

     #参数variables
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


