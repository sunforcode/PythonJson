from NodeFinder import returnObjcet

class pyDecoder(object):

     #形参列表
     @classmethod
     def funcFormalParaList(cls,fieldDic):
         funcFormalParaList = ""
         for param in fieldDic.paramsList:
             if param.paramaType != "INPUT_OBJECT":
                 funcFormalParaList = funcFormalParaList + ", " + param.name
         if fieldDic.input_object:
             for param in fieldDic.input_object.paramsList:
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

         verifyParamsList += ",".join(["%s:$%s" % (x.paramasTypeTree[-1],x.paramasTypeTree[-1]) for x in field.paramsList])
         # for param in field.paramsList :
         #     verifyParamsList = verifyParamsList + param.name + ": $" + param.name + ", "
         #
         # if len(verifyParamsList) > 0:
         #     verifyParamsList = verifyParamsList[0:len(verifyParamsList)-2]
         #     verifyParamsList = verifyParamsList
         if verifyParamsList != "":
             verifyParamsList = "(" + verifyParamsList + ")"

         return verifyParamsList

    #eg: "$after: String, $before: String, $first: Int, $last: Int, $marketUuid: String!"
     @classmethod
     def paramTypeMap(cls,field):
         paramTypeMap = ""
         for param in field.paramsList :
             if param.paramaType != "INPUT_OBJECT":
                 paramTypeMap += "$" + param.name + ": " + param.paramaType + ", "
         if field.input_object:
             for param in field.input_object.paramsList:
                 paramTypeMap += "$" + param.name + ": " + param.paramaType + ", "
         if len(paramTypeMap) > 0:
             paramTypeMap = paramTypeMap[0:len(paramTypeMap)-2]
             paramTypeMap = "%s"%paramTypeMap
         if paramTypeMap != "":
             paramTypeMap = "(" + paramTypeMap +")"
         return paramTypeMap
     #参数variables
     @classmethod
     def variablesList(cls,field):
         variablesListString = ""
         # paramsList=field.paramsList
         # if field.input_object:
         #     paramsList.extend(field.input_object.paramsList)
         # paramsList = [x for x in paramsList if x.paramasTypeTree[1] != "INPUT_OBJECT"]
         for param in field.paramsList:
             singleParam = ""
             if param.paramasTypeTree[0] in ["SCALAR","ENUM","LIST"]:
                 if param.paramasTypeTree[1] == "Int":
                     singleParam = "\t\t\t\"%s\":int(%s),\n"%(param.name,param.name)
                 else:
                     singleParam = "\t\t\t\"%s\":%s,\n"%(param.name,param.name)
             # else:
             #     singleParam = "\t\t\t\"%s\":%s,\n"%((param.name,param.name))

             variablesListString += singleParam
         if field.input_object:
             for param in field.input_object.paramsList:
                 if param.paramasTypeTree[-2] in ["SCALAR","ENUM","LIST"]:
                     if param.paramasTypeTree[1] == "Int":
                         singleParam = "\t\t\t\"%s\":int(%s),\n" % (param.name, param.name)
                     else:
                         singleParam = "\t\t\t\"%s\":%s,\n" % (param.name, param.name)
                     variablesListString += singleParam
         # if len(variablesListString) > 0:
         #     variablesListString = variablesListString[0:len(variablesListString)-2] #去最后的逗号
         return variablesListString

     @classmethod
     def returnString(cls,field):
         if field.returnObject.childFieldList != None:
             resultString = ""
             res = cls.deCoder(resultString = resultString,childFieldList=field.returnObject.childFieldList,index=1)
             return res
         else:
             print("zaizhefanhui le ")
             return ""

     @classmethod
     def deCoder(cls,resultString,childFieldList,index):

         if childFieldList != None:
             for objc in childFieldList:
                 if isinstance(objc, returnObjcet):
                     resultString =  resultString +cls.multiplyT(index) +objc.name
                     resultString = resultString + "\n"+cls.multiplyT(index)+"{\n"
                     print(resultString)
                     tempDic = ""
                     resultString += cls.deCoder(tempDic,objc.childFieldList,index+1)
                     resultString = resultString +cls.multiplyT(index) +"}\n"
                     pass
                 else:
                     resultString = resultString + cls.multiplyT(index) + objc + "\n"
                     # print(resultString)
                     # return resultString
                     pass
             return resultString
         else:
             # print(resultString)
             # print("-======")
             return resultString

     @classmethod
     def multiplyT(cls,index):
         result = ""
         for i in range(0,index):
             result += "\t"
         return result

