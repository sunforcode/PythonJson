import json
from create_case1 import GenCasePy
from workJson import jsonString
from  NodeFinder import Finder,APIModel,paramModel
from PYJsonDecoder import pyDecoder


finder =  Finder(jsonString = jsonString,queryTpye="queryType")
allAPIList = finder.getAllFieldList()




# pyDecoder = pyDecoder()



    # print("接口名称是 " + apiModel.name)
    # APIServiceName = apiModel.serviceName
    # print("接口服务是 " + APIServiceName)
    #

    # APIParamsCount = len(argsArray)
    #
    # print("参数的数量是%d" % APIParamsCount)
    # print("--------------")
    #
    # APIName = signleField["name"]
    # #####################################
    # paramasString = ""
    # argsNameList = []
    # args = ""
    # variableString = ""

    #                paramModelT.paramaTypeString = paramModel.handleSingleString(paramModelT.paramasTypeTree)

    #
    #     paramaTypeString = paramModelT.paramaTypeString
    #     resultList = paramModelT.paramasTypeTree
    #     argName = paramModelT.name
    #
    #     ## 参数组装
    #     if len(paramasString)>0:
    #         paramasString += ", "
    #     paramasString += "$"+argName+": "+paramaTypeString
    #
    #     print("---")
    #     argsNameList.append(argName)
    #
    #     ##方法的参数列表
    #     args = args + argName + ","
    #
    #     # 强制转换 和 variables = {}
    #     single = ""
    #
    #     if resultList[0] == "SCALAR" and resultList[1] == "Int":
    #         single = "\t\t\t" + "\"" + argName + "\"" + ":" + "int" + "(" + argName + ")" + "," + "\n"
    #         pass
    #
    #     else:  # resultList[0] == "SCALAR" and resultList[1] == "String":
    #         single = "\t\t\t" + "\"" + argName + "\"" + ":" + argName + "," + "\t" + "\t" + "\t" + "\n"
    #     pass
    #     variableString = variableString + single
    #
    # # 接口层级
    # args = args[0:len(args) - 1]
    # variableString = variableString[0:len(variableString) - 2]
    #
    # paramasString = "\"" + paramasString + "\""
    # last = pyDecoder.formartString("query",paramasString,APIName,"")
    #
    # print(args) # 参数列表
    # print("query")
    # print(paramasString)
    # print(APIServiceName)
    # inputObject = ""
    #
    # for argName in argsNameList:
    #     inputObject = inputObject + argName + ": $" + argName + ","
    #
    # inputObject = inputObject[0:len(inputObject)-1]
    # print(inputObject)
    # print("====-------")
    # print(variableString)
    #
    #
    # #整体组装
    # creater = GenCasePy(queryString="query", argsString=args, paramasString=paramasString, apiName=APIName,
    #                     serviceName=APIServiceName, inputObject=inputObject, variableString=variableString)
    # if APIServiceName not in createdServices:
    #     creater.createFileClass()
    #     createdServices.append(APIServiceName)
    # creater.createPyFile()










# print(formatString)