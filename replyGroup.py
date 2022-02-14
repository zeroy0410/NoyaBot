from random import random
from pymysql import NULL
import requests,DataBase
from sqlalchemy import false
import calculatorSympy

talk_enable=set({892230531,878723783,675232402})
talk_probability={}
admin_uid=set({2020150384}) #管理员账号

def teach(uid,str,op):
    someNewRule=str.split("|")
    print(someNewRule)
    DataBase.setAns(someNewRule[0],someNewRule[1])
    sendMessage(uid,"诺雅学会了哦~",op)

def sendMessage(uid,message,op):
    url='http://127.0.0.1:5700'
    data={}
    if op==0:
        data={'message_type':'private','user_id':uid,'message':message}
    else:
        data={'message_type':'group','group_id':uid,'message':message}
    requests.get(url+'/send_msg',params=data)

def groupSolve(gid,uid,nickname,message):
    if_Ask=False
    content=message
    content=content.strip('\n')
    content=content.strip('\r')
    content=content+' '
    if content[0:4]=="/ask":
        content=content[5:-1]+' '
        if_Ask=True

    if content[0:6]=="/teach":
        teach(gid,content[7:-1],1)

    elif content[0:5]=="/echo":
        sendMessage(gid,content[6:-1],1)

    elif content[0:5]=="/calc":
        str="太难算了，不会QvQ"
        str=calculatorSympy.calc(content[6:-1])
        sendMessage(gid,str,1)

    elif content[0:7]=="/delete":
        if uid in admin_uid:
            DataBase.rmAns(content[8:-1])
            sendMessage(gid,"删除成功",1)
        else:
            sendMessage(gid,"你没有权限！",1)

    elif content[0:4]=="/let":
        if uid in admin_uid:
            if content[5:16]=="talk_enable":
                if content[17:21]=='True':
                    talk_enable.add(gid)
                    sendMessage(gid,"已开启闲聊~",1)
                else:
                    if gid in talk_enable:
                        talk_enable.remove(gid)
                        sendMessage(gid,"已关闭闲聊~",1)
            elif content[5:21]=="talk_probability":
                talk_probability[gid]=float(content[22:-1])
                sendMessage(gid,"闲聊概率已设定为: "+content[22:-1],1)
        else:
            sendMessage(gid,"你没有权限！",1)

    elif (gid in talk_enable) and DataBase.getAns(content[0:-1])!=NULL:
        check=random()
        if gid not in talk_probability:
            talk_probability[gid]=0.4
        print(check,talk_probability[gid])
        if check<talk_probability[gid] or if_Ask==True:
            if_Ask=False
            sendMessage(gid,DataBase.getAns(content[0:-1]),1)