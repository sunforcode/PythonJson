from create_case1 import GenCasePy
from workJson import jsonString
from  NodeFinder import Finder,APIModel,paramModel
from PYJsonDecoder import pyDecoder

type = "queryType"

finder = Finder(jsonString = jsonString,queryTpye=type)
allAPIList = finder.getAllFieldList()

creater = GenCasePy()

for field in allAPIList:
    APIServiceName = field.serviceName
    queryString = type # query#
    APIName = field.name
    funcFormalParaList = pyDecoder.funcFormalParaList(field) # 方法的形参列表#
    paramTypeMap = pyDecoder.paramTypeMap(field) #每个参数的类型
    verifyParamsList = pyDecoder.verifyParamsList(field) #验证参数
    variablesList = pyDecoder.variablesList(field) #variables中的参数
    returnString = pyDecoder.returnString(field)

    creater.createPyFile(APIName = APIName,APIType = type.replace("Type",""),serviceName = APIServiceName,
                         funcFormalParaList = funcFormalParaList,paramTypeMap = paramTypeMap,
                         verifyParamsList = verifyParamsList,variableString = variablesList,returnString = returnString)
