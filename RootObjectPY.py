import json
from create_case1 import GenCasePy
from workJson import jsonString
from  NodeFinder import Finder,APIModel,paramModel
from PYJsonDecoder import pyDecoder

type = "queryType"
finder =  Finder(jsonString = jsonString,queryTpye=type)
allAPIList = finder.getAllFieldList()

createdServices=[]
for field in allAPIList:
    APIServiceName = field.serviceName
    queryString = type # query#
    apiName = field.name #
    funcFormalParaList = pyDecoder.funcFormalParaList(field) # 方法的形参列表#
    queryParamList = pyDecoder.queryParamList(field) #每个参数的类型
    testParamsList = pyDecoder.testParamsList(field) #验证参数
    variablesList = pyDecoder.variablesList(field) #variables中的参数

    creater = GenCasePy(queryString=type, funcFormalParaList=funcFormalParaList, paramasString=queryParamList, apiName=apiName,
                        serviceName=APIServiceName, inputObject=testParamsList, variableString=variablesList)

    if APIServiceName not in createdServices:
        creater.createFileClass()
        createdServices.append(APIServiceName)
    creater.createPyFile()
