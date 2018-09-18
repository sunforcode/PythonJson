import json
from workJson import jsonString

#寻找根节点
def getData(key,dic:dict):
    for k,v in dic.items():
        if isinstance(v,dict) and k==key and v.get(key)!= None:
            return getData(key, v)
        else:
            return v

#将整个param整合成一个字典
def getParamsDic(rootKey,recurKey,dic):
    resultDic:dict = {}
    typeDic:dict = dic.get(rootKey) #获取到key为type的字典
    for k,v in typeDic.items():
        if k == recurKey and typeDic.get(recurKey) != None: #存在需要递归的字典,并且递归的字典不为None
            tempDic = getData(recurKey, typeDic) #将递归的字典整合到最终的字典中
            # print(tempDic)
            for kt,vt in tempDic.items():
                if kt != "ofType": #去掉这个递归的key
                    # print(kt)
                    # print(vt)
                    resultDic[kt] = vt
        else:
            print(k)
            resultDic[k] = v
            pass
        pass
    return resultDic
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
i = 0
for signleField in fieldArray :
    print(i)
    i = i+1
    argsArray = signleField.get("args")
    for arg in argsArray:
       resultDic = getParamsDic("type","ofType",arg)
       # print(resultDic)
        # typeDic = arg["type"]  # dic
        # rootType = getData("ofType",typeDic)
        # print(i)
        # print(rootType)
        # i = i + 1
