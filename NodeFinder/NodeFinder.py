import json
# from  workJson import jsonString

class Finder(object):
    def __init__(self,jsonString,queryTpye):
        self.rootJson = json.loads(jsonString)
        self.queryTpye = queryTpye

    #找到所有的接口和参数的对象列表
    def getAllFieldList(self):
        fieldArray = self.getTypeField(self.queryTpye)      # fields的内容,list
        allFieldList = []
        for signleField in fieldArray:
            apiModel = APIModel()
            apiModel.name = signleField["name"]
            apiModel.serviceName = signleField["service"]

            apiModelParamlist = []
            argsArray = signleField.get("args")   # args内容

            apiModel.returnObject = self.gerReturnType(signleField)

            inputObjcTitle = ""
            inputObjcName = ""
            for arg in argsArray:
                # args里面的所有参数
                paramModelT = paramModel()
                paramModelT.paramasTypeTree = self.getParamsDic(arg)  # 将所有参数的要求保存到了一个栈中,所有kind和最后一个值是name

                inputObjcTitle = self.hasInputObject(paramModelT.paramasTypeTree)
                # 判断是否为object或者input_object,返回最后一个name
                inputObjcName = arg["name"] #记录参数名称,最外层的name
                paramModelT.name = arg["name"]

                paramModelT.paramaType = self.handleSingleString(paramModelT.paramasTypeTree)
                apiModelParamlist.append(paramModelT)

            apiModel.paramsList = apiModelParamlist
            if inputObjcTitle != None and inputObjcTitle != "":
                inputObjc = self.getInputObject(inputObjcTitle)
                inputObjc.name = inputObjcName
                apiModel.input_object = inputObjc
            allFieldList.append(apiModel)
        return allFieldList

    def hasInputObject(self,paramasTypeTree):
        length = len(paramasTypeTree)
        objc = paramasTypeTree[(length - 2)]
        if objc == "OBJECT" or objc == "INPUT_OBJECT":
            return paramasTypeTree[length -1]       # 返回最后一个name
        else:
            return None

    # 获得input里面的参数
    def getInputObject(self,inputObjcName):
        inputObjc = inputObject()
        inputObjcNodeDic = self.findAllTypeNode(inputObjcName)
        inputModelParamlist = []
        inputFields = inputObjcNodeDic["inputFields"]
        for arg in inputFields:
            argModel = paramModel()
            argModel.paramasTypeTree = self.getParamsDic(arg)
            argModel.name = arg["name"]
            argModel.paramaType = self.handleSingleString(argModel.paramasTypeTree)
            inputModelParamlist.append(argModel)
        inputObjc.paramsList = inputModelParamlist
        return inputObjc

    # 寻找以root节点为名称的类型 queryType为: subscriptionType queryType mutationType
    # 返回值为以该queryType下的整个大根
    def findAllTypeNode(self,queryTypeName):
        # queryTypeName = self.rootJson["data"]["__schema"][self.queryTpye]["name"]
        typesArray = self.rootJson["data"]["__schema"]["types"]  # 是个list
        for signleType in typesArray:
            # 查看types下name为queryType_name值的
            if signleType["name"] == queryTypeName:
                print("找到了名字为" + queryTypeName + "的节点" )
                break
        return signleType

    def gerReturnType(self,field):

        returnObjct = returnObjcet()
        returnObjct.paramLimitCondition = self.getParamsDic(field)
        returnObjct.name = field["name"]#returnObjct.paramLimitCondition[len(returnObjct.paramLimitCondition) -1]
        addedList = []
        nextList = self.getNextObject(returnObjct.paramLimitCondition, addedList=addedList)
        returnObjct.childFieldList = nextList
        # returnObjct.returnObjectFields = nextList[1]
        return returnObjct

    def recursionFields(self,head:list):
        pass

    def getNextObject(self,paramsList:list,addedList:list):
        count =  len(paramsList)
        if count >= 2 and (paramsList[count - 2] == "OBJECT"):
            nextObjcName = paramsList[count - 1]
            nextField =  self.findAllTypeNode(nextObjcName)
            fieldsList =  nextField["fields"]
            # print(fieldsList)
            fieldNameList:list = []
            objectNameList: list = []
            for field in fieldsList:
                nextLevelList = self.getParamsDic(field)

                if nextLevelList[len(nextLevelList) -2] == "OBJECT" and nextLevelList[len(nextLevelList) -1] != "ApiKey":
                    next = self.gerReturnType(field)
                    fieldNameList.append(next)
                else:
                    fieldNameList.append(field["name"])

            return fieldNameList

                # if nextLevelList[len(nextLevelList) - 1] == "ApiKey":
                #     print(nextLevelList)
                # else:
                #
                #     self.getNextObject(nextLevelList,addedList=addedList)

        else:
            return None
            pass


        pass


    #获取对应的节点中所有的 fields
    def getTypeField(self,queryTpye):
        queryTypeName = self.rootJson["data"]["__schema"][queryTpye]["name"]
        queryType = self.findAllTypeNode(queryTypeName)
        return queryType["fields"]


    #将一个params的所有限制构建成一个栈,栈顶是这个params的最终类型
    def getParamsDic(self,singleFieldDic:dict):
        paramStack = []
        typeDic = singleFieldDic.get("type")
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
            # if ofTypeValue["kind"] == "OBJECT" or ofTypeValue["kind"] == "INPUT_OBJECT":
            #     print("最后的对象是一个object 需要再次进行递归探索")
            return paramList

    def handleSingleString(cls, paramaList):
        """拼接参数"""
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

#api接口对象
class APIModel(object):

    def __init__(self):
        self.name = ""
        self.serviceName = ""
        self.paramsList = []
        self.returnObject:inputObject = None #返回值对象
        self.input_object = None

class inputObject(object):
    def __init__(self,name = "",paramasTypeTree = []):
        self.name = name
        self.paramsList = []
    pass

class returnObjcet(object):

    def __init__(self):
        self.paramLimitCondition = []
        self.returnObjectFields = []
        self.name = ""
        self.childFieldList = []

    pass


# 参数对象
class paramModel(object):

    def __init__(self,name = "",paramasTypeTree = []):
        self.name = name
        self.paramasTypeTree = paramasTypeTree
        self.paramaType = ""

    pass

# a=paramModel