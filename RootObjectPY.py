import json
from workJson import jsonString

def handleParam():
    pass

def handleLastParams():
    pass

#寻找根节点
def getData(key,dic:dict,paramString):
    paramString = paramString + "属性的要求是" + dic["kind"]
    if dic.get(key)!= None:
        return getData(key, dic.get(key),paramString)
    else:
        paramString = paramString + dic["kind"] +"类型的" + dic["name"]
        return paramString

def getDataList(key, dic: dict, paramList:list):
    if dic.get(key) != None:
        paramList.append(dic["kind"])
        return getDataList(key, dic.get(key), paramList)
    else:
        paramList.append(dic["kind"])
        paramList.append(dic["name"])
        return paramList
resultList = []
#将整个param整合成一个字典
def getParamsDic(dic):
    paramString = ""
    paramList = []
    typeDic = dic["type"]
    paramName = dic["name"]
    paramString = "$" + paramName + ":"
    if typeDic.get("ofType") != None:
        result = getDataList("ofType",typeDic,paramList)
        return result
    else:
        paramList.append(typeDic["kind"])
        paramList.append(typeDic["name"])
        return  paramList

rootJson = json.loads(jsonString)

queryTypeName = rootJson["data"]["__schema"]["queryType"]["name"]
mutationTypeName=rootJson["data"]["__schema"]["mutationType"]["name"]
typesArray = rootJson["data"]["__schema"]["types"]     #是个list

for signleType in typesArray:
    # 查看types下name为queryType_name值的
    if signleType["name"] == queryTypeName:
        print("找到了名字为"+queryTypeName+"的节点")
        break

fieldArray = signleType["fields"]
# 找到了fields,fields是个list

def handleSingleString(paramaList):
    i = len(paramaList)-1
    length = len(paramaList)
    signleParamsString = ""
    lastType = ""

    while i >= 0:
        if i == length-1:
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
        i = i-1
        pass
    # print("signleParamsString")
    # print(signleParamsString)
    # print("signleParamsString")
    return signleParamsString

"""query ($baseAssets: [String]!, $quoteAsset: String!) {
  assetPrices(baseAssets: $baseAssets, quoteAsset: $quoteAsset) {
    baseAsset
    price
    __typename
  }
}"""

def formartString(queryString,paramasString,portName,inputObject):
    formatString = """{query} ({paramas}) {{
      {portName}({inputObject}) {{
        __typename
      }}
    }}""".format(query = queryString,paramas = paramasString,portName = portName,inputObject = inputObject)
    return  formatString

for signleField in fieldArray:
    i = 0
    print("==============================")
    print("接口名称是 "+signleField["name"])
    argsArray = signleField.get("args")
    print("参数的数量是%d"%len(argsArray))
    print("--------------")
    paramasString = ""
    for arg in argsArray:
        print("第 %d 个参数" % i)
        i += 1
        resultList = getParamsDic(arg)  #将所有参数的要求保存到了一个数组中
        handledSingleParam = handleSingleString(resultList)
        if len(paramasString)>0:
            paramasString += ", "
        paramasString += "$"+arg["name"]+": "+handledSingleParam
        print("---")
    paramasString = "\"" + paramasString + "\""
    print(paramasString)
    last = formartString("query",paramasString,signleField["name"],"")
    print(last)





# print(formatString)