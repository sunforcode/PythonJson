import os


class GenCasePy(object):
    """用于生成文件"""
    def __init__(self, queryString, argsString, paramasString, apiName, serviceName, inputObject, variableString):
        '''
        :param queryString:query查询类型
        :param argsString:参数
        :param paramasString:构建的参数集合,如"$baseAssets: [String!]!, $quoteAsset: String!"
        :param apiName:接口名称,如assetPrices 
        :param inputObject:input_object参数
        :param variableString:variables参数
        '''
        self.queryString = queryString
        self.argsString = argsString
        self.paramasString = paramasString
        self.apiName = apiName
        self.serviceName = serviceName
        self.inputObject = inputObject
        self.variableString = variableString
        self.fileName = self.serviceName + ".py"
        self.first = False

    def createFileClass(self):
        className = '''
from common.base import base

class %s(base):''' % self.serviceName
        with open(self.fileName, "w", encoding='utf-8') as fw:
            self.first = True
            fw.write(className)

    def createPyFile(self):

        funcContent = '''
    def {funcName}(self,{args}):
        query="""{orderType} ({paramsString}) {{
  {apiName}({objcString}) {{
    orders {{
      id
      __typename
    }}
    __typename
  }}
}}
"""
        operationName = None
        variables = {{
{variableString}
            }}
        return self.request(query, operationName, variables)'''.format(funcName=self.apiName, args=self.argsString, orderType="query", paramsString=self.paramasString,
                       apiName=self.apiName, objcString=self.inputObject, variableString=self.variableString)
        with open(self.fileName, "a+", encoding='utf-8') as fw:
        # print("=========123213213213213123")
        # print(text)
            self.first = True
            fw.write(funcContent)
