import json
import os
import difflib
import random

from sqlalchemy import null
if not os.path.exists("textCorpus/data.json"):
    f = open("textCorpus/data.json", "w", encoding='utf-8')
    f.write(open("textCorpus.json.bak", "r", encoding='utf-8').read())
    f.close()

with open("textCorpus/data.json", 'r', encoding='utf-8') as load_f:
    dic = json.load(load_f)


def getAns(str):
    if str in dic:
        return dic[str]
    if 'image' not in str:
        lis = dic.keys()
        ans = difflib.get_close_matches(str, lis, 3, cutoff=0.5)
        print(ans)
        if ans != []:
            return dic[random.choice(ans)]
    return ''


def setAns(str, ans):
    dic[str] = ans
    with open("textCorpus/data.json", "w", encoding='utf-8') as f:
        json.dump(dic, f)


def rmAns(str):
    if str in dic:
        dic.pop(str)
        with open("textCorpus/data.json", "w", encoding='utf-8') as f:
            json.dump(dic, f)
        return True
    else:
        return False
