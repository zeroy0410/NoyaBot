import json
import os
if not os.path.exists("./data.json"):
    f=open("./data.json","w",encoding='utf-8')
    f.write(open("data.json.bak","r",encoding='utf-8').read())
    f.close()

with open("./data.json",'r',encoding='utf-8') as load_f:
        dic=json.load(load_f)

def getAns(str):
    if str in dic:
        return dic[str]
    return "NULL"

def setAns(str,ans):
    dic[str]=ans
    with open("data.json","w",encoding='utf-8') as f:
        json.dump(dic,f)

def rmAns(str):
    if str in dic:
        dic.pop(str)
        with open("data.json","w",encoding='utf-8') as f:
            json.dump(dic,f)