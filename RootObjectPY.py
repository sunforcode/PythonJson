import json
from workJson import jsonString

#寻找根节点
def getData(key,dic:dict,paramString):
    paramString = paramString + "属性的要求是" + dic["kind"]
    if dic.get(key)!= None:
        return getData(key, dic.get(key),paramString)
    else:
        paramString = paramString + dic["kind"] +"类型的" + dic["name"]
        return paramString

#将整个param整合成一个字典
def getParamsDic(dic):
    paramString = ""
    typeDic = dic["type"]
    paramName = dic["name"]
    paramString = "参数名字是: " + paramName + " "
    if typeDic.get("ofType") != None:
        result = getData("ofType",typeDic,paramString)
        return result
    else:
        paramString += "无参数要求"
        return  paramString
        pass

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

for signleField in fieldArray :
    i = 0
    print("==============================")
    print("接口名称是 "+signleField["name"])
    argsArray = signleField.get("args")
    print("参数的数量是%d"%len(argsArray))
    print("--------------")
    for arg in argsArray:
        print("第 %d 个参数" % i)
        i += 1
        resultDic = getParamsDic(arg)
        print(resultDic)
        print("---")
