import os


class GenCasePy(object):
    """用于生成文件"""
    def __init__(self):
        self.createdServices = []

    def createFileClass(self,serviceName):
        className = '''
from common.base import base

class %s(base):''' % serviceName

        fileName = serviceName +".py"

        with open(fileName, "w", encoding='utf-8') as fw:
            fw.write(className)

    def createPyFile(self, APIName, APIType, serviceName, funcFormalParaList, paramTypeMap,  verifyParamsList, variableString,returnString):
        '''
        :param APIName: 接口名称,eg:addOrderAPI 
        :param APIType: API的类型,eg:query,mutation等
        :param serviceName:服务名称
        :param funcFormalParaList: 方法中形参参数列表
        :param paramTypeMap: 参数和参数类型的对照表,eg:age : int
        :param verifyParamsList: 验证语句参数列表
        :param variableString:variables参数
        '''
        fileName = serviceName + ".py"

        # 不重复创建
        if serviceName not in self.createdServices:
            self.createFileClass(serviceName=serviceName)
            self.createdServices.append(serviceName)

        funcContent = '''
    def {APIName}(self{funcFormalParaList}):
        query="""{APIType}{paramTypeMap}{{
  {APIName}{verifyParamsList}{{
{returnString}
  }}
}}
"""
        operationName = None
        variables = {{
{variableString}
            }}
        return self.request(query, operationName, variables)'''.format(
            APIName = APIName, funcFormalParaList = funcFormalParaList,
            APIType = APIType, paramTypeMap = paramTypeMap,
            verifyParamsList = verifyParamsList, variableString = variableString,returnString = returnString)

        with open(fileName, "a+", encoding='utf-8') as fw:
        # print("=========123213213213213123")
        # print(text)
            fw.write(funcContent)
