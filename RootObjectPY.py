import json
from workJson import jsonString
#寻找根节点
def getData(key,dic:dict):
    for k,v in dic.items():
        if isinstance(v,dict) and k==key and v.get(key)!= None:
            return getData(key, v)
        else:
            return v

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
    argsArray = signleField.get("args")
    for arg in argsArray:
        type1 = arg["type"]  # dic
        rootDic = getData("ofType",type1)
        print(rootDic)