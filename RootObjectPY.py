import json
from create_case1 import GenCasePy
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
queryType=str(queryTypeName).split("Type")[0]
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

serviceName = ""
createdServices=[]

for signleField in fieldArray:
    # field下的list
    i = 0
    print("==============================")
    print("接口名称是 "+signleField["name"])
    argsArray = signleField.get("args")
    print("参数的数量是%d"%len(argsArray))
    serviceName = signleField["service"]
    print("--------------")
    paramasString = ""
    argsNameList = []
    args = ""
    variableString = ""
    for arg in argsArray:
        # args里面的所有参数
        print("第 %d 个参数" % i)
        i += 1
        resultList = getParamsDic(arg)  #将所有参数的要求保存到了一个数组中
        handledSingleParam = handleSingleString(resultList)
        if len(paramasString)>0:
            paramasString += ", "
        paramasString += "$"+arg["name"]+": "+handledSingleParam
        print("---")
        argsNameList.append(arg["name"])

        args = args + arg["name"] + ","
        single = ""

        if resultList[0] == "SCALAR" and  resultList[1] == "Int" :
            single = "\t\t\t"+"\"" + arg["name"] + "\"" + ":" + "int" + "(" + arg["name"] + ")" + "," + "\n"
            pass

        else: #resultList[0] == "SCALAR" and resultList[1] == "String":
            single ="\t\t\t"+ "\"" + arg["name"] + "\"" + ":" + arg["name"] + "," + "\t" + "\t" + "\t" + "\n"
        pass
        variableString = variableString  + single

    args = args[0:len(args) - 1]
    variableString = variableString[0:len(variableString) - 2]

    paramasString = "\"" + paramasString + "\""
    print(paramasString)
    portName = signleField["name"]
    last = formartString("query",paramasString,portName,"")


    # for name in argsNameList:
    #     args = args + name +","
    #     variableString = variableString + "\"" + name + "\"" +":"+name  + "," +"\t"+"\t"+"\t"+"\n"
    # args = args[0:len(args) -1]
    # variableString = variableString[0:len(variableString) -2]

    print(args) # 参数列表
    print("query")
    print(portName)
    print(paramasString)
    print(serviceName)
    inputObject = ""
    for argName in argsNameList:
        inputObject = inputObject + argName + ": $" + argName + ","

    inputObject = inputObject[0:len(inputObject)-1]
    print(inputObject)
    print("====-------")
    print(variableString)
    creater = GenCasePy(queryString="query", argsString=args, paramasString=paramasString, apiName=portName,
                        serviceName=serviceName, inputObject=inputObject, variableString=variableString)
    if serviceName not in createdServices:
        creater.createFileClass()
        createdServices.append(serviceName)
    creater.createPyFile()










# print(formatString)