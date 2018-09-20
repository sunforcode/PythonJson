import json
# from  workJson import jsonString

class Finder(object):
    def __init__(self,jsonString,queryTpye):
        self.rootJson = json.loads(jsonString)
        self.queryTpye = queryTpye

    #找到所有的接口和参数的对象列表
    def getAllFieldList(self):
        fieldArray = self.getTypeField()
        allFieldList = []
        for signleField in fieldArray:
            apiModel = APIModel()
            apiModel.name = signleField["name"]
            apiModel.serviceName = signleField["service"]
            apiModelParamlist = []
            argsArray = signleField.get("args")

            for arg in argsArray:
                # args里面的所有参数
                paramModelT = paramModel()
                paramModelT.paramasTypeTree = self.getParamsDic(arg)  # 将所有参数的要求保存到了一个栈中
                paramModelT.name = arg["name"]
                apiModelParamlist.append(paramModelT)

            apiModel.paramsList = apiModelParamlist
            allFieldList.append(apiModel)
        return allFieldList


    # 寻找以root节点为名称的类型 queryType为: subscriptionType queryType mutationType
    # 返回值为以该queryType下的整个大根
    def findAllTypeNode(self):
        queryTypeName = self.rootJson["data"]["__schema"][self.queryTpye]["name"]
        typesArray = self.rootJson["data"]["__schema"]["types"]  # 是个list
        for signleType in typesArray:
            # 查看types下name为queryType_name值的
            if signleType["name"] == queryTypeName:
                print("找到了名字为" + queryTypeName + "的节点")
                break
        return  signleType

    #获取对应的节点中所有的 fields
    def getTypeField(self):
        queryType = self.findAllTypeNode()
        return queryType["fields"]


    #将一个params的所有限制构建成一个栈,栈顶是这个params的最终类型
    def getParamsDic(self,singleFieldDic:dict):
        paramStack = []
        typeDic = singleFieldDic["type"]
        # 如果获取到了oftype字典不为None,则进行递归的查找oftype
        if typeDic.get("ofType") != None:
            paramStack.append(typeDic["kind"])
            result = self.getDataList("ofType", typeDic.get("ofType"), paramStack)
            return result
        # 如果没有oftype的限制,直接读取
        else:
            paramStack.append(typeDic["kind"])
            paramStack.append(typeDic["name"])
            return paramStack

    #递归查找oftype的方式
    def getDataList(self,ofTypeKey, ofTypeValue: dict, paramList: list):
        if ofTypeValue.get(ofTypeKey) != None:
            paramList.append(ofTypeValue["kind"])
            return self.getDataList(ofTypeKey, ofTypeValue.get(ofTypeKey), paramList)
        else:
            paramList.append(ofTypeValue["kind"])
            paramList.append(ofTypeValue["name"])
            if ofTypeValue["kind"] == "OBJECT":
                print("最后的对象是一个object 需要再次进行递归探索")
            return paramList




#api接口对象
class APIModel(object):

    def __init__(self):
        self.name = ""
        self.serviceName = ""
        self.paramsList = []
        pass
    pass

# 参数对象
class paramModel(object):

    def __init__(self,name = "",paramasTypeTree = []):
        self.name = name
        self.paramasTypeTree = paramasTypeTree

    pass

